document.addEventListener("DOMContentLoaded", () => {
  const cells = document.querySelectorAll("td");
  const clickedCells = JSON.parse(localStorage.getItem("clickedCells")) || [];

  cells.forEach((cell, index) => {
    if (clickedCells.includes(index)) {
      cell.classList.add("clicked");
    }
    cell.addEventListener("click", () => {
      cell.classList.toggle("clicked");
      const updatedClicked = [];
      cells.forEach((ce, idx) => {
        if (ce.classList.contains("clicked")) updatedClicked.push(idx);
      });
      localStorage.setItem("clickedCells", JSON.stringify(updatedClicked));
    });
  });
});
