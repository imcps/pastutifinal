from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.template.defaultfilters import slugify
from django.core.validators import URLValidator
import datetime
from django.utils import timezone

class TechProfile(models.Model):
	name = models.CharField(max_length = 65)
	email = models.EmailField(max_length = 60,null = True, blank = True)
	mobileNumber = models.BigIntegerField()

	def __str__(self):
		return '%s'%(self.name)


class Team(models.Model):
	teamName = models.CharField(max_length=50, null=True, blank=True)
	event = models.CharField(max_length = 60)
	teamLeader = models.ForeignKey(TechProfile, related_name = 'teamLeader')
	#members = models.ManyToManyField(TechProfile, related_name = 'members')

	def __str__(self):
		return '%s'%(self.teamName)
	
class Members(models.Model):
	name = models.CharField(max_length = 65, null = False, blank = False)
	email = models.EmailField(max_length = 60,null = True, blank = True)
	mobileNumber = models.BigIntegerField()
	team = models.ForeignKey(Team)
	teamLeader = models.ForeignKey(TechProfile)

	def __str__(self):
		return '%s %s'%(self.name, self.team.teamName)