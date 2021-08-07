from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Mara
from .forms import maraForm

# Create your views here.

def home(request):
    article = Mara.objects.all()
    articleList = Mara.objects.all()
    paginator = Paginator(articleList, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'home.html',{'article' : article, 'posts' : posts})

def detail(request, article_id):
    article_detail = get_object_or_404(Mara, pk = article_id)
    return render(request, 'detail.html' ,{'article' : article_detail})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = maraForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = maraForm()
        return render(request,'new.html', {'form':form})


def edit(request, article_id):
    post = get_object_or_404(Mara, pk = article_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = maraForm(instance = post)
        return render(request, 'edit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = maraForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/marablog/detail/' + str(article_id))
        return redirect('home')

def delete(request, article_id):
    article_delete =  Mara.objects.get(id = article_id)
    article_delete.delete()
    return redirect('home')