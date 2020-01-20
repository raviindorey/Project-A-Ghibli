from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from .services import get_movies_with_its_cast


def movie_list(request):
    movies = cache.get('movies')
    if not movies:
        movies = get_movies_with_its_cast(
                films_endpoint=settings.FILMS_ENDPOINT,
                people_endpoint=settings.PEOPLE_ENDPOINT,
            )
        cache.set('movies', movies)
    return render(request, 'movies/movie_list.html', {'movies': movies})
