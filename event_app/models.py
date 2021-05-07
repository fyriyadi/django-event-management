from django.db import models
from django.contrib.auth.models import User
import multiselectfield

   

class Event(models.Model):
    event_name = models.CharField(max_length=200, null=True)
    categories = (('Webinar','webinar'), ('Seminar','seminar'), ('Workshop','workshop'))
    event_category = models.CharField(max_length=20, choices=categories, null=True, default='Workshop')
    audiences = (('Umum','umum'), ('Guru','guru'))
    event_audience = models.CharField(max_length=20, choices=audiences, null=True, default='Umum')
    ticket_price = models.IntegerField(null=True, default=0)
    ticket_available = models.IntegerField(null=True, default=0)
    event_summary = models.CharField(max_length=100, null=True)
    event_date = models.DateField(null=True, blank=True,default='2021-05-19')
    event_start_time = models.TimeField(null=True, blank=True, default='08:30')
    event_finish_time = models.TimeField(null=True, blank=True, default='14:30')
    event_facilities = models.ManyToManyField('Facility', blank=True)
    event_venue = models.CharField(max_length=100, null=True)
    event_trainer = models.ManyToManyField('Trainer', blank=True)
    event_thumbnail = models.ImageField(null=True, blank=True)
    event_image_header = models.ImageField(null=True, blank=True)
    event_detail = models.CharField(max_length=500, null=True)
    event_contact_person = models.CharField(max_length=200, null=True)    
    
    def __str__(self):
        return self.event_name

class Facility(models.Model):
    facility_name = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=20, null=True, default="bookmark")

    def __str__(self):
        return self.facility_name




class Trainer(models.Model):
	trainer_name = models.CharField(max_length=100, null=True)
	trainer_photo = models.ImageField(null=True, blank=True)
	trainer_title = models.CharField(max_length=100, null=True)
	trainer_twitter = models.CharField(max_length=200, blank=True, null=True)
	trainer_linkedin = models.CharField(max_length=200, blank=True, null=True)
	

	def __str__(self):
		return self.trainer_name

	@property
	def imageURL(self):
		try:
			url = self.trainer_photo.url
		except:
			url = ''
		return url


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    payment_status = models.BooleanField(default=False, null=True, blank=False)
    attendance_status = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return '%s %s' % (self.participant, self.event)