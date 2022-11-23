from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include

from manager.views import (
    index, rules, characters, contact
)

urlpatterns = [
    path('', index, name="index"),
    path('rules/', rules, name="rules"),
    path('characters/', characters, name="characters"),
    path('contact/', contact, name="contact"),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

