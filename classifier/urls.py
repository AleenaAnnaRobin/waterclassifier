from .views import Landing, Signup, QualityAnalysisView,Profile,EditProfile
from django.urls import path

urlpatterns=[
    path("",Landing.as_view(),name="landing"),
    path("profile/",Profile.as_view(),name="profile"),
    path("signup/",Signup.as_view(),name="signup"),
    path("profile/quality/",QualityAnalysisView.as_view(),name="quality"),
    path("profile/edit/<int:data_id>/",EditProfile.as_view(),name="edit"),
    ]