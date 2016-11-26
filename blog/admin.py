#l'admin deve considerare anche la nostra applicazione dei post - importa i post#
from django.contrib import admin
from .models import Post 

admin.site.register(Post)