fetch("/api/health")
  .then((res) => res.json())
  .then((data) => {
    document.getElementById("health-status").textContent =
      "API status: " + data.status;
  })
  .catch(() => {
    document.getElementById("health-status").textContent =
      "API status: unreachable";
  });
