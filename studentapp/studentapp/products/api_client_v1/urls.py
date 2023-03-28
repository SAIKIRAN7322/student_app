from django.urls import path

from products.api_client_v1.views import productsClientPostingPDetailsView, productsClientPostingPwithImagesView, \
    productsClientGettingPWithImagesView, productsClientAddingPtouserproductsCartView

urlpatterns = [
    path("post_product_details/",productsClientPostingPDetailsView.as_view(),name="productsClientPostingPDetailsURL"),
    path("post_product_details_and_Images/",productsClientPostingPwithImagesView.as_view(),name = "productsClientPostingPwithImagesURL"),
    path("get_all_product_details_and_Images/", productsClientGettingPWithImagesView.as_view(),name = " productsClientGettingPWithImagesURL"),
    path("Addingtocart/",productsClientAddingPtouserproductsCartView.as_view(),name="productsClientAddingPtouserproductsCartURL")


]