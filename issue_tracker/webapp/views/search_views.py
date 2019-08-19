from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, FormView, ListView
from webapp.forms import SearchForm, IssueSearchForm
from webapp.models import Project, Issue


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, *args, **kwargs):
        form = SearchForm()
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        if query:
            search_project = Project.objects.filter(name__icontains=query)
            context['search_list'] = search_project

        context['form'] = form
        return context


class IssueSearchView(FormView):
    template_name = 'issue_search.html'
    form_class = IssueSearchForm
    search_query = {}

    def form_valid(self, form):
        self.search_query = form.cleaned_data.copy()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:issue_search_results') + '?' + urlencode(self.search_query)


class IssueSearchResultsView(ListView):
    template_name = 'issue_search_results.html'
    context_object_name = 'issues'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['query'] = urlencode({
            'description': self.request.GET.get('description'),
            'status': self.request.GET.get('status'),
        })
        return context

    def get_queryset(self):
        filter_kwargs = {
            'description__icontains': self.request.GET.get('description'),
            'issue_status__name__exact': self.request.GET.get('status'),
            'issue_type__name__exact': self.request.GET.get('type'),
            'milestone__project__name__exact': self.request.GET.get('project')
        }

        non_empty_kwargs = {}
        for key, value in filter_kwargs.items():
            if value != 'None' and value:
                non_empty_kwargs[key] = value
        if len(non_empty_kwargs) > 0:
            return Issue.objects.filter(**non_empty_kwargs).distinct()
        return Issue.objects.all()