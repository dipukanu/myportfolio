from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail  
from django.conf import settings
# Create your views here.

def Home(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg="You have got a new message from your Portfolio. Please check it by login into your account 'https://portfoliobydipu.herokuapp.com/admin'"
            to='dipukanu96@gmail.com'
            send_mail('New Contact from Portfolio', msg, settings.EMAIL_HOST_USER, [to]) 
            messages.info(request, "Your message has been sent successfully!")
            return redirect('/#contact')
    else:
        form = ContactForm()
        return render(request, 'mycv.html',{'form':form})

def work(request):
    return render(request, 'work_more.html')
    