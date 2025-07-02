document.getElementById('summarize-button').addEventListener('click', function() {
    const textInput = document.getElementById('text-input').value;
    const fileInput = document.getElementById('file-input').files[0];
    const summaryResults = document.getElementById('summary-results');
    const loader = document.getElementById('loader');

    if (!textInput && !fileInput) {
        alert('Please enter text or upload a file.');
        return;
    }

    loader.style.display = 'block';
    summaryResults.innerHTML = '';

    const formData = new FormData();
    if (textInput) {
        formData.append('text', textInput);
    }
    if (fileInput) {
        formData.append('file', fileInput);
    }

    fetch('/summarize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = 'none';
        if (data.error) {
            alert(data.error);
            return;
        }

        summaryResults.innerHTML = `
            <h3>Summarization Results</h3>
            <h4>K-means Summary:</h4>
            <p>${data.kmeans_summary}</p>
            <h4>TextRank Summary:</h4>
            <p>${data.textrank_summary}</p>
            <h4>ROUGE Comparison:</h4>
            <p>${data.rouge_results}</p>
        `;
    })
    .catch(error => {
        loader.style.display = 'none';
        console.error('Error:', error);
        alert('An error occurred while processing your request.');
    });
});