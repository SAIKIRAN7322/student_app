from django.urls import path

from accounts.api_client_v1.views import accountsClientCreateUserView, accountsClientGetUsersView, accountsLoginSystemView, accountsLoginGeneratingOtpView

urlpatterns = [


    # <editor-fold desc="Creating user and user profile">
    path("Create-User/",accountsClientCreateUserView.as_view(),name = "accountsClientCreateUserURL"),
    # </editor-fold>


    # <editor-fold desc="get all users">
    path("All-Users/",accountsClientGetUsersView.as_view(),name = "accountsClientGetUsersURL"),
    # </editor-fold>
    path("LoginOtp/",accountsLoginGeneratingOtpView.as_view(),name = "accountsLoginGeneratinOtpURL"),
    path("Login/",accountsLoginSystemView.as_view(),name ="accountsLoginSystemURL" ),

]