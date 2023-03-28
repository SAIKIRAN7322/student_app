from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,HTTP_200_OK
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import accountsUserCartProductsModel, accountsUserModel, accountsUserCartModel
from products.api_client_v1.serializers import PostingProductSerializer, PostingProductDetailsSerializer, \
    productsClientGettingPWithImagesSerializer, productsClientOwneridandProductidserializer
from products.models import productsPModel


# <editor-fold desc="Posting product details View">
class productsClientPostingPDetailsView(APIView):
    def post(self, request):
        serialize = PostingProductSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, HTTP_201_CREATED)
        else:
            return Response(serialize.errors, HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="Posting products with images View">
class productsClientPostingPwithImagesView(APIView):
    def post(self, request):
        serialize = PostingProductDetailsSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=HTTP_400_BAD_REQUEST)
# </editor-fold>
# <editor-fold desc="Getting all products along with images">
class productsClientGettingPWithImagesView(APIView,LimitOffsetPagination):
    def get(self,request):
        try:
            instance = productsPModel.objects.all()
            results = self.paginate_queryset(instance, request, view=self)
        except Exception as e:
            return Response("{message:Object not found}",status=status.HTTP_400_BAD_REQUEST)
        serializer = productsClientGettingPWithImagesSerializer(results,many=True)
        return  self.get_paginated_response(serializer.data)
# </editor-fold

# <editor-fold desc="Adding product to user cart">
class productsClientAddingPtouserproductsCartView(APIView):
    def post(self,request):
        serialize=productsClientOwneridandProductidserializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"message":"Successfully added to cart"},status=HTTP_200_OK)
        else:
            return Response(serialize.errors,status=HTTP_400_BAD_REQUEST)
# </editor-fold>




