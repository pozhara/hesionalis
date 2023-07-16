from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DeleteView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from core.models import Artist, Design, Appointment
from .forms import RegisterForm, LoginForm, EditProfileForm, PasswordChangeForm, AppointmentForm

# Create your views here.

faqs = [
    {
        "question": "How do I book an appointment?",
        "answer": "Provide information about the booking process, such as whether appointments are made online, over the phone, or in person. Mention any specific requirements or steps involved in securing a tattoo appointment."
    },
    {
        "question": "Is there a minimum age requirement for getting a tattoo?",
        "answer": "Explain the legal age requirements for getting a tattoo in your location. If there are any additional policies or restrictions regarding age, such as parental consent for minors, include that information as well."
    },
    {
        "question": "How much does a tattoo cost?",
        "answer": "Address the question of pricing by explaining that tattoo costs vary depending on factors such as the size, design complexity, placement, and the artist's experience. Consider providing a general price range or mentioning that pricing is determined during a consultation."
    },
    {
        "question": "Do you require a deposit for appointments?",
        "answer": "Inform customers about your deposit policy, including whether a deposit is required to secure an appointment and any refund or rescheduling policies associated with deposits."
    },
    {
        "question": "How should I prepare for my tattoo appointment?",
        "answer": "Offer guidance on how clients should prepare themselves before their appointment, such as avoiding alcohol or blood-thinning medications, staying hydrated, and eating a good meal beforehand."
    },
    {
        "question": "What safety measures do you have in place?",
        "answer": "Highlight the importance of safety and cleanliness in your studio. Explain the measures you take to ensure a sterile environment, including the use of disposable needles, sterilization techniques, and adherence to health regulations."
    },
    {
        "question": "Can I bring my own design, or do you provide custom designs?",
        "answer": "Explain whether clients can bring their own tattoo design ideas or if you offer custom design services. Describe any consultation process involved in turning their ideas into a unique tattoo design."
    },
    {
        "question": "How long does the tattoo process take?",
        "answer": "Provide a general estimate of the time required for different tattoo sizes or design complexities. Emphasize that tattooing is a meticulous process and that the duration can vary depending on factors like the design, client comfort, and breaks."
    },
    {
        "question": "How do I take care of my tattoo after getting it done?",
        "answer": "Offer aftercare instructions to help clients properly care for their new tattoo. Include information on cleaning, moisturizing, avoiding direct sunlight, and any specific aftercare products you recommend."
    },
    {
        "question": "Can I see examples of your previous work?",
        "answer": "Direct clients to your portfolio, either on your website or social media platforms, where they can view examples of your artists' previous work. Highlight the versatility and quality of your artists' tattooing styles."
    }
]


class HomeView(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'index.html', context={"artists": artists})


class FAQView(View):

    def get(self, request):

        return render(request, 'faq.html', context={"faqs": faqs})


class ArtistView(ListView):
    model = Artist
    template_name = 'artists.html'
    context_object_name = 'artists'


class DesignsView(View):
    def get(self, request):
        designs = Design.objects.all()
        size = ['large', "medium", "small"]
        return render(request, 'styles.html', context={'size': size, "designs": designs})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect('home')


class EditProfileView(View):
    def get(self, request):
        user = request.user
        if not user:
            return redirect('login')
        profile = EditProfileForm(initial={
                                  'first_name': user.first_name, 'last_name': user.last_name})
        username = request.user.username
        context = {'profile': profile}
        return render(request, 'edit_profile.html', context)

    def post(self, request):
        user = request.user
        if not user:
            # Retrieve the user from the database
            return redirect('login')
        form = EditProfileForm(request.POST or None, instance=user)

        if form.is_valid():
            # Update the user data and save the changes
            user = request.user
            if request.method == 'POST':
                if form.is_valid():
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    form.save()
                    messages.success(request, "Your profile has been successfully updated!")
                    return redirect('home')
        else:
            messages.error(request, "Please provide valid information")
            return redirect('edit_profile')
        context = {'form': form}
        return render(request, 'edit_profile.html', context)


class PasswordChangeView(View):
    def get(self, request):
        user = request.user
        if not user:
            return redirect('login')
        change_password = PasswordChangeForm(user)
        context = {"change_password": change_password}
        return render(request, 'edit_password.html', context)

    def post(self, request):
        user = request.user
        if not user:
            # Retrieve the user from the database
            return redirect('login')
        change_password = PasswordChangeForm(request.user, request.POST)

        if change_password.is_valid():

            user = change_password.save()
            print(user.password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password has been successfully updated.')
            change_password.cleaned_data['old_password'] = None
            # Redirect to the same page after successful password change
            return redirect('home')
        else:
            messages.error(request, 'Please provide your old password and confirm the new one')

        context = {"change_password": change_password}
        return render(request, 'edit_password.html', context)


class CreateAppointmentView(LoginRequiredMixin, View):
    
    template_name = 'appointment_form.html'
    login_url = '/login/?next=/appointment/create/'

    def get(self, request, artist_id=None):
        form = AppointmentForm()
        if artist_id is not None:

            form.fields['artist'].initial = artist_id

        return render(request, 'appointment_form.html', {'form': form})

    def post(self, request, artist_id=None):

        form = AppointmentForm(request.POST)
        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Appointment was requested successfully!")
            return redirect('appointment')

        return render(request, 'appointment_form.html', {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to create an appointment.')
        return super().dispatch(request, *args, **kwargs)


class AppointmentView(LoginRequiredMixin, View):
    template_name = 'appointment.html'
    login_url = '/login/?next=/appointments/'
    context_object_name = 'appointments'

    def get(self, request):
        appointments = Appointment.objects.filter(user__email=request.user.email)
        return render(request, self.template_name, {'appointments': appointments})
