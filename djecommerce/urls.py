
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Lynn's Unique Collection"
admin.site.site_title = "Lynn's Unique Collection"


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('core.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


