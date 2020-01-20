import requests
from django.conf import settings


def merge_cast_with_movies(all_films, all_people):
    """
    We are creating a film_people dictionary which
    will contain the film id as keys and information of
    peoples as values.

    film_people = {'film_id', [{people_1}, {people_2}, ...]}
    """

    film_people = {}

    for people in all_people:
        films = people['films']
        for film in films:
            film_id = film.split(settings.FILMS_ENDPOINT)[1]
            if film_id in film_people.keys():
                film_people[film_id].append(people)
            else:
                film_people[film_id] = [people]

    for film in all_films:
        people = film_people.get(film['id'])
        film['people'] = people

    return all_films


def get_movies_with_its_cast(*, films_endpoint, people_endpoint):

    all_films = requests.get(films_endpoint).json()
    all_people = requests.get(people_endpoint).json()

    return merge_cast_with_movies(all_films, all_people)
