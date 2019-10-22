from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"hello", views.Hellotestmodel),
    url(r"contact/save", views.SaveContact),
]
