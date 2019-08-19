"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import webapp.views.issue_views
import webapp.views.milestone_views
import webapp.views.project_views
import webapp.views.search_views
from django.contrib import admin
from django.urls import path

from webapp import views
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp.views.issue_views.IndexView.as_view(), name='index'),
    path('projects', webapp.views.project_views.ProjectListView.as_view(), name='project_list'),
    path('search', webapp.views.search_views.SearchView.as_view(), name='search'),
    path('issue/<int:issue_pk>', webapp.views.issue_views.IssueView.as_view(), name='issue'),
    path('projects/<int:pk>', webapp.views.project_views.ProjectDetailView.as_view(), name='project_detail'),
    path('milestones/<int:pk>', webapp.views.milestone_views.MilestoneDetailVIew.as_view(), name='milestone_detail'),
    path('issue_types', webapp.views.issue_views.IssueTypesView.as_view(), name='issue_types'),
    path('issue_statuses', webapp.views.issue_views.IssueStatusesView.as_view(), name='issue_statuses'),
    path('issue_types/create', webapp.views.issue_views.IssueTypeCreateView.as_view(), name='create_issue_type'),
    path('issue_statuses/create', webapp.views.issue_views.IssueStatusCreateView.as_view(), name='create_issue_status'),
    path('issue_types/<int:issue_type_pk>/update', webapp.views.issue_views.IssueTypeUpdateView.as_view(), name='update_issue_type'),
    path('issue_statuses/<int:issue_status_pk>/update', webapp.views.issue_views.IssueStatusUpdateView.as_view(), name='update_issue_status'),
    path('issue_types/<int:issue_type_pk>/delete', webapp.views.issue_views.IssueTypeDeleteView.as_view(), name='delete_issue_type'),
    path('issue_statuses/<int:issue_status_pk>/delete', webapp.views.issue_views.IssueStatusDeleteView.as_view(), name='delete_issue_status'),
    path('issue/search', webapp.views.search_views.IssueSearchView.as_view(), name='issue_search'),
    path('issue/search-results', webapp.views.search_views.IssueSearchResultsView.as_view(), name='issue_search_results'),
    path('create_projects', webapp.views.project_views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/create_milestone', webapp.views.milestone_views.MilestoneCreateView.as_view(), name='create_milestone'),
    path('milestones/<int:pk>/create_issue', webapp.views.issue_views.IssueCreateView.as_view(), name='create_issue'),
    path('projects/<int:pk>/update', webapp.views.project_views.ProjectUpdateView.as_view(), name='update_project'),
    path('milestones/<int:pk>/update', webapp.views.milestone_views.MilestoneUpdateView.as_view(), name='update_milestone'),
    path('issue/<int:issue_pk>/update', webapp.views.issue_views.IssueUpdateView.as_view(), name='update_issue'),
    path('projects/<int:pk>/delete', webapp.views.project_views.ProjectDeleteView.as_view(), name='delete_project'),
    path('milestones/<int:pk>/delete', webapp.views.milestone_views.MilestoneDeleteView.as_view(), name='delete_milestone'),
    path('issue/<int:issue_pk>/delete', webapp.views.issue_views.IssueDeleteView.as_view(), name='delete_issue'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),

]
