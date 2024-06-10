from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

class Demo():
    def root_route(request):
        template = loader.get_template('root.html')
        return HttpResponse(template.render())

    def login_page(request):
        return render(request, 'intro/login.html')


    def register_page(request):
        name = "Muhammad"
        address = "Betmore, Mathbaria"
        age = 23
        
        data = {"name": name, "address": address, "age": age}
        fruits = {"fruits": ["Banana", "Apple", "Orange"]}
        context = {**data, **fruits}
        
        return render(request, "register.html", context=context)

    

