async function uploadImage() {
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    let formData = new FormData();
    formData.append("image", file);

    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let data = await response.json();
    document.getElementById("messages").innerHTML += `<p>Bot: ${data.response}</p>`;
}

function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    document.getElementById("messages").innerHTML += `<p>You: ${userInput}</p>`;
    document.getElementById("userInput").value = "";
}