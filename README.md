# Movie List

  Studio Ghibli is a Japanese movie company. They offer a ​[REST API](https://ghibliapi.herokuapp.com/) where one can query
  information about movies and people (characters).
  The task is to write a Python application which serves a page on localhost:8000/movies/. This
  page should contain a plain list of all movies from the Ghibli API. For each movie the people that
  appear in it should be listed.
  Do not use the ​ people ​ field on the ​ /films​ endpoint, since it’s broken. There is a list field called
  films ​ on the ​ /people ​ endpoint which you can use to get the relationship between movies and
  the people appearing in them.
  You don’t have to worry about the styling of that page.
  Since accessing the API is a time-intensive operation, it should not happen on every page load.
  But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so
  make sure that the information on the page is not older than 1 minute when the page is loaded.
  The code should be submitted in a clean and refactored state. Please format the code
  according to the PEP8 conventions.
  Don’t forget to test your code. Your tests don’t have to be complete, but you should describe
  how you would extend them if you had the time.If you have to skip some important work due to time limitations, feel free to add a short
  description of what you would improve and how if you had the time for it.
