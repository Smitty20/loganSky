from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse
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
    
def submit(request):
    client = Client()
    order = Order()
    randvar = False
    template = loader.get_template('sky/submit.html')
    context = {
        'dont know why I need this': randvar,
    }
    try:
        f_name = request.POST['first']
        l_name = request.POST['last']
        add = request.POST['address']
        serv = request.POST['service']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'sky/input.html')
    else:
        client.first_name = f_name
        client.last_name = l_name
        client.address = add
        
        client.save()
        
        order.client = client
        order.service = serv
        order.order_date = timezone.now()
        
        order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponse(template.render(context, request))  