from django.contrib import admin
from authentication.models import Avatar, User


# Register your models here.
admin.site.register(User)
admin.site.register(Avatar)