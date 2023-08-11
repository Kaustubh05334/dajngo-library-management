from django import forms
from .models import Book, Member,Lended

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['debt']


class LendForm(forms.ModelForm):
    class Meta:
        model = Lended
        exclude = ['returned']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(qty__gte=1)

class ReturnForm(forms.Form):
    lending = forms.ModelChoiceField(queryset=Lended.objects.filter(returned=False))
