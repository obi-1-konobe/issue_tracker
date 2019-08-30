from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from webapp.forms import IssueTypeForm, IssueStatusForm, IssueForm
from webapp.models import Issue, IssueType, IssueStatus, Milestone


class IndexView(ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issues'
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        return Issue.objects.all().order_by('-created_at')


class IssueView(TemplateView):
    template_name = 'issues/issue.html'

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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueTypeDeleteView(View):

    def get(self, request, *args, **kwargs):
        issue_type = get_object_or_404(IssueType, pk=kwargs['issue_type_pk'])
        issue_type.delete()
        return redirect('issue_types')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueStatusDeleteView(View):

    def get(self, request, *args, **kwargs):
        issue_status = get_object_or_404(IssueStatus, pk=kwargs['issue_status_pk'])
        issue_status.delete()
        return redirect('issue_statuses')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueCreateView(CreateView):
    template_name = 'issues/issue_create.html'
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        form.instance.milestone = self.get_milestone()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['milestone'] = self.get_milestone()
        return super().get_context_data(**kwargs)

    def get_milestone(self):
        return Milestone.objects.get(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('webapp:milestone_detail', kwargs={'pk': self.object.milestone.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issues/update.html'
    form_class = IssueForm
    pk_url_kwarg = 'issue_pk'

    def get_success_url(self):
        return reverse('webapp:issue', kwargs={'issue_pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        issue = Issue.objects.get(pk=self.kwargs.get('issue_pk'))
        if issue.author != self.request.user or not self.request.user.is_superuser:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    pk_url_kwarg = 'issue_pk'

    def get_success_url(self):
        return reverse('webapp:milestone_detail', kwargs={'pk': self.object.milestone.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        issue = Issue.objects.get(pk=self.kwargs.get('issue_pk'))
        if issue.author != self.request.user or not self.request.user.is_superuser:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)