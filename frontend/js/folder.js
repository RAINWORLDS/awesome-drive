function createFolder() {
  const name = document.getElementById("folderName").value;
  const ownerId = localStorage.getItem("user_id") || 1;
  fetch("/folder/create?name=" + name + "&owner_id=" + ownerId, { method: "POST" })
    .then(res => res.json())
    .then(data => alert(data.message));
}
