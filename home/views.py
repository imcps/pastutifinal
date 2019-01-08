from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
import os

def landing(request):
	return render(request, 'index.html', {})



def register(request):
	if request.method == 'POST':
		post = request.POST

		print post

		tech_profile = TechProfile()
		tech_profile.email = post.get('leader-email')
		tech_profile.name = post.get('leader-name')
		tech_profile.mobileNumber = post.get('leader-contact')

		tech_profile.save()

		team = Team()
		team.teamName = post.get('team-name')
		team.teamLeader = post.get('leader-name')
		team.event = post.get('event')
		team.save()

		# for memeber 1
		try:
			mem1 = Members()

			mem1.name = post.get('mem1-name')
			mem1.email = post.get('mem1-email')
			mem1.mobileNumber = post.get('mem1-contact')
			mem1.team = team
			mem1.teamLeader = tech_profile

			mem1.save()

		except:
			print "no mem1"
			pass


			# member 2
		try:
			mem2 = Members()

			mem2.name = post.get('mem2-name')
			mem2.email = post.get('mem2-email')
			mem2.mobileNumber = post.get('mem2-contact')
			mem2.team = team
			mem2.teamLeader = tech_profile

			mem2.save()

		except:
			pass


		try:
			mem3 = Members()

			mem3.name = post.get('mem3-name')
			mem3.email = post.get('mem3-email')
			mem3.mobileNumber = post.get('mem3-contact')
			mem3.team = team
			mem3.teamLeader = tech_profile

			mem3.save()

		except:
			pass


		try:
			mem4 = Members()

			mem4.name = post.get('mem4-name')
			mem4.email = post.get('mem4-email')
			mem4.mobileNumber = post.get('mem4-contact')
			mem4.team = team
			mem4.teamLeader = tech_profile

			mem4.save()

		except:
			pass


