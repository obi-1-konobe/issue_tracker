from django.urls import reverse
from django.views.generic import DetailView, CreateView
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

    def form_valid(self, form):
        form.instance.project = self.get_project()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['project'] = self.get_project()
        return super().get_context_data(**kwargs)

    def get_project(self):
        return Project.objects.get(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})