from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views
from ilan import views as il_view
from user import views as us_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', il_view.AnasayfaView.as_view(), name='anasayfa'),
    path('ilan/', include('ilan.urls', namespace='ilan')),
    path('user/', include('django.contrib.auth.urls')),
    path('register/', us_view.register, name='register'),
    path('dashboard/', us_view.dashboard, name='dashboard'),
    path('edit/', us_view.edit, name='edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)