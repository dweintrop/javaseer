from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from oas.models import Javaseer

import os
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
		return HttpResponse('')
	return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')
	# return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')

def setup(request):

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	setup_text = open(os.path.join(BASE_DIR, '../scripts/setup.sh'), 'rb').read()

	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="setup.sh"'
	response.write(setup_text)

	return response