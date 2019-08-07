from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'row':5, 'placeholder': "Whta's on your mind?"}
        ),
        max_length="400",
        help_text = "The max length is 4000"
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

