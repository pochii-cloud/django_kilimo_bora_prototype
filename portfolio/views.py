from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from djangoProject9.forms import QueryForm
from portfolio.models import Query


class BaseView(TemplateView):
    template_name = 'base.html'


class QueryView(FormView):
    form_class = QueryForm
    template_name = 'query.html'
    success_url = reverse_lazy('SuccessMessage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class QueryListView(TemplateView):
    template_name = 'feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = Query.objects.all()
        return context


class ResponseView(TemplateView):
    template_name = 'response.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = Query.objects.get(pk=self.kwargs.get('pk'))
        return context


class SuccessMessage(View):
    def get(self, request, **kwargs):
        messages.info(request, 'question received check response after 12 hours')
        return render(request, 'successmessage.html')
