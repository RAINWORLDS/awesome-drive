function shareFile(filename) {
  fetch(`/files/share/${filename}`, { method: "POST" })
    .then(res => res.json())
    .then(data => {
      prompt("复制分享链接：", window.location.origin + data.share_url);
    });
}
