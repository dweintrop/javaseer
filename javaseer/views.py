from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from oas.models import Javaseer, Chirp

import os
import datetime
import logging    


# endpoint for javaseer calls that push data fro student computers to my database
def javaseer(request):
	if request.method == 'POST':
		javaseer = Javaseer(
			StudentID = request.POST['student_id'],
			StudentName = request.POST['student_name'],
			Source = 'command line',
			JavacCall = request.POST['javacCall'],
			TimeStamp = datetime.datetime.now(),
			JavaProgram = request.POST['javaProgram'],
			JavaCompilerOutput = request.POST['javaCompilerOutput'],
			)
		javaseer.save()
		return HttpResponse('')
	return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')
	# return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')


# endpoint for javaseer calls that push data fro student computers to my database
def chirp(request):
	# Logger
	log = logging.getLogger(__name__)

	log.info(request)

	chirp = Chirp(
		StudentID = 'id',#request.POST['FILE_NAME'],
		StudentName = 'name',#request.POST['FILE_NAME'],
		Source = 'BlueJ',
		JavacCall = request.POST['FILE_NAME'],
		TimeStamp = datetime.datetime.now(),
		JavaProgram = request.POST['FILE_CONTENTS'],
		JavaCompilerOutput = request.POST['MSG_TYPE'] + ': ' + request.POST['MSG_MESSAGE'],
		NumCompiles = request.POST['TOTAL_COMPILES']
		)
	chirp.save()
	


	# if request.method == 'POST':
	# 	javaseer = Javaseer(
	# 		StudentID = request.POST['student_id'],
	# 		StudentName = request.POST['student_name'],
	# 		JavacCall = request.POST['javacCall'],
	# 		TimeStamp = datetime.datetime.now(),
	# 		JavaProgram = request.POST['javaProgram'],
	# 		JavaCompilerOutput = request.POST['javaCompilerOutput'],
	# 		)
	# 	javaseer.save()
	# 	return HttpResponse('')
	return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')
	# return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')



def setup(request):

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	setup_text = open(os.path.join(BASE_DIR, '../scripts/setup.sh'), 'rb').read()

	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="setup.sh"'
	response.write(setup_text)

	return response