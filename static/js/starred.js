function click_download() {
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