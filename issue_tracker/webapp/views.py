from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View

from webapp.models import Issue, IssueType, IssueStatus
from webapp.forms import IssueTypeForm, IssueStatusForm


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