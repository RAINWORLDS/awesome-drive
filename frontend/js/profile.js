document.addEventListener("DOMContentLoaded", () => {
  const userId = localStorage.getItem("user_id") || 1;

  fetch(`/user/me/${userId}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("profile").innerHTML = `
        <p>📧 邮箱: ${data.email || '未绑定'}</p>
        <p>📱 手机: ${data.phone || '未绑定'}</p>
        <p>🐙 GitHub ID: ${data.github_id || '未绑定'}</p>
      `;
    });

  document.getElementById("avatarImg").src = `/files/download/avatar_${userId}.jpg`;
});

function uploadAvatar() {
  const file = document.getElementById("avatar").files[0];
  const formData = new FormData();
  formData.append("file", file);
  formData.append("user_id", localStorage.getItem("user_id") || 1);

  fetch("/files/avatar", {
    method: "POST",
    body: formData
  }).then(res => res.json())
    .then(data => {
      alert("上传成功！");
      location.reload();
    });
}
