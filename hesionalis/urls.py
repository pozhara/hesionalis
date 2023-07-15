"""hesionalis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.forms import LoginForm
from core.views import HomeView, ArtistView, DesignsView, FAQView, RegisterView, CustomLoginView, LogoutView, EditProfileView, PasswordChangeView, CreateAppointmentView, AppointmentView

urlpatterns = [
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path("edit_password", PasswordChangeView.as_view(), name="edit_password"),
    path('', HomeView.as_view(), name='home'),
    path('artists/', ArtistView.as_view(), name='artists'),
    path('styles/', DesignsView.as_view(), name='styles'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_appointment/', CreateAppointmentView.as_view(), name='create_appointment'),
    path('appointment/', AppointmentView.as_view(), name='appointment'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
