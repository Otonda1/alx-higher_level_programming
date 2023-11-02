const movies = $('UL#list_movies');
$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  (data) => {
    const films = data.results;
    films.forEach(film => {
      movies.append('<li>' + film.title + '</li>');
    });
  });
