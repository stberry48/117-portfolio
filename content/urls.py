from django.urls import path
from .views import projects_list, experience

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', projects_list, name='projects_list'),
    path('experience', experience, name='experience'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)