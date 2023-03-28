import string

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from accounts.api_client_v1.serializers import accountsClientCustomerSerializer, accountsClientGetUserSerializer, \
    accountsClientLoginOtpSerializer, accountsClientotprequestSerializer, accountsClientMailOTPSerializer
from accounts.models import accountsUserProfileModel, accountsUserModel, accountsUserLoginOTPModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# <editor-fold desc="Creating a new user">
class accountsClientCreateUserView(APIView):
    def post(self,request):
        serializer = accountsClientCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_404_NOT_FOUND)
# </editor-fold>

# <editor-fold desc="Generation of otp for email">
class accountsLoginGeneratingOtpView(APIView):
    def post(self,request):
        serialize = accountsClientLoginOtpSerializer(data = request.data)
        if serialize.is_valid():
            print('Hello', serialize.data)
            if(accountsUserModel.objects.filter(email=serialize.data["email"])):
                object = accountsUserModel.objects.get(email=serialize.data["email"])
                chars = string.digits
                m = "".join(random.choice(chars) for _ in range(4))
                Instance=accountsUserLoginOTPModel.objects.create(owner=object,otp=m)
                send_mail("OTP VERIFICATION MAIL", "Your Login otp is {otp} ".format(otp=m),"djasunka113@gmail.com",[serialize.data["email"]])
                return Response("{message:OTP has been sent to your mail}",status=HTTP_200_OK)
            else:
                return Response("{message: User doesn't exist please do signup}",status=HTTP_404_NOT_FOUND)
        else:
            return (serialize.errors,HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="Login">
class accountsLoginSystemView(APIView):
    def post(self,request):
        serialize=accountsClientMailOTPSerializer(data=request.data)
        if serialize.is_valid():
            object = accountsUserModel.objects.get(email=serialize.data['email'])
            m = accountsUserLoginOTPModel.objects.values("otp").filter(owner=object).order_by("-id").first()
            if(m["otp"]==serialize.data["otp"]):
                user = accountsUserLoginOTPModel.objects.get(owner=object, otp=serialize.data["otp"])
                print("HELLOO",user)
                refresh = RefreshToken.for_user(object)
                return Response(
                        {
                            "refresh":str(refresh),
                            "access":str(refresh.access_token)
                        }
                        )
            else:
                return Response("{message:Your Login otp had expired,please do enter latest otp }")
        else:
            return Response(serialize.errors)
# </editor-fold>


# <editor-fold desc="Getting all users">
class accountsClientGetUsersView(APIView,LimitOffsetPagination):
    def get(self,request):
        try:
            queryset = accountsUserModel.objects.all()
            results = self.paginate_queryset(queryset, request, view=self)
        except:
            return Response("{Message:Objects Not Found}",status=HTTP_404_NOT_FOUND)
        serializer = accountsClientGetUserSerializer(results,many=True)
        return self.get_paginated_response(serializer.data)
# </editor-fold>
