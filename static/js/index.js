function openTab(event, tabId) {
  // 1. Reset all tabs
  document.querySelectorAll(".tab").forEach((t) => {
    t.style.display = "none";
  });

  // 2. Reset all buttons (remove the 'active' class)
  document.querySelectorAll(".btn-tab").forEach((btn) => {
    btn.classList.remove("active");
  });

  // 3. Show the specific tab
  document.getElementById(tabId).style.display = "block";

  // 4. Add 'active' class to the button that was clicked
  event.currentTarget.classList.add("active");
}
