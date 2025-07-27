function uploadWithProgress(file) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/upload/progress");
  xhr.upload.onprogress = (e) => {
    const percent = (e.loaded / e.total * 100).toFixed(2);
    document.getElementById("progressBar").style.width = percent + "%";
  };
  const formData = new FormData();
  formData.append("file", file);
  xhr.send(formData);
}
