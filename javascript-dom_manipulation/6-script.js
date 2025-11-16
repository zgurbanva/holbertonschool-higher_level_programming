const characterDiv = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    characterDiv.textContent = data.name;
  })
  .catch((error) => {
    characterDiv.textContent = `Error: ${error.message}`;
  });
