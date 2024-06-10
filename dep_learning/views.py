from django.http import HttpResponse
from django.template import loader

def deep_learning(request):
    template = loader.get_template('dl.html')
    return HttpResponse(template.render())

def machine_learning(request):
    template = loader.get_template('ml.html')
    return HttpResponse(template.render())