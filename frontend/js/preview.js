function previewImage(filename) {
  const img = document.createElement("img");
  img.src = `/files/preview/${filename}`;
  img.style.maxWidth = "300px";
  const div = document.createElement("div");
  div.appendChild(img);
  document.body.appendChild(div);
}
