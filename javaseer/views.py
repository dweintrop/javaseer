from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from oas.models import Javaseer, Chirp, ChirpRun, PencilCodeEvent, Student

import os
import datetime
import json
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
		return HttpResponse('successfully created Log: ' + str(pencilCodeEvent.id))
	return HttpResponse('faliure')

def get_data(request, table):
	if 'filter' in request.GET:
		inFilter = request.GET['filter']
		if table == 'Students':
			teachers = Student.objects.filter(School="Northwestern").order_by("Name")
			students = Student.objects.filter(School=inFilter).order_by("Name")
			teacher_json = [({'studentID':t.StudentID, 'name': t.Name, 'username': t.Username, 'condition':t.Condition, 'password': t.Password}) for t in teachers]
			student_json = [({'studentID':s.StudentID, 'name': s.Name, 'username': s.Username, 'condition':s.Condition, 'password': s.Password}) for s in students]
			data_json = teacher_json + student_json
		# elif table == 'Section':
		#   teacher = Teacher.objects.get(id=inFilter)
		#   sections = Section.objects.filter(teacher=teacher)
		#   data_json = [(s.id, s.subject + ' ' + s.section) for s in sections]
		return HttpResponse(json.dumps({'table' : table, 'values': data_json}))#, mimetype="application/json")
	else:
		return HttpResponse(table)

