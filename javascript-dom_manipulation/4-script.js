const itemEl = document.getElementById("add_item")
const listEl = document.querySelector(".my_list")

itemEl.addEventListener("click", myFunction)

function myFunction() {
	listEl.innerHTML += `<li>Item</li>`
}
