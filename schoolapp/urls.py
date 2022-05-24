from django.urls import path
from schoolapp.views import StudentCreateAPIView, StudentListAPIView, StudentDetailView


urlpatterns = [
    path('register/', StudentCreateAPIView.as_view(), name='student-create'),
    path('', StudentListAPIView.as_view(), name='student-list'),
    path('<pk>/', StudentDetailView.as_view(), name='student-detail'),
]
