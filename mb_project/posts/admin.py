from django.contrib import admin

# Register your models here.
# For registering model you have to ecplicitly import the model and register.
from .models import Post
admin.site.register(Post)
