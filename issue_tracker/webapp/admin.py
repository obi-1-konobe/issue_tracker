from django.contrib import admin
from webapp.models import Issue, IssueStatus, IssueType, Project, Milestone

admin.site.register(Issue)
admin.site.register(IssueStatus)
admin.site.register(IssueType)
admin.site.register(Project)
admin.site.register(Milestone)
