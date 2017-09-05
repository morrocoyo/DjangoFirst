from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import random
import pickle

# Create your views here.
# function based view 

def home(request):
    num = random.randint(0,1000); num2= random.randint(0,1000); num3= random.randint(0,1000);
    some_list=[num, num2, num3]
    context = {
            "bool_item": True, 
            "num":num,
            "some_list": some_list,
            }
    return render(request, "home.html", context)

def redes(request):
    TweetsAmb = pickle.load(open('/home/juang/Documents/Python Scripts/Genesis/Data/TweetsAmb', "rb" ) )
    TA=[t[2] for t in TweetsAmb[0:15]]
    context = {"TA": TA
            }
    return render(request, "redes.html", context)

def articulos(request):
    context = {
            }
    return render(request, "articulos.html", context)


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kargs):
        context = super(HomeView, self).get_context_data(*args, **kargs)
        num = random.randint(0,1000); num2= random.randint(0,1000); num3= random.randint(0,1000);
        some_list=[num, num2, num3]
        context = {
            "bool_item": True, 
            "num":num,
            "some_list": some_list,
            }
        print(context)
        return context
class RedesView(TemplateView):
    template_name = 'redes.html'
    def get_context_data(self, *args, **kargs):
        context = super(RedesView, self).get_context_data(*args, **kargs)
        TweetsAmb = pickle.load(open('/home/juang/Documents/Python Scripts/Genesis/Data/TweetsAmb', "rb" ) )
        TA=[t[2] for t in TweetsAmb[0:15]]
        context = {"TA": TA
                }
        print(context)
        return context

    
    
#    def post(self, request, *args, **kwargs):
#        print(kwargs)
#        context = {}
#        return render(request, "articulos.html", context)
#    def put(self, request, *args, **kwargs):
#        print(kwargs)
#        context = {}
#        return render(request, "articulos.html", context)
