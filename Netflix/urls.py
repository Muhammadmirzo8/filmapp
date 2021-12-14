
from django.contrib import admin
from django.urls import path , include
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
from rest_framework.permissions import AllowAny

doc_view = get_schema_view(
     openapi.Info(
         title="Clone app of Netflix", 
         default_version = 'v1', 
         descrption = '(REST API) Clone of Netflix using Dajngo Rest Framework', 
         contact = openapi.Contact("Muhammadmirzo Toshpolatjonov <mtoshpulatjonov@gmail.com>")
     ), 
     public=True, 
     permission_classes=(AllowAny,)
)



urlpatterns = [
    path('admin/', admin.site.urls),  
    path("Netflix/", include("films.urls") ),  
    path("swaggerdoc/", doc_view.with_ui('swagger', cache_timeout=0), name="swagger_doc") , 
    path("redoc/", doc_view.with_ui('redoc', cache_timeout=0), name="redoc_doc")
    

]
