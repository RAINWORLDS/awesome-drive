document.addEventListener("DOMContentLoaded", () => {
  fetch("/admin/users")
    .then(res => res.json())
    .then(users => {
      const userHtml = users.map(u =>
        `<p>ID: ${u.id} | Email: ${u.email || '无'} | Phone: ${u.phone || '无'}</p>`
      ).join("");
      document.getElementById("userList").innerHTML = userHtml;
    });

  fetch("/admin/files")
    .then(res => res.json())
    .then(files => {
      const fileHtml = files.map(f =>
        `<p>${f.filename} | 上传者 ID: ${f.owner_id} | 时间: ${f.created_at}</p>`
      ).join("");
      document.getElementById("fileList").innerHTML = fileHtml;
    });
});
