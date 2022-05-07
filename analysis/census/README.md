# Scripts to pre-process and upload Australia 2016 Census Data

## setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage
```
-h help
--db DATABASE_NAME
--census CENSUS_FILE_PATH 
--type CENSUS_DATA_TYPE 
[--year CENSUS_YEAR]
```
## Upload pre-processed census JSON file
Example:
```
python data_loader.py \
    --db census \
    --type ancestry \
    --code G08 \
    --file census_LGA-G08_proportions.json
```