from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import TuitCreateForm,TuitLocationCreateForm
from .models import TuitLocation


# Create your views here.
# function based view 


class TuitListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return TuitLocation.objects.filter(owner = self.request.user)

class TuitDetailView(DetailView):
    def get_queryset(self):
        return TuitLocation.objects.filter(owner = self.request.user) #in the future we can filter by user
    
class TuitCreateView(LoginRequiredMixin,CreateView):
    form_class=TuitLocationCreateForm
    login_url = '/login/'
    template_name   = 'form.html'
#    success_url='/tuits/'
    
    def form_valid(self, form):
            instance=form.save(commit=False)
            instance.owner=self.request.user
            return super(TuitCreateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TuitCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Agregue un Tuit'
        return context
    
class TuitUpdateView(LoginRequiredMixin,UpdateView):
    form_class=TuitLocationCreateForm
    login_url = '/login/'
    template_name   = 'tuits/detail-update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TuitUpdateView, self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Actualice {name}'
        return context

    def get_queryset(self):
        return TuitLocation.objects.filter(owner = self.request.user)


 
    
    
    

