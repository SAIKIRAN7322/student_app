from django.urls import path,include
urlpatterns = [
    path("api/client/v1/",include("products.api_client_v1.urls"))
]