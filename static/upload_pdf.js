const scroll = new LocomotiveScroll({
    el: document.querySelector('[data-scroll-container]'),
    smooth: true
});
// JavaScript to update the file name display
const fileInput = document.getElementById('file-input');
const fileNameParagraph = document.getElementById('file-name');

fileInput.addEventListener('change', function () {
    // Display the selected file name when a file is selected
    fileNameParagraph.textContent = this.files[0].name;
});

document.addEventListener("DOMContentLoaded", function() {
    // Check if the summary container has content
    const summaryContainer = document.getElementById('summary_container');
    if (summaryContainer.textContent.trim() !== '') {
        // If it has content, clear it
        summaryContainer.innerHTML = '';
    }

    // Listen for page reload event
    window.addEventListener('beforeunload', function(event) {
        // Clear the summary container when the page is reloaded
        summaryContainer.innerHTML = '';
    });
});
