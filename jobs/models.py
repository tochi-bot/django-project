from django.db import models
from django.contrib.auth.models import AbstractUser

# Define a custom user model extending the built-in AbstractUser
class user(AbstractUser):
    # Override the email field to enforce uniqueness
    email = models.EmailField(unique=True)

    # Boolean field to indicate if the user is a recruiter
    is_recruiters = models.BooleanField(default=False)
    
    # Boolean field to indicate if the user is an applicant
    is_applicant = models.BooleanField(default=False)

    # Boolean field to indicate if the user has a resume
    has_resume = models.BooleanField(default=False)

    # Boolean field to indicate if the user has a company
    has_company = models.BooleanField(default=False)



