from rest_framework import serializers
from .models import Student, Gatepass, DayScholar, Hostelite


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
                'FirstName',
                'RegisterationNumber',
                'insidehostel')


class GatepassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatepass
        fields = ('GatePassNo',
                  'outdate',
                  'indate')


class DayScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayScholar
        fields = ('BusFacility',
                  'Residence'
                  'Address')


class HosteliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostelite
        fields = ('HostelBlock',
                  'RoomNo',
                  'Residence')



