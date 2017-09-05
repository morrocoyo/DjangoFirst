from django.shortcuts import render
from django.views.generic.edit import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from .forms import ItemForm
from .models import Item


class HomeView(View):
    def get(self, request, *arg, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'home.html', {})
        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True).order_by('-updated')[:4]
        return render(request, 'menus/home-feed.html', {'object_list':qs})

# Create your views here.
class ItemListView(LoginRequiredMixin,ListView):
    template_name = 'menus/item_list.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(LoginRequiredMixin,DetailView):
    template_name = 'menus/item_detail.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ItemForm
    login_url = '/login/'
    # success_url = '/create'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Crear Item'
        return context

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    login_url = '/login/'
    template_name = 'menus/detail-update.html'

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Actualizar Item'
        return context

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
