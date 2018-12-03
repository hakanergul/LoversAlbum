from django.urls import path
from ilan import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'ilan'

urlpatterns = [
    path('ekle/', views.IlanEkleView.as_view(), name="ilan_ekle"),
    path('<int:pk>', views.ilan_detail, name="ilan_goster"),
    path('listele/', views.IlanListView.as_view(), name="ilan_listele"),
    path('<int:pk>/edit', views.IlanUpdateView.as_view(), name='ilan_update'),
    path('<int:pk>/delete', views.IlanDeleteView.as_view(), name='ilan_delete'),
    path('<int:pk>/mutlulukdile', views.mutluluk_dile, name='mutluluk_dile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)