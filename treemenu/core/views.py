from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')

def contacts(request):
  return render(request, 'contacts.html')

def blogs(request):
  return render(request, 'blogs.html')

def blog_detail(request, blog_id):
  return render(request, 'blog_detail.html', {'blog': blog_id})