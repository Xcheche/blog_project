from django import forms

from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
        }
        
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Newsletter.objects.filter(email=email).exists():
                raise forms.ValidationError('You are already subscribed')
            return email
