from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

# Retrieve the user model (default or custom) used in the project
UserModel = get_user_model()

# Define a custom authentication backend that allows authentication using either username or email
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Attempt to retrieve the user by username or email (case-insensitive)
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # If the user does not exist, create a dummy user to avoid timing attacks
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            # If multiple users are returned, retrieve the first one ordered by ID
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        # Check if the provided password is correct and the user is allowed to authenticate
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
