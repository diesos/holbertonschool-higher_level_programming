const divEl = document.getElementById("red_header")
const headEl = document.querySelector("header")

divEl.addEventListener("click", myFunction)

function myFunction() {
	headEl.style.color = "#FF0000"
}
