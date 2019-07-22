from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Issue


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 1
    
    def get_queryset(self):
        return Issue.objects.all().order_by('-created_at')
    
