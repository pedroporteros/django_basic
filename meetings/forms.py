from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(required=True, label='Your name', max_length=100)
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':10, 'cols':80}))
    
    def log_data(self):
        print(self.cleaned_data.get('name'))
        print(self.cleaned_data.get('comment'))