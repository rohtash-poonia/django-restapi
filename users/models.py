from django.db import models


class User(models.Model):
	# Store a unique username for each user record.
	username = models.CharField(max_length=150, unique=True)
	# Store an optional email address.
	email = models.EmailField(blank=True)
	# Store the user's first name.
	first_name = models.CharField(max_length=150, blank=True)
	# Store the user's last name.
	last_name = models.CharField(max_length=150, blank=True)
	# Store an optional phone/mobile number.
	mobile_number = models.CharField(max_length=20, blank=True)
	# Upload profile images into the media/profile_pictures/ folder.
	profile_picture = models.ImageField(
		upload_to="profile_pictures/",
		blank=True,
		null=True,
	)

	# Show the username in admin pages and the Django shell.
	def __str__(self):
		return self.username
