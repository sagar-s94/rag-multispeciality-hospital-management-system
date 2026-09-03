from django.contrib.auth.forms import UserCreationForm
from .models import register_data

class userRegisterForm(UserCreationForm):

    class Meta:
        model = register_data
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "profile_image",
            "role",
        ]