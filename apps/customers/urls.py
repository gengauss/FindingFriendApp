from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name="home"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('edit/',views.edit_profile, name="edit_profile"),
    path('login/', LoginView.as_view(template_name="Login/index.html"), name='login'),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
