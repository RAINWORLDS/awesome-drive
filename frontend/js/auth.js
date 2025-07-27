function sendEmailCode() {
  fetch("/auth/email/send", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: document.getElementById("email").value })
  });
}

function verifyEmail() {
  fetch("/auth/email/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email: document.getElementById("email").value,
      code: document.getElementById("emailCode").value
    })
  }).then(res => res.json()).then(data => alert("登录成功，用户ID：" + data.user_id));
}

function sendPhoneCode() {
  fetch("/auth/phone/send", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone: document.getElementById("phone").value })
  });
}

function verifyPhone() {
  fetch("/auth/phone/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      phone: document.getElementById("phone").value,
      code: document.getElementById("phoneCode").value
    })
  }).then(res => res.json()).then(data => alert("登录成功，用户ID：" + data.user_id));
}

function githubLogin() {
  window.location.href = "/auth/github/login";
}
