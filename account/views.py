from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
    
def register(request):
    return render(request, 'register.html')
    
def profile(request):
    return render(request, 'profile.html')
    
def forget_pwd(request):
    return render(request, 'forget_pwd.html')