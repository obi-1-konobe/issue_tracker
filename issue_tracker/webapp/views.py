from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from webapp.models import Issue


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 1
    
    def get_queryset(self):
        return Issue.objects.all().order_by('-created_at')


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['issue_pk'])
        return context
