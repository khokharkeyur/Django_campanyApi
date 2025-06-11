from rest_framework import serializers
from . import models

class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = models.Employee
        fields = "__all__"