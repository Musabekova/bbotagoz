from django.db import models
# Create your models here.

from django.urls import reverse


class Dancer(models.Model):
    first_name = models.CharField(max_length=200, help_text="Есімін енгізініз")
    last_name = models.CharField(max_length=200, help_text="Тегін енгізініз")
    date_of_birth = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["last_name", "first_name"]


    def get_absolute_url(self):
        return reverse('dancer-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.last_name, self.first_name)


class Coach(models.Model):
    first_name = models.CharField(max_length=200, help_text="Есімін енгізініз")
    last_name = models.CharField(max_length=200, help_text="Тегін енгізініз")
    date_of_birth = models.DateField(null=True, blank=True)
    awards = models.CharField(max_length=200, help_text="Марапаттарды енгізініз")

    class Meta:
        ordering = ["first_name","last_name"]

    def get_absolute_url(self):
        return reverse('coach-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.first_name,self.last_name)


