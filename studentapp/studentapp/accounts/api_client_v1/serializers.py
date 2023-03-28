import datetime

from rest_framework import serializers, exceptions
import re
from accounts.models import accountsUserModel


# <editor-fold desc="accountsClientCustomerSerializer">
class accountsClientCustomerSerializer(serializers.Serializer):
    phonenumber = serializers.IntegerField()
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    image = serializers.ImageField()
    class Meta:
        fields = "all"


    def validate(self,data):
        print("HELLLOOO",data)
        phone_number = str(data["phonenumber"])
        r = re.fullmatch('[6-9][0-9]{9}',phone_number)
        if r==None:
            raise serializers.ValidationError("{message:Phone number is not valid}")
        # date = datetime.datetime.strptime(data["dob"], '%Y-%m-%d').date()
        # print(date)
        k=datetime.datetime.now().date()-data["dob"]
        print(k.days/365)
        if((k.days/365)<=18):
            raise serializers.ValidationError("{message:user age is less than 18 not allowed}")
        """
                have to create user, user profile and user cart
        """
        if (accountsUserModel.objects.filter(email=data['email'])):
            raise exceptions.ValidationError("{message:User with email already exist try other}")
        if (accountsUserModel.objects.filter(phonenumber=data['phonenumber'])):
            raise exceptions.ValidationError("{message:User with phonenumber already exist try other}")
        else:
            return data

    def create(self, validated_data):
        """
        have to create user, user profile and user cart
        """
        from accounts.models import accountsUserProfileModel
        object=accountsUserModel.objects.create(phonenumber=validated_data["phonenumber"],email=validated_data["email"])
        try:
            instance = accountsUserProfileModel.objects.create(owner=object,name=validated_data["name"],dob = validated_data["dob"],image=validated_data['image'])
        except Exception as e:
            object.delete()
            raise serializers.ValidationError(f"userprofile not created because{e}")
        return validated_data
# </editor-fold>

# <editor-fold desc="accountsClientGetUserProfilesSerializer">
class accountsClientGetUserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        from accounts.models import accountsUserProfileModel
        model = accountsUserProfileModel
        fields = "__all__"
# </editor-fold>

# <editor-fold desc="accountsClientGetUserSerializer">
class accountsClientGetUserSerializer(serializers.ModelSerializer):
    Profile = accountsClientGetUserProfilesSerializer(source="accountsUserProfile_owner",read_only=True)
    class Meta:
        model = accountsUserModel
        fields = ["Profile","phonenumber","email"]
# </editor-fold>


# <editor-fold desc="accountsClientLoginOtpSerializern">
class accountsClientLoginOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    class Meta:
        fields = "__all__"
# </editor-fold>

from accounts.models import accountsUserLoginOTPModel
# <editor-fold desc="accountsClientotprequestSerializer">
class accountsClientotprequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountsUserLoginOTPModel
        fields = "__all__"
    def create(self,validated_data):
        return validated_data
# </editor-fold>


# <editor-fold desc="accountsClientCreateUserSerializer">
class accountsClientCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = accountsUserModel
        fields = ["phonenumber","email"]
# </editor-fold>
# <editor-fold desc="accountsClientMailOTPSerializer">
class accountsClientMailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.IntegerField(required=True)
    class Meta:
        fields ="__all__"
# </editor-fold>