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



function clears(event) {

    var record = confirm("Do you want to clear?");

    if (record == true) {
        $("#staticBackdrop").load(location.href + " #staticBackdrop>*", "");

    } else {
        event.stopImmediatePropagation();
        event.preventDefault();
        return false;
    }


}


function validateSize(input) {
    const fileSize = input.files[0].size / 1024 / 1024;
    if (fileSize > 5) {
        alert('File size exceeds 5 MB');
        input.value = "";
        return;
    }
}


function click_download() {
    alert("hello");
    document.getElementById('download').click();
}


function download() {
    let downloadButton = document.querySelector('.download');
    // document.getElementById('download').click();
    if (downloadButton) {
        click_download();
        
        downloadButton.addEventListener('click', function (event) {
            event.preventDefault();

            /* Start loading process. */
            downloadButton.classList.add('loading');
            

            /* Set delay before switching from loading to success. */
            window.setTimeout(function () {
                downloadButton.classList.remove('loading');
                downloadButton.classList.add('success');
            }, 2000);

           

            /* Reset animation. */
            window.setTimeout(function () {
                downloadButton.classList.remove('success');
            }, 4000);

            

        });
    };
}


function rename() {

    if(document.getElementById('rename').style.display == "none") {
        document.getElementById('rename').style.display = "block";
    } else {
        document.getElementById('rename').style.display = "none";
    }

    document.getElementById('before').style.display = "none";
    document.getElementById('after').style.display = "block";
}


function before_button() {
    document.getElementById('before').style.display = "block";
    document.getElementById('after').style.display = "none";

    document.getElementById('rename').style.display = "none";
}


function submitNewFileName() {
    let form = document.getElementById("newfilename_submit");
    form.submit();
}
