from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    paginate_orphans = 1
    paginate_by = 10
    template_name = 'projects/list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['milestone_list'] = self.object.milestones.all().order_by('-started_at')
        return context


class ProjectCreateView(CreateView):
    template_name = 'projects/create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})