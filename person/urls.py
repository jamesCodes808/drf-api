from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('<int:pk>', PersonDetail.as_view(), name='person_detail')
]