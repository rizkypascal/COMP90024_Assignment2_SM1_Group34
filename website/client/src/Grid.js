import { useState } from 'react';
import { AgGridReact } from 'ag-grid-react'; // the AG Grid React Component

import 'ag-grid-community/dist/styles/ag-grid.css'; // Core grid CSS, always needed
import 'ag-grid-community/dist/styles/ag-theme-alpine.css'; // Optional theme CSS

const Grid = ({ data, type }) => {
    const [rowData, setRowData] = useState(data);
    const [columns, setColumns] = useState([
        { field: type },
        { field: 'proportion' },
        { field: 'value' },
    ])

    return (
        <div>
            <div className="ag-theme-alpine" style={{ height: 400, width: 600 }}>
                <AgGridReact rowData={rowData} columnDefs={columns}></AgGridReact>
            </div>
            <div>
                <p>Out of {rowData[0]['total']} persons living in this LGA</p>
            </div>
        </div>
    )
}

export default Grid;