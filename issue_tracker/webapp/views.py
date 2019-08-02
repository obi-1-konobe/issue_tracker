from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, TemplateView, View, DetailView, FormView

from webapp.models import Issue, IssueType, IssueStatus, Project, Milestone
from webapp.forms import IssueTypeForm, IssueStatusForm, SearchForm, IssueSearchForm


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


class IssueTypesView(ListView):
    template_name = 'issue_types.html'
    context_object_name = 'issue_types'

    def get_queryset(self):
        return IssueType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = IssueTypeForm()
        context['form'] = form
        return context


class IssueTypeCreateView(View):
    def post(self, request, *args, **kwargs):
        form = IssueTypeForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            IssueType.objects.create(
                name=data['name'],
            )
            return redirect('issue_types')
        else:
            return render(request, 'issue_types', context={'form': form})


class IssueTypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        issue_type = get_object_or_404(IssueType, pk=kwargs['issue_type_pk'])
        form = IssueTypeForm(data={
            'name': issue_type.name
        })

        return render(request, 'update_issue_type.html', context={'form': form, 'issue_type': issue_type})

    def post(self, request, *args, **kwargs):
        form = IssueTypeForm(data=request.POST)
        issue_type = get_object_or_404(IssueType, pk=kwargs['issue_type_pk'])
        if form.is_valid():
            data = form.cleaned_data
            issue_type.name = data['name']
            issue_type.save()
            return redirect('issue_types')
        else:
            return render(request, 'update_issue_type.html', context={'form': form, 'issue_type': issue_type})


class IssueTypeDeleteView(View):

    def get(self, request, *args, **kwargs):
        issue_type = get_object_or_404(IssueType, pk=kwargs['issue_type_pk'])
        issue_type.delete()
        return redirect('issue_types')


class IssueStatusesView(ListView):
    template_name = 'issue_statuses.html'
    context_object_name = 'issue_statuses'

    def get_queryset(self):
        return IssueStatus.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = IssueStatusForm()
        context['form'] = form
        return context


class IssueStatusCreateView(View):
    def post(self, request, *args, **kwargs):
        form = IssueStatusForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            IssueStatus.objects.create(
                name=data['name'],
            )
            return redirect('issue_statuses')
        else:
            return render(request, 'issue_statuses', context={'form': form})


class IssueStatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        issue_status = get_object_or_404(IssueStatus, pk=kwargs['issue_status_pk'])
        form = IssueStatusForm(data={
            'name': issue_status.name
        })

        return render(request, 'update_issue_status.html', context={'form': form, 'issue_status': issue_status})

    def post(self, request, *args, **kwargs):
        form = IssueStatusForm(data=request.POST)
        issue_status = get_object_or_404(IssueStatus, pk=kwargs['issue_status_pk'])
        if form.is_valid():
            data = form.cleaned_data
            issue_status.name = data['name']
            issue_status.save()
            return redirect('issue_statuses')
        else:
            return render(request, 'update_issue_status.html', context={'form': form, 'issue_status': issue_status})


class IssueStatusDeleteView(View):

    def get(self, request, *args, **kwargs):
        issue_status = get_object_or_404(IssueStatus, pk=kwargs['issue_status_pk'])
        issue_status.delete()
        return redirect('issue_statuses')


class ProjectListView(ListView):
    model = Project
    paginate_orphans = 1
    paginate_by = 5
    template_name = 'projects/list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['milestone_list'] = self.object.milestones.all().order_by('-started_at')
        return context


class MilestoneDetailVIew(DetailView):
    model = Milestone
    template_name = 'milestones/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues_list'] = self.object.issues.all().order_by('-created_at')
        return context


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
        return reverse('issue_search_results') + '?' + urlencode(self.search_query)


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