document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = document.getElementById('image-input').files[0];
    const formData = new FormData();
    formData.append('image', input);

    // Clear previous results but keep the image preview
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    // Show loading spinner
    const loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'loading-spinner';
    resultDiv.appendChild(loadingSpinner);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();

    // Remove loading spinner
    resultDiv.removeChild(loadingSpinner);

    // Display the parsed JSON data
    const parsedDataDiv = document.createElement('div');
    parsedDataDiv.className = 'section';
    parsedDataDiv.innerHTML = `
        <h2>Parsed Data:</h2>
        <pre>${JSON.stringify(result.parsed_data, null, 2)}</pre>
        <button onclick="copyToClipboard('${JSON.stringify(result.parsed_data, null, 2).replace(/\n/g, '\\n')}')">Copy to Clipboard</button>
    `;
    resultDiv.appendChild(parsedDataDiv);

    // Keep the image preview visible
    const imagePreview = document.getElementById('image-preview');
    imagePreview.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

document.getElementById('image-input').addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById('image-preview');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';  // Ensure the preview is visible
        };
        reader.readAsDataURL(file);
    }
});

function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text.replace(/\\n/g, '\n');
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied to clipboard');
}

// Toggle dark mode
document.getElementById('toggle-switch').addEventListener('change', (e) => {
    document.body.classList.toggle('dark-mode', e.target.checked);
});