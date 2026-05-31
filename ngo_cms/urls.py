from django.contrib import admin
from django.urls import path

from home.views import home, about, projects, media

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('media/', media, name='media'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)