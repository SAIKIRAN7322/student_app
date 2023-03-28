from django.urls import path, include
urlpatterns = [
    path('api/client/v1/', include("studentdetails.api_client_v1.urls"))
]