let currentPage = 1;
const perPage = 10;

function loadFiles() {
  fetch("/files/list")
    .then(res => res.json())
    .then(files => {
      const start = (currentPage - 1) * perPage;
      const pageFiles = files.slice(start, start + perPage);
      const table = document.querySelector("#fileTable tbody");
      table.innerHTML = "";

      pageFiles.forEach(file => {
        const row = `<tr>
          <td>${file.filename}</td>
          <td>${(file.size / 1024).toFixed(2)} KB</td>
          <td>
            <a href="/files/download/${file.filename}">下载</a> |
            <a href="#" onclick="previewImage('${file.filename}')">预览</a> |
            <a href="#" onclick="deleteFile('${file.filename}')">删除</a>
          </td>
        </tr>`;
        table.innerHTML += row;
      });
    });
}

function nextPage() {
  currentPage++;
  loadFiles();
}

function prevPage() {
  if (currentPage > 1) {
    currentPage--;
    loadFiles();
  }
}

document.addEventListener("DOMContentLoaded", loadFiles);
