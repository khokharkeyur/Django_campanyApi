from rest_framework import serializers
from . import models

class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"