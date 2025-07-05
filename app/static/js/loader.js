document.addEventListener("DOMContentLoaded", function() {
    // Change from summary-button to summarize-button
    const summarizeButton = document.getElementById("summarize-button");
    const loader = document.getElementById("loading-indicator");

    if (summarizeButton) {
        summarizeButton.addEventListener("click", function() {
            loader.style.display = "block"; // Show loader

            fetch('/', { method: 'POST' })
                .then(response => {
                    if (!response.ok) throw new Error("Có lỗi từ server");
                    return response.text(); // hoặc .blob(), .arrayBuffer() tùy loại dữ liệu
                })
                .then(data => {
                    console.log('Phản hồi từ server:', data); // có thể là HTML, plain text, v.v.
                    loader.style.display = 'none'; // ✅ Ẩn loader sau khi có phản hồi
                })
                .catch(error => {
                    console.error('Lỗi khi fetch:', error);
                    loader.style.display = 'none'; // ❗ Vẫn ẩn loader nếu có lỗi
                });
            
            
            // // Simulate a delay for the summarization process
            // setTimeout(function() {
            //     loader.style.display = "none"; // Hide loader
            // }, 3000); // Adjust time as needed for actual processing
        });
    }
});