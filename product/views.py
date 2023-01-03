from django.shortcuts import render

def product_page(request):
    return render(request, 'product-page.html')
    
def vendor_profile(request):
    return render(request, 'vendor-profile.html')
