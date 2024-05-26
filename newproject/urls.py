from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("commons/", include('commons.urls')),
    path("crud/", include('crud.urls')),
    path("accounts/",include("accounts.urls")),
    path("quiz/",include("quiz.urls")),
    path('',include("myapp.urls")),
    path('classbased/',include("classbased.urls", namespace="classbased")),
    path('api/',include("api.urls", namespace="api")),
        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)