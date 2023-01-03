from django.shortcuts import render

def error(request):
    return render(request, '404.html')
    
def about(request):
    return render(request, 'about-page.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def faq(request):
    return render(request, 'faq.html')

def home(request):
    return render(request, 'index.html')  

def search(request):
    return render(request, 'search.html')
