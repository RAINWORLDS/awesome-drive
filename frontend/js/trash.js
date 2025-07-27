function deleteToTrash(filename) {
  const uid = localStorage.getItem("user_id") || 1;
  fetch(`/trash/delete/${filename}?user_id=${uid}`, { method: "POST" })
    .then(res => res.json())
    .then(data => alert(data.message));
}
