from django.urls import path
from .views import studentdetailsClientSDView,studentdetailsClientSingleSdetailsView,studentdetailsCreateStudentView,studentdetailsClientUploadingMarksView,studentdetailsClientGradesandFinalgradeView,studentdetailsCreateSDWithBranchAndMarksView
urlpatterns=[

    path('all-students/', studentdetailsClientSDView.as_view(),name="studentdetailsclientStudentDetailsURL"),
    path("single-student-details/<int:id>/",studentdetailsClientSingleSdetailsView.as_view(),name='studentdetailsclientsinglestudentdetailsURL'),
    path('create-student/',studentdetailsCreateStudentView.as_view(),name='studentdetailsclientcreatestudentURL'),
    path('add-student-marks/<int:id>/', studentdetailsClientUploadingMarksView.as_view(),name="studentdetailsclientuploadingmarksURL"),
    path("student-marks/<int:id>/",studentdetailsClientGradesandFinalgradeView.as_view(),name="studentdetailsclientgradesandfinalgradeURL"),
    path("create-student-branch-marks/",studentdetailsCreateSDWithBranchAndMarksView.as_view(),name='studentdetailsCreateSDWithBranchAndMarksURL')
]