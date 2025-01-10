import logging

from django.contrib import messages  # type: ignore
from django.contrib.auth.decorators import login_required

# type: ignore
from django.core.mail import send_mail  # type: ignore
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy  # type: ignore
from django.views import generic  # type: ignore

from config import settings

from .forms import ProfileUpdateForm, SignUpForm, UserUpdateForm
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
    
    
    
# @login_required 
# def profile(request):
#     profile = Profile.objects.all()
#     context = {
#         'profile': profile
#     }
#     return render(request, 'users/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)