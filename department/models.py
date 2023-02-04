from django.db import models
from django.urls import reverse

from utility.common_fields import BaseModel


class Department(BaseModel):
    department_name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def get_update_url(self):
        return reverse('update_department',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_department',  kwargs={"pk": self.pk})

    def __str__(self):
        return self.department_name
