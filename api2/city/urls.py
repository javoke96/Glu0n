from django.conf.urls import url
from .views import ListCityView

urlpatterns = [
    url('', ListCityView.as_view(), name="cities-all")
]
