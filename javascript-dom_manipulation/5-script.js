const headEl = document.querySelector("header")
const divEl = document.getElementById("update_header")

divEl.addEventListener("click", () =>{
	headEl.innerHTML = "New Header!!!"
})
