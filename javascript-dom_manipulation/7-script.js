document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const moviesList = document.getElementById('list_movies');

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const { results } = data;

      results.forEach((film) => {
        const li = document.createElement('li');
        li.textContent = film.title;
        moviesList.appendChild(li);
      });
    })
    .catch((error) => {
      console.error('Error fetching movies:', error);
    });
});
