from django.db import models
from django.contrib.auth.models import User

PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
    ('None', 'None'),
)
class Todo(models.Model):
    title = models.CharField(max_length=169)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    # connection to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #return the title in the admin panel **NOT WORKING**
    def __str__(self):
        return self.title + ' | ' + str(self.user   )

