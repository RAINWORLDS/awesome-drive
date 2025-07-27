function saveUser(userId) {
  localStorage.setItem("user_id", userId);
}

function getUser() {
  return localStorage.getItem("user_id");
}

function logout() {
  localStorage.removeItem("user_id");
  window.location.href = "login.html";
}
