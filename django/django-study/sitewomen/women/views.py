from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

def index(request):
    #t = render_to_string('women/index.html')
    menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
    data = {'title': 'Главная страница',
            'menu': menu
            }
    return render(request, 'women/index.html', context=data)

def categories(request):
    return HttpResponse('<h1> Статьи по категориям </h1>')

def categories_by_id(request, cat_id):
    return HttpResponse(f'<h1> Статьи по категориям </h1> <p> cat_id: {cat_id} </p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1> Статьи по категориям </h1><p> cat_slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам </h1> <p> year: {year} </p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

def about(request):
    data = {'title': 'о сайте'}
    return render(request, 'women/about.html', data)