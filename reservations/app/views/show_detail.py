from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView

from app.models import Show

"""# Show DetailView Class definition
class DetailShow(DetailView):
    model = Show
    template_name = 'app/shows/show_detail.html'
    context_object_name = 'show'

    def get_context_data(self, **kwargs):
        context = super(DetailShow, self).get_context_data(**kwargs)
        return context"""