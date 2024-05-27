document.addEventListener("DOMContentLoaded", () => {
    async function fetchHello() {
        try {
            const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
            const data = await response.json();
            const divEl = document.getElementById('hello');
            if (divEl) {
                divEl.textContent = data.hello;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    fetchHello();
});
