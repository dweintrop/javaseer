from django.shortcuts import render
from django.http import HttpResponse

from oas.models import Javaseer

import datetime

# endpoint for javaseer calls that push data fro student computers to my database
def javaseer(request):
	if request.method == 'POST':
		javaseer = Javaseer(
			StudentID = request.POST['student_id'],
			StudentName = request.POST['student_name'],
			JavacCall = request.POST['javacCall'],
			TimeStamp = datetime.datetime.now(),
			JavaProgram = request.POST['javaProgram'],
			JavaCompilerOutput = request.POST['javaCompilerOutput'],
			)
		javaseer.save()
		return HttpResponse('success')
	return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')
	# return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')
