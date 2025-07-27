const lang = localStorage.getItem("lang") || "zh";

function translateUI() {
  if (lang === "en") {
    document.querySelector("h1").innerText = "File Manager";
    document.querySelector("button").innerText = "Create Folder";
  }
}

window.onload = translateUI;
