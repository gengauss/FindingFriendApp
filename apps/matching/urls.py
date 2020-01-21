from django.urls import path

from . import views,matching_test

urlpatterns = [
    # path('', views.retrieve_user, name='index'),
    path(r'match/',views.matching,name='match'),
    # path('thankyou/', views.thankyou, name='thanks'),
    path(r'add/<int:matched_id>/',views.add_friend,name='add_friend'),
    path(r'chat/<int:matched_id>/',views.add_channel,name='add_channel'),
]
