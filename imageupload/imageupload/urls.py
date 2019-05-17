
from django.contrib import admin 
from django.urls import url ,include
from django.conf import settings 
from django.conf.urls.static import static 
from gallary import views
  
urlpatterns =[
    url(r'^admin/',admin.site.urls),
    url(r'^gallary/', include('gallary.urls', namespace='gallary')),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 