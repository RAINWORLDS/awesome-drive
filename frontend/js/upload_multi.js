function uploadMultiple(files) {
  const formData = new FormData();
  for (const file of files) {
    formData.append("files", file);
  }
  fetch("/upload/multiple", {
    method: "POST",
    body: formData
  }).then(res => res.json())
    .then(data => alert("上传成功: " + data.count + " 个文件"));
}
