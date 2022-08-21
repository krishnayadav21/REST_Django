from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializer import SerializerEmp

# Create your views here.

#Read
@api_view(['GET'])
def read(request):
    data = Employee.objects.all()    
    Result = SerializerEmp(data, many=True)
    return Response(Result.data)

#Create
@api_view(['POST'])
def create(request):
    a = SerializerEmp(data=request.data)
    if a.is_valid():
        a.save()
    return Response(a.data)


#Update
@api_view(['PUT'])
def update(request, Emp_id):
    a = Employee.objects.get(Emp_id=Emp_id)
    newdata = SerializerEmp(instance=a, data=request.data)
    if newdata.is_valid():
        newdata.save()
    return Response(newdata.data)


#Delete
@api_view(['DELETE'])
def delete(request, Emp_id):
    data = Employee.objects.filter(Emp_id=Emp_id)
    if data:
        data.delete()
        Result={"Result":f"Record of {Emp_id} is Deleted Successfully!!"}
    else:
        Result={"Result":"No record Found!!"}
    return Response(Result)


    