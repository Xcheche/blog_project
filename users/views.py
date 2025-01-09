import logging

from django.contrib import messages  # type: ignore

# type: ignore
from django.core.mail import send_mail  # type: ignore
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy  # type: ignore
from django.views import generic  # type: ignore

from config import settings

from .forms import SignUpForm
from .models import Profile

logger = logging.getLogger(__name__)

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        email = form.cleaned_data['email']
        logger.info(f"Sending email to: {email}")
        try:
            send_mail(
                subject='Welcome to Cheche\'s Blog!',
                message='Thank you for signing up.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )
            
            messages.success(self.request, f'Signup successful for {user},  Please check your email.')
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}")
            messages.error(self.request, "Signup successful, but email sending failed.")
        return super().form_valid(form)
    
def profile(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)