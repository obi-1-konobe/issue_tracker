from django import forms
from webapp.models import Project, IssueStatus, IssueType, Milestone, Issue


class IssueTypeForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=50,
        label='Issue type'
    )


class IssueStatusForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=50,
        label='Issue status'
    )
    

class SearchForm(forms.Form):
    search = forms.CharField(
        required=True,
        max_length=50,
        label='Search'
    )


class IssueSearchForm(forms.Form):
    project = forms.ModelChoiceField(
        required=True,
        queryset=Project.objects.all()
    )

    status = forms.ModelChoiceField(
        required=False,
        queryset=IssueStatus.objects.all(),
    )

    type = forms.ModelChoiceField(
        required=False,
        queryset=IssueType.objects.all(),
    )

    description = forms.CharField(
        max_length=100,
        required=False,
        label='Description'
    )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['name', 'description']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'issue_type', 'performer', 'issue_status']