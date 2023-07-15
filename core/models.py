from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

GENDER = [
    ('Male', "Male"),
    ("Female", "Female"),
    ("Nonbinary", "Nonbinary"),
    ("Other", "Other")
]

TATTOO_SIZE = [
    ('S', 'Small'),
    ("M", "Medium"),
    ("L", "Large"),
    ('XL', "Extra-large")
]

TATTOO_LOCATION = [
    ("Ear", "Ear"),
    ("Neck", "Neck"),
    ("Shoudler", "Shoulder"),
    ("Bicep", "Bicep"),
    ("Forearm", "Forearm"),
    ("Arm", "Arm"),
    ("Chest", "Chest"),
    ("Sternum", "Sternum"),
    ("Stomach", "Stomach"),
    ("Hip", "Hip"),
    ("Thigh", "Thigh"),
    ("Knee", "Knee"),
    ("Calf", "Calf"),
    ("Shin", "Shin"),
    ("Ankle", "Ankle"),
    ("Foot", "Foot"),
]

APPOINTMENT_STATUS = [
    (0, "Pending"),
    (1, "Accepted"),
    (2, "Rejected"),
]

TATTOO_CATEGORY = [
    ("Neo Traditional", "Neo Traditional"),
    ("Fine Line", "Fine Line"),
    ("Tribal", "Tribal"),
    ("Watercolor", "Watercolor"),
    ("Blackwork", "Blackwork"),
    ("Realism", "Realism"),
    ("Japanese", "Japanese"),
    ("Patchwork", "Patchwork"),
    ("Ignorant", "Ignorant"),
    ("Portrait", "Portrait"),
    ("Animal", "Animal"),
    ("Floral", "Floral")
]


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200, null=True)
    skills = models.CharField(max_length=30, choices=TATTOO_CATEGORY, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    appointment_at = models.DateTimeField()
    tattoo_location = models.CharField(max_length=30, choices=TATTOO_LOCATION, null=True, blank=True)
    tattoo_size = models.CharField(max_length=3, choices=TATTOO_SIZE)
    tattoo_category = models.CharField(max_length=30, choices=TATTOO_CATEGORY, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="website_user")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name="appointment_artist")
    comment = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=APPOINTMENT_STATUS, default=0)

    class Meta:
        ordering = ['-created_on', 'artist']

    def __str__(self):
        return f"{self.user}"


class Design(models.Model):
    image = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, choices=TATTOO_CATEGORY)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name="design_artist")

    def __str__(self):
        return f"{self.category}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
