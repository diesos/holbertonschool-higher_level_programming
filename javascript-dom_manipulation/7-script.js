
const ulEl = document.getElementById("list_movies")

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(res =>res.json())
.then(data => {
	const title = data.results.map(result => result.title)
	title.forEach(title => ulEl.innerHTML += `<li>${title}</li>`)
	})
