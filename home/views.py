from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Language, Function
from .forms import FunctionForm


class HomeListView(ListView):
    template_name = 'home/home.html'

    def get_queryset(self):
        return Language.objects.all()


class FunctionListView(ListView):
    template_name = 'home/list.html'

    def get_queryset(self):
        return Function.objects.filter(language = self.kwargs['pk'])


class FunctionDetailView(DetailView):
    model = Function
    template_name = 'home/functiondetails.html'


def add_function(request):
    languages = Language.objects.all()
    form = FunctionForm()
    return render(request, 'home/addfunctionform.html', {'languages': languages, 'form': form})


def create_function(request):
    if request.method == 'POST':
        form = FunctionForm(request.POST)

        if form.is_valid():
            language = Language.objects.get(pk = form.cleaned_data['language_id'])
            newFunction = Function(title = form.cleaned_data['function_title'], body = form.cleaned_data['function_body'],
                                   language = language, date = timezone.now())
            newFunction.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        return add_function(request)
    
    
