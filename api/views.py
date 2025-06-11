from django.shortcuts import render
from rest_framework import viewsets 
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.companySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = models.Company.objects.get(pk=pk)
            emp = models.Employee.objects.filter(company=company)
            serializer = serializers.employeeSerializer(emp, many=True,context={'request': request})
            return Response(serializer.data)
        except models.Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)
        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.employeeSerializer