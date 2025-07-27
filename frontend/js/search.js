function searchFiles() {
  const query = document.getElementById("query").value;
  fetch(`/files/search?query=${query}`)
    .then(res => res.json())
    .then(data => {
      const result = document.getElementById("results");
      result.innerHTML = data.results.map(f =>
        `<p>${f}</p>`
      ).join("");
    });
}
