from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

USER_TYPE = (
    ('Editor','Editor'),
    ('Artist','Artist'),
    ('Admin','Admin'),
)

TYPE = (
    ('Grupo','Grupo'),
    ('Solo','Solo')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices = USER_TYPE , blank=True,null=True)
    mobile_no = models.CharField(max_length=20, null=True ,unique=True, blank=True,validators=[
      RegexValidator(
        regex=r'^[0-9]+$',
        message="Phone number must be entered in the format '123456789' "
      ),
    ],)
    # user_image = models.ImageField(upload_to ='images/' , height_field=None, width_field=None, max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, choices = TYPE , blank=True,null=True)
    file_no = models.CharField(max_length=50, default="", blank=True,null=True)
    bank_name = models.CharField(max_length=200, default="", blank=True,null=True)
    account_holder_nm = models.CharField(max_length=200, default="", blank=True,null=True)
    IBAN = models.CharField(max_length=200, default="", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return str(self.mobile_no)



class Kineto_Kisom(models.Model):
    ARTIST_NAME = models.CharField(default="",max_length=100,blank=True, null=True)
    CONTENT_NAME = models.CharField(default="",max_length=100,blank=True, null=True)
    NET_ROYALTY_TOTAL = models.FloatField(default=0.0, null=True,blank=True)

    def __str__(self):
        return str(self.ARTIST_NAME)

class RBT_MAR(models.Model):
    ARTIST_NAME = models.CharField(default="",max_length=100,blank=True, null=True)
    CONTENT_NAME = models.CharField(default="",max_length=100,blank=True, null=True)
    REV_X_2 = models.FloatField(default=0.0, null=True,blank=True)

    def __str__(self):
        return str(self.ARTIST_NAME)

class AltaFonte_MAR(models.Model):
    SERVICE_ID = models.CharField(default="",max_length=100,blank=True, null=True)
    COUNTRY = models.CharField(default="",max_length=200,blank=True, null=True)
    ARTIST_DISPLAY = models.CharField(default="",max_length=500,blank=True, null=True)
    TRACK_TITLE = models.CharField(default="",max_length=300,blank=True, null=True)
    NET = models.FloatField(default=0.0, null=True,blank=True)

    def __str__(self):
        return str(self.ARTIST_DISPLAY)

