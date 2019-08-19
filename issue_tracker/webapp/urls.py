from django.urls import path

from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', issue_views.IndexView.as_view(), name='index'),
    path('projects', project_views.ProjectListView.as_view(), name='project_list'),
    path('search', search_views.SearchView.as_view(), name='search'),
    path('issue/<int:issue_pk>', issue_views.IssueView.as_view(), name='issue'),
    path('projects/<int:pk>', project_views.ProjectDetailView.as_view(), name='project_detail'),
    path('milestones/<int:pk>', milestone_views.MilestoneDetailVIew.as_view(), name='milestone_detail'),
    path('issue_types', issue_views.IssueTypesView.as_view(), name='issue_types'),
    path('issue_statuses', issue_views.IssueStatusesView.as_view(), name='issue_statuses'),
    path('issue_types/create', issue_views.IssueTypeCreateView.as_view(), name='create_issue_type'),
    path('issue_statuses/create', issue_views.IssueStatusCreateView.as_view(), name='create_issue_status'),
    path('issue_types/<int:issue_type_pk>/update', issue_views.IssueTypeUpdateView.as_view(), name='update_issue_type'),
    path('issue_statuses/<int:issue_status_pk>/update', issue_views.IssueStatusUpdateView.as_view(), name='update_issue_status'),
    path('issue_types/<int:issue_type_pk>/delete', issue_views.IssueTypeDeleteView.as_view(), name='delete_issue_type'),
    path('issue_statuses/<int:issue_status_pk>/delete', issue_views.IssueStatusDeleteView.as_view(), name='delete_issue_status'),
    path('issue/search', search_views.IssueSearchView.as_view(), name='issue_search'),
    path('issue/search-results', search_views.IssueSearchResultsView.as_view(), name='issue_search_results'),
    path('create_projects', project_views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/create_milestone', milestone_views.MilestoneCreateView.as_view(), name='create_milestone'),
    path('milestones/<int:pk>/create_issue', issue_views.IssueCreateView.as_view(), name='create_issue'),
    path('projects/<int:pk>/update', project_views.ProjectUpdateView.as_view(), name='update_project'),
    path('milestones/<int:pk>/update', milestone_views.MilestoneUpdateView.as_view(), name='update_milestone'),
    path('issue/<int:issue_pk>/update', issue_views.IssueUpdateView.as_view(), name='update_issue'),
    path('projects/<int:pk>/delete', project_views.ProjectDeleteView.as_view(), name='delete_project'),
    path('milestones/<int:pk>/delete', milestone_views.MilestoneDeleteView.as_view(), name='delete_milestone'),
    path('issue/<int:issue_pk>/delete', issue_views.IssueDeleteView.as_view(), name='delete_issue'),
]