from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def customHomePage(request):
#     return HttpResponse('My Django application custom home page')

def customHomePage(request):
    # return render(request, template_name='customHomePage.html')
    return render(request, 'customHomePage.html')
