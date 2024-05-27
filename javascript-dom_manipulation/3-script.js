const divEl = document.getElementById("toggle_header")
const headEl = document.querySelector("header")

divEl.addEventListener("click", myFunction)

function myFunction() {
	console.log("ok")
	if (headEl.className === 'red')
		headEl.className = 'green'
	else
	headEl.className ='red'
}
