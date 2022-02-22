from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()
from accounts.models import Managers


def get_house_album_path(instance, filename):
    house_number = instance.unit.unit_number
    return "unit-images/{0}/{1}".format(house_number, filename)

class Counties(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('by-county', args=[self.slug])

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Counties'
        ordering = ('name',)
        managed = True

class Estate(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=100, unique=True)
    registered_owner = models.CharField(max_length=50)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    registered_country = models.CharField(max_length=50, default='Kenya')
    added = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Estates'
        verbose_name = 'Estate'

    def __str__(self):
        return f"{self.name}"

class Building(models.Model):
    STATUS_CHOICES = [
        ('op', 'Vacancies Available'),
        ('um', 'Under Maintanance'),
        ('fo', 'Fully Occupied'),
        ('dc', 'Decomisioned'),
    ]
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    registered_owner = models.CharField(max_length=50)
    manager = models.ForeignKey(Managers, on_delete=models.CASCADE, related_name='building_manager')
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address_line = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='building-cover', null=True, blank=True)
    county = models.ForeignKey(Counties, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, default='Kenya')
    building_status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    added = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('building-units', args=[self.slug])

    def __str__(self):
        return f"{self.name}"

class UnitType(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    added = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Available Unit Types'

class RentalUnit(models.Model):
    MAINTANANCE_STATUS_CHOICES = [
        ('nm', 'Needs Inspection'),
        ('ip', 'Initiating Inspection'),
        ('ir', 'Maintanance In Progress'),
        ('op', 'No Active Reports'),
    ]
    STATUS_CHOICES = [
        ('occupied', 'Currently Occupied'),
        ('ready', 'Ready To Move In'),
        ('hold', 'On Hold'),
        ('maintanance', 'Under Maintanance'),
    ]
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, help_text='This field is autogenerated')
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    dimension = models.CharField(max_length=50)
    kitchen = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    maintanance_status = models.CharField(max_length=6, choices=MAINTANANCE_STATUS_CHOICES, default='op')
    total_occupants = models.PositiveIntegerField(help_text="Number of people in the unit", null=True, blank=True)
    water_available = models.BooleanField(default=True)
    electricity_available = models.BooleanField(default=True)
    added = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join((slugify(self.unit_number), slugify(self.building)))
            super(RentalUnit, self).save(*args, **kwargs)
        super(RentalUnit, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('building', 'unit_number')

    def get_url(self):
        return reverse('unit-details', args=(self.building.slug, self.slug))

    def __str__(self):
        return f"{self.unit_number} - {self.building}"

#TODO: Display only units in tenant building when updating the user

class UnitAlbum(models.Model):
    unit = models.ForeignKey(RentalUnit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_house_album_path, width_field='image_width', height_field='image_height')
    image_width = models.IntegerField(default=600)
    image_height = models.IntegerField(default=500)

    def __str__(self):
        return f"{self.unit.unit_number}"
