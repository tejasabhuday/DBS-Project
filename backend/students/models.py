from django.db import models


class Student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Batch = models.CharField(max_length=100)
    RegisterationNumber = models.CharField(primary_key=True, max_length=9)
    Department = models.CharField(max_length=100)
    in_time = models.DateTimeField(null=True, auto_now_add=True)
    out_time = models.DateTimeField(null=True)
    Residence = models.CharField(max_length=100)
    insidehostel = models.BooleanField(default=False)

    def __str__(self):
        return self.RegisterationNumber


class DayScholar(models.Model):
    BusFacility = models.BooleanField(default=False)
    Residence = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Address


class Hostelite(models.Model):
    HostelBlock = models.CharField(max_length=100)
    RoomNo = models.CharField(max_length=4)
    Residence = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.RoomNo


class Gatepass(models.Model):
    GatePassNo = models.AutoField(primary_key=True)
    outdate = models.DateField()
    indate = models.DateField()

    def __str__(self):
        return self.GatePassNo
