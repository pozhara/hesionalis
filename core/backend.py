from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


class EmailAuthenticationBackend(object): 
    @staticmethod
    def authenticate(request, email=None, password=None):
        try:
            user = User.objects.get(
                email=email
            )
            print(check_password(password, user.password))
        except User.DoesNotExist:
            return None

        if user and check_password(str(password), user.password):
            return user
        else:
            messages.error(request, 'Incorrect email or password')

        return None
