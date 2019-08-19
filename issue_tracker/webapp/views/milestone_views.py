from django.shortcuts import redirect

from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import MilestoneForm
from webapp.models import Milestone, Project


class MilestoneDetailVIew(DetailView):
    model = Milestone
    template_name = 'milestones/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues_list'] = self.object.issues.all().order_by('-created_at')
        return context


class MilestoneCreateView(CreateView):
    template_name = 'milestones/create.html'
    model = Milestone
    form_class = MilestoneForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.get_project()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['project'] = self.get_project()
        return super().get_context_data(**kwargs)

    def get_project(self):
        return Project.objects.get(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})


class MilestoneUpdateView(UpdateView):
    model = Milestone
    template_name = 'milestones/update.html'
    form_class = MilestoneForm
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:milestone_detail', kwargs={'pk': self.object.pk})


class MilestoneDeleteView(DeleteView):
    model = Milestone
    template_name = 'milestones/delete.html'
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})