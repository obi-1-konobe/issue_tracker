from django import forms


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
