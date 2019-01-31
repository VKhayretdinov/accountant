from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.post_list, name='post_list'),
                  path('<int:pk>/', views.post_detail, name='post_detail'),
                  path('post/new/', views.post_new, name='post_new'),
                  path('<int:pk>/post/add_like', views.post_add_like, name='post_add_like'),
                  path('INN/', views.inn, name='INN'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
