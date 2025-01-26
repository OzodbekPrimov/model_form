from django.urls import path
from .views import main, person_list
urlpatterns = [
    path('', main, name='main'),
    path('person-list/', person_list, name='person_list' ),
]

