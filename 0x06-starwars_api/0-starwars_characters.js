#!/usr/bin/node

// Import the request module
const request = require('request');
const args = process.argv;
const arg1 = args[2];

// Define the URL you want to make a request to
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg1 + '/';

// Make a GET request to fetch film data
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const filmData = JSON.parse(body);

  // Extract characters array
  const characters = filmData.characters;

  // Function to fetch character data recursively and display names
  const fetchAndDisplayCharacterNames = (index) => {
    if (index >= characters.length) {
      return; // Base case: if all characters are processed, stop recursion
    }

    const characterUrl = characters[index];

    // Make a GET request to each character URL
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the JSON response body of each character
      const characterData = JSON.parse(body);

      // Extract and log the name of each character
      console.log(characterData.name);

      // Recursive call to fetch and display next character's name
      fetchAndDisplayCharacterNames(index + 1);
    });
  };

  // Start fetching and displaying character names
  fetchAndDisplayCharacterNames(0);
});
