from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

def sendmail(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        title = request.POST.get('title')
        content = request.POST.get('content')
        mail = EmailMessage(title, content, to=[address])
        mail.send()
        return redirect ("done")
    else:
        return render(request, 'mailIndex.html')

def done(request):
    return render(request, 'done.html')
