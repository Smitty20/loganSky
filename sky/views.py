from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader

from .models import Client, Order

def home(request):
    randvar = False
    template = loader.get_template('sky/home.html')
    context = {
        'dont know why I need this': randvar,
    }
    return HttpResponse(template.render(context, request))
    
def contact(request):
    randvar = False
    template = loader.get_template('sky/contact.html')
    context = {
        'dont know why I need this': randvar,
    }
    return HttpResponse(template.render(context, request))

def purchase(request):
    randvar = False
    template = loader.get_template('sky/input.html')
    context = {
        'dont know why I need this': randvar,
    }
    return HttpResponse(template.render(context, request))