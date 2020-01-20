from django.test import TestCase
from django.conf import settings
import requests
from .services import merge_cast_with_movies

SAMPLE_FILMS = [
    {
        "id": "film-1",
        "title": "Castle in the Sky",
        "description": "The orphan Sheeta inherited a mysterious",
        "director": "Hayao Miyazaki",
        "producer": "Isao Takahata",
        "release_date": "1986",
        "rt_score": "95"
    },
    {
        "id": "film-2",
        "title": "Grave of the Fireflies",
        "description": "In the latter part of World War II, a boy",
        "director": "Isao Takahata",
        "producer": "Toru Hara",
        "release_date": "1988",
        "rt_score": "97"
    }
]

SAMPLE_PEOPLE = [
    {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Actor-A",
        "gender": "male",
        "age": "late teens",
        "eye_color": "brown",
        "hair_color": "brown",
        "films": [
            "https://ghibliapi.herokuapp.com/films/film-1"
        ],
        "species": "https://ghibliapi.herokuapp.com/species/",
        "url": "https://ghibliapi.herokuapp.com/people/"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Actor-B",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": [
            "https://ghibliapi.herokuapp.com/films/film-2"
        ],
        "species": "https://ghibliapi.herokuapp.com/species/",
        "url": "https://ghibliapi.herokuapp.com/people/"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Actor-C",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": [
            "https://ghibliapi.herokuapp.com/films/film-2"
        ],
        "species": "https://ghibliapi.herokuapp.com/species/",
        "url": "https://ghibliapi.herokuapp.com/people/"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Actor-D",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": [
            "https://ghibliapi.herokuapp.com/films/film-1",
            "https://ghibliapi.herokuapp.com/films/film-2"
        ],
        "species": "https://ghibliapi.herokuapp.com/species/",
        "url": "https://ghibliapi.herokuapp.com/people/"
    }
]


class UnitTest(TestCase):

    def test_movies_page_loads(self):
        response = self.client.get('http://localhost:8000/movies/')
        self.assertTemplateUsed(response, 'movies/movie_list.html')
        self.assertTrue(response.status_code == 200)

    # For our application to keep working,
    # we need to make sure that the 3rd party api has the required fields

    def test_movies_end_point(self):
        response = requests.get(settings.FILMS_ENDPOINT)
        self.assertTrue(response.status_code == 200)
        response_json = response.json()

        for item in [
                'id', 'title', 'description', 'director', 'producer',
                'release_date', 'rt_score']:
            self.assertTrue(item in response_json[0].keys())

    def test_people_end_point(self):
        response = requests.get(settings.PEOPLE_ENDPOINT)
        self.assertTrue(response.status_code == 200)
        response_json = response.json()

        for item in ['name', 'films', 'url']:
            self.assertTrue(item in response_json[0].keys())

    def get_cast_names(self, movie):
        cast = []
        for people in movie['people']:
            cast.append(people['name'])
        return cast

    def test_movies_has_people(self):
        movies_with_people = merge_cast_with_movies(
                SAMPLE_FILMS,
                SAMPLE_PEOPLE,
            )

        # Actor-A in film-1
        # Actor-B and Actor-C in film-2
        # Actor-D in both film-1 and film-2
        cast_film_1 = ['Actor-A', 'Actor-D']
        cast_film_2 = ['Actor-B', 'Actor-C', 'Actor-D']
        for movie in movies_with_people:
            if movie['id'] == 'film-1':
                self.assertEqual(len(movie['people']), 2)
                cast = self.get_cast_names(movie)
                self.assertEqual(set(cast_film_1), set(cast))
            else:
                self.assertEqual(len(movie['people']), 3)
                cast = self.get_cast_names(movie)
                self.assertEqual(set(cast_film_2), set(cast))
