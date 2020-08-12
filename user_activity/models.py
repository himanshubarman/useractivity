from django.db import models
import random
import string
from timezone_field import TimeZoneField
import uuid

# Create your models here.
def generate_user_id():
	length = 9
	charset = string.ascii_letters + string.digits
	result = ''.join(random.choice(charset) for i in range(length))
	return result.upper()
    
# User Model for details such as id, real_name, tz as in Time field in different zone
class User(models.Model):
	id = models.CharField(max_length=6, primary_key=True, default=generate_user_id)
	real_name = models.CharField(max_length=255)
	tz = models.CharField(max_length=50)

# User Activity Model defining foreign key relationship with User Model
class UserActivity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()



