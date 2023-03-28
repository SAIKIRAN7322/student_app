from rest_framework import serializers

from accounts.models import accountsUserModel, accountsUserCartProductsModel, accountsUserCartModel
from products.models import productsPModel,productsPImageModel


# <editor-fold desc="PostingProductSerializer">
class PostingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productsPModel
        fields = ["title","description"]
# </editor-fold>


# <editor-fold desc="ImageSerializer">
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productsPImageModel
        fields = "__all__"
# </editor-fold>

# <editor-fold desc="PostingProductDetailsSerializer">
class PostingProductDetailsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=300,required=True)
    images = serializers.ListField(child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False))
    price = serializers.IntegerField(default=0)
    def create(self, validated_data):
        object = productsPModel.objects.create(title=validated_data["title"],description=validated_data['description'],price=validated_data["price"])
        for image in validated_data["images"]:
            try:
                productsPImageModel.objects.create(product = object,image = image)
            except Exception as e:
                object.delete()
                return serializers.ValidationError(f"image object not created because {e} ")
        return validated_data
    class Meta:
        fields = "__all__"
# </editor-fold>

# <editor-fold desc="productsClientGettingPWithImagesSerializer">
class productsClientGettingPWithImagesSerializer(serializers.ModelSerializer):
    Images = serializers.SerializerMethodField(read_only=True)
    def get_Images(self,obj):
        try:
            images = productsPImageModel.objects.values("image").filter(product = obj)
        except:
            return "{message:images not found}"
        return images
    class Meta:
        model = productsPModel
        fields = "__all__"
# </editor-fold>


# <editor-fold desc="productsClientOwneridandProductidserializer">
class productsClientOwneridandProductidserializer(serializers.Serializer):
    productid = serializers.IntegerField()
    ownerid = serializers.IntegerField()
    class Meta:
        fields = "__all__"


    def validate(self,data):
        ownerid = data["ownerid"]
        productid = data["productid"]
        if accountsUserModel.objects.filter(id=ownerid).exists():
            if productsPModel.objects.filter(id=productid).exists():
                if accountsUserCartProductsModel.objects.filter(owner_id=ownerid,product_id=productid).exists():
                    status = accountsUserCartProductsModel.objects.filter(owner_id=ownerid,product_id=productid)
                    print("Helloo",status["status"])




    def create(self,validated_data):
        return ""






# </editor-fold>



# <editor-fold desc="Practiced code">
# owner = data["ownerid"]
#
#         if accountsUserModel.objects.filter(id=data["ownerid"]).exists():
#             if productsPModel.objects.filter(id=data["productid"]).exists():
#                 if accountsUserCartProductsModel.objects.filter(owner_id=data["ownerid"],product_id=data['productid']).exists():
#                     status = accountsUserCartProductsModel.objects.values("status").get(owner_id=data["ownerid"], product_id=data['productid'])
#                     if status["status"] == "Pending":
#                         raise serializers.ValidationError("{message:The Product is already in the cart}")
#             else:
#                 raise serializers.ValidationError("{message:Either Product id doesn't exist}")
#         else:
#             raise serializers.ValidationError("{message:Either Owner id doesn't exist}")
#         return data






# if (accountsUserCartProductsModel.objects.filter(owner_id=validated_data["ownerid"],
#                                                  product_id=validated_data['productid']).exists()):
#     status = accountsUserCartProductsModel.objects.values("status").get(owner_id=validated_data["ownerid"],
#                                                                         product_id=validated_data['productid'])
#     if status["status"] == "Completed":
#         newusercartproductsobject = accountsUserCartProductsModel.objects.filter(owner_id=validated_data["ownerid"],
#                                                                                  product_id=validated_data[
#                                                                                      'productid']).update(
#             status="Pending")
#         print("HELLOOO", newusercartproductsobject)
#         if (accountsUserCartModel.objects.filter(owner_id=validated_data["ownerid"])):
#             productsadding = accountsUserCartModel.objects.filter(owner_id=validated_data["ownerid"]).update(
#                 products=newusercartproductsobject)
#         else:
#             usercartobject = accountsUserCartModel.objects.create(owner_id=validated_data["ownerid"])
#             usercartobject.products.add(newusercartproductsobject)
#             usercartobject.products.save()
#
# else:
#     newcartproductobject = accountsUserCartProductsModel.objects.create(owner_id=validated_data["ownerid"],
#                                                                         product=validated_data['productid'])
#     print("HIIIIIII I AM CARTPRODUCTS OBJECT", newcartproductobject)
#     if (accountsUserCartModel.objects.filter(owner_id=validated_data["ownerid"])):
#         productsadding = accountsUserCartModel.objects.filter(owner_id=validated_data["ownerid"]).update(
#             products=newcartproductobject)
#     else:
#         usercartobject = accountsUserCartModel.objects.create(owner_id=validated_data["ownerid"])
#         usercartobject.products.add(newcartproductobject)
#         usercartobject.products.save()
# return validated_data
# </editor-fold>