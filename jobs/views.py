from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import user
from .form import RegisterUserForm

#Register applicant only
def register_applicant(request):
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_applicant=True


def index(request):
    return render(request, 'jobs/index.html')

def about(request):
    return render(request, 'jobs/about.html')

def contact(request):
    if request.method=='POST':
        name=request.post.get('form-group')
        submit=submit in request.post
    return render(request, 'jobs/contact.html')

def careers(request):
    return render(request, 'jobs/careers.html')
