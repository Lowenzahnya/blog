from django.shortcuts import render, redirect
from .models import Task
from blog.main.forms import TaskForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def detail(request, pk):
    try:
        article = Task.objects.get(id=pk)
        latest_comments = article.comment_set.order_by("-id")[:10]
    except:
        raise Http404('Статья не найдена')

    return render(request, 'main/detail.html', {'article': article, 'latest_comments': latest_comments})


def comment(request, pk):
    article = Task.objects.get(id=pk)
    article.comment_set.create(author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('detail', args=(article.id,)))


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ERROR: Невермая форма'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
