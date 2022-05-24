from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from schoolapp.serializers import StudentSerializer
from rest_framework.permissions import AllowAny
from schoolapp.models import Student
from rest_framework.response import Response


class StudentCreateAPIView(GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 201)


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    queryset = Student.objects.all()


class StudentDetailView(RetrieveAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    queryset = Student.objects.all()
    lookup_fields = 'pk'
