from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from oas.models import Javaseer, Chirp, ChirpRun, PencilCodeEvent

import os
import datetime
import logging    


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


# endpoint for javaseer calls that push data from BlueJ to my database
def chirp(request):
	# Logger
	log = logging.getLogger(__name__)

	log.info(request)
	if request.method == 'POST':
		if request.POST['DELTA_NAME'] == 'CompileData':
			# BlueJ Compile Event
			chirp = Chirp(
				StudentID = request.POST['STUDENT_ID'],
				StudentName = request.POST['STUDENT_NAME'],
				JavacCall = request.POST['FILE_NAME'],
				TimeStamp = datetime.datetime.now(),
				JavaProgram = request.POST['FILE_CONTENTS'],
				JavaCompilerOutput = request.POST['MSG_TYPE'] + ': ' + request.POST['MSG_MESSAGE'],
				NumCompiles = request.POST['TOTAL_COMPILES']
				)
			chirp.save()
			
		if request.POST['DELTA_NAME'] == 'InvocationData':
			# BlueJ Run (Ojbect invoked) Event
			chirpRun = ChirpRun (
				StudentID = request.POST['STUDENT_ID'],
				StudentName = request.POST['STUDENT_NAME'],
				ClassName = request.POST['CLASS_NAME'],
				MethodName = request.POST['METHOD_NAME'],
				ObjectName = request.POST['OBJECT_NAME'],
				Parameters = request.POST['PARAMETERS'],
				Result = request.POST['RESULT'],
				TimeStamp = datetime.datetime.now()
				)
			chirpRun.save()
		return HttpResponse('')
	return HttpResponse('There was an error recording your compilation - please tell Mr. Weintrop')

def setup(request):

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	setup_text = open(os.path.join(BASE_DIR, '../scripts/setup.sh'), 'rb').read()

	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="setup.sh"'
	response.write(setup_text)

	return response


# store a user pencil code interaction
def pencilCoder(request): 
	if request.method == 'POST':
		pencilCodeEvent = PencilCodeEvent(
		  StudentID = request.POST['student_id'],
		  Assignment = request.POST['assignment'],
		  ProjectName = request.POST['project_name'],
		  TimeStamp = datetime.datetime.now(),
		  EditorMode = request.POST['editorMode'],
		  Condition = request.POST['condition'],
		  EventType = request.POST['eventType'],
		  Program = request.POST['program'],
		  FloatingBlocks = request.POST['floatingBlocks'],
		  ProjectHTML = request.POST['projectHTML'],
		  ProjectCSS = request.POST['projectCSS']
			)
		pencilCodeEvent.save()
		return HttpResponse('success')
	return HttpResponse('faliure')


