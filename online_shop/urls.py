from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop_site.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('contact/', ContactViews.as_view(), name='contact'),
    path('about/', about, name='about')
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)