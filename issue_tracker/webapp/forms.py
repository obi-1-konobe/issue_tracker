from django import forms
from webapp.models import Project


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
    # project = forms.ModelChoiceField(
    #     required=True,
    #     queryset=Project.objects.all()
    # )

    description = forms.CharField(
        max_length=100,
        required=False,
        label='Description'
    )