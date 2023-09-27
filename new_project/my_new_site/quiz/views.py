from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная страница",
        "username": "nikita",
    }
    return render(request, "quiz/index.html", context)


def about(request):
    return render(request, "quiz/about.html", {"title": "О сайте"})


def categories(request):
    return render(request, "quiz/categories.html", {'title': 'Категории'})
