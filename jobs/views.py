from django.shortcuts import render

def index(request):
    return render(request, 'jobs/index.html')

def about(request):
    return render(request, 'jobs/about.html')

def contact(request):
    if request.method=='post':
        name=request.post.get('form-group')
        submit=submit in request.post
    return render(request, 'jobs/contact.html')

def careers(request):
    return render(request, 'jobs/careers.html')
