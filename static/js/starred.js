function click_download(download_id) {
    document.getElementById(download_id).click();
}


function download(download_id) {
    let downloadButton = document.querySelector('.download');
    // document.getElementById('download').click();
    if (downloadButton) {
        click_download(download_id);

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


function remove_from_favourite(file_id, csrf_token) {

	$.post("", {
		star_id: file_id,
		csrfmiddlewaretoken: csrf_token
	});

}



function delete_file(deleted, file_id, csrf_token) {
	document.getElementById(deleted).style.color = "red";

	$.post("", {
		star_id: file_id,
		csrfmiddlewaretoken: csrf_token
	});
}
