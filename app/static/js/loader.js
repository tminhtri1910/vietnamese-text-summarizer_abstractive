document.addEventListener("DOMContentLoaded", function() {
    // Change from summary-button to summarize-button
    const summarizeButton = document.getElementById("summarize-button");
    const loader = document.getElementById("loading-indicator");

    if (summarizeButton) {
        summarizeButton.addEventListener("click", function() {
            loader.style.display = "block"; // Show loader

            // Simulate a delay for the summarization process
            setTimeout(function() {
                loader.style.display = "none"; // Hide loader
            }, 3000); // Adjust time as needed for actual processing
        });
    }
});