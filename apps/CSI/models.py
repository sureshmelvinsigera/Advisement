from django.db import models


# Create your models here.

class office_hours(models.Model):
    WEEKDAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sun'),
    )

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return '{} {} {}'.format(self.weekday, self.from_hour, self.to_hour)


class advisor(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    office = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    hours = models.ForeignKey(office_hours, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.hours)


class student(models.Model):
    std_id = models.CharField(max_length=255, null=False)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    major_choices = (('CS', 'Computer Science'), ('ISI', 'Information Systems'))
    major = models.CharField(max_length=3, choices=major_choices, null=False)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=False)
    advisor = models.ForeignKey(advisor, on_delete='models.CASCADE')

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)
