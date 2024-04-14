from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets, status


class StudentView(APIView):

    def get_student(self, pk):
        try:
            student = Student.objects.get(RegisterationNumber=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Added Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)

    def put(self, request, pk=None):
        student_to_update = Student.objects.get(RegisterationNumber=pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student updated Successfully", safe=False)
        return JsonResponse("Failed To Update Student")

    def delete(self, request, pk):
        student_to_delete = Student.objects.get(studentId=pk)
        student_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)

    def update_hostel_status(self, request, RegisterationNumber):
        student = self.get_object(RegisterationNumber)
        student.insidehostel = request.data['insidehostel']
        student.save()
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)