from django.shortcuts import render, redirect 
from .models import Usercontact
from .views import *
from .forms import UsercontactForm
from django.utils import timezone

def newMessage(request): 
    if request.method == 'POST' : 
        form = UsercontactForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.created_at = timezone.now()
            comment.save()
            #return redirect('detailMessage', id)
        return redirect('messageList')
    else: 
        form = UsercontactForm()
        return render(request,'newMessage.html', {'form' : form})

def messageList(request):
    posts = Usercontact.objects.filter(fromID = request.user)
    return render(request,"messageList.html", {'posts': posts})

def sendMessage(request):
    posts = Usercontact.objects.filter(toID = request.user)
    return render(request,"sendMessage.html", {'posts': posts})

