function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);
  formData.append("user_id", 1);
  fetch("/files/upload", {
    method: "POST",
    body: formData
  }).then(res => res.json())
    .then(data => {
      alert("上传成功：" + data.filename);
      location.reload();
    });
}
