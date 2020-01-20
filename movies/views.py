from django.shortcuts import render
from .services import get_movies_with_its_cast
from django.conf import settings


def movie_list(request):
    movies = get_movies_with_its_cast(
            films_endpoint=settings.FILMS_ENDPOINT,
            people_endpoint=settings.PEOPLE_ENDPOINT,
        )
    return render(request, 'movies/movie_list.html', {'movies': movies})
