from django.shortcuts import render, redirect
from .models import Project, Certificate,Education
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    projects = Project.objects.all()
    certs = Certificate.objects.all()
    education_list=Education.objects.all()
    # Contact form POST işləməsi
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f'New Contact Form Submission from {name}, Email: {email}',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL], 
        )
        return redirect('home')  # form göndərildikdən sonra səhifəni reload et

    return render(request, 'home.html', {
        'projects': projects,
        'certs': certs,
        'education_list': education_list
    })
