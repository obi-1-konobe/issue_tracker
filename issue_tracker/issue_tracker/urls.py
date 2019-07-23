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
from django.contrib import admin
from django.urls import path

from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('issue/<int:issue_pk>', views.IssueView.as_view(), name='issue'),
    path('issue_types', views.IssueTypesView.as_view(), name='issue_types'),
    path('issue_types/create', views.IssueTypeCreateView.as_view(), name='create_issue_type'),
    path('issue_types/<int:issue_type_pk>', views.IssueTypeUpdateView.as_view(), name='update_issue_type'),
]
