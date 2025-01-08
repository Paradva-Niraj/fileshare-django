from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register',views.register_view,name='register_view'),
    path('login/',views.login_view,name='login_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('logout/',views.logout_view, name='logout_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
