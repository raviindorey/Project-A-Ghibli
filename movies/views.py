from django.shortcuts import render


def movie_list(request):
    return render(request, 'movies/movie_list.html')
