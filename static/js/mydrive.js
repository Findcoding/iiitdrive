
function addRows(emptbl, col) {
    var table = document.getElementById(emptbl);
    var rowCount = table.rows.length;
    var cellCount = table.rows[0].cells.length;
    var row = table.insertRow(rowCount);

    for (var i = 0; i <= cellCount; i++) {
        var cell = 'cell' + i;
        cell = row.insertCell(i);

        if (document.getElementById(col + i) != null) {
            var copycel = document.getElementById(col + i).innerHTML;
            cell.innerHTML = copycel;
        }

    }

}



function deleteRows(emptbl) {
    var table = document.getElementById(emptbl);
    var rowCount = table.rows.length;
    if (rowCount > '1') {
        var row = table.deleteRow(rowCount - 1);
        rowCount--;
    } else {
        alert('There should be atleast one row');
    }

}



function clears() {

    $("#staticBackdrop").load(location.href + " #staticBackdrop>*", "");

}