from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    
    path('events/', include('events.urls')),
    path('opera/', include('opera.urls')),
<<<<<<< HEAD
=======
    path('tickets/', include('tickets.urls')),

>>>>>>> 6410340c128350e2f5d2d9a06383fc927e6a8814
    

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

