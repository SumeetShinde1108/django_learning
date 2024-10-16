from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Student
from .serializers import StudentSerializer


class LCStudentAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Handling GET request to list students
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Handling POST request to create a student
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RUDStudentAPI(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
