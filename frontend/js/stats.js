document.addEventListener("DOMContentLoaded", () => {
  fetch("/files/stats")
    .then(res => res.json())
    .then(stats => {
      document.body.innerHTML += `
        <h2>📊 系统统计</h2>
        <p>用户数：${stats["用户数"]}</p>
        <p>文件数：${stats["文件数"]}</p>
        <p>总容量：${stats["总容量（MB）"]} MB</p>
      `;
    });
});
