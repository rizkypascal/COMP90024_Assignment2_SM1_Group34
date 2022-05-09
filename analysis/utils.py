import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


from db_utils import DbUtils


def load_polygons():
    """Load lga polygons.

    Returns:
        _type_: _description_
    """
    db = DbUtils.connect(db_name="lga")
    query = {
        "selector": {
            "geometry": {
                "$ne": None
            }
        },
        "limit": 100
    }

    all_polygons = []
    for doc in db.find(query):
        try:
            # One of: "MultiPolygon", "Polygon"
            geo_type = doc.get("geometry", {}).get("type")

            all_rows = doc.get("geometry", {}).get("coordinates", [])
            # if not multi, make it an array
            if geo_type == "Polygon":
                all_rows = [all_rows]

            for row in all_rows:
                coordinates = doc.get("geometry", {}).get("coordinates", [])[0]

                if geo_type == "MultiPolygon":
                    coordinates = coordinates[0]

                lons_vect = []
                lats_vect = []
                for point in coordinates:
                    lons_vect.append(point[0])
                    lats_vect.append(point[1])

                lons_lats_vect = np.column_stack((lons_vect, lats_vect)) # Reshape coordinates
                polygon = Polygon(lons_lats_vect) # create polygon
                # polygon = Polygon(coordinates) # create polygon

                obj = {
                    "data": {
                        "lga_name_2016": doc.get("properties", {}).get("lga_name_2016"),
                        "lga_code_2016": doc.get("properties", {}).get("lga_code_2016"),
                    },
                    "polygon": polygon
                }
                all_polygons.append(obj)
        except Exception as e:
            name = doc.get("properties", {}).get("lga_name_2016")
            print(f"Failed to load polygon {name}: {e}")

    return all_polygons

def assign_lga_to_tweet(polygons, doc):
    """Assign LGA to tweet.

    Args:
        polygons (list of Polygons): LGA polygons
        doc (dict): a tweet
    """
    try:
        geo = doc.get("geo")
        if geo is None:
            return doc

        coordinates = geo.get("coordinates", [])
        
        point = Point(coordinates[1], coordinates[0]) # create point

        found_lga = False
        for obj in polygons:
            polygon = obj.get("polygon")
            if point.within(polygon):
                found_lga = True # check if a point is in the polygon 
            elif polygon.contains(point):
                found_lga = True
            elif point.touches(polygon):
                found_lga = True

            old_extra = doc.get("extra", {})
            if found_lga is True:
                print(f"LGA FOUND. Tweet ID: {doc['_id']}")
                lga = obj.get("data")
                lga_data = {"lga": lga}
                doc["extra"] = {**old_extra, **lga_data}
                return doc
            else:
                print(f"LGA UNKNOWN. Tweet ID: {doc['_id']}")
                lga_unknown = {"lga_unknown": True}
                doc["extra"] = {**old_extra, **lga_unknown}
                return doc

        return doc

    except Exception as e:
        print(f"Some error occurred when assigning LGA to a tweet: {e}")
