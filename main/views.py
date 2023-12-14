from django.shortcuts import render, redirect
from .models import Task, Products
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Отзывы', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def news(request):
    return render(request, 'main/news.html')


def kontakt(request):
    return render(request, 'main/kontakt.html')


def bros(request):
    product = Products.objects.all()
    return render(request, 'main/bros.html', {'product': product})


def chashka(request):
    return render(request, 'main/chashka.html')


def panda(request):
    return render(request, 'main/panda.html')


def prazd(request):
    return render(request, 'main/prazd.html')


def cena(request):
    return render(request, 'main/cena.html')