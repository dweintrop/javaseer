from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from oas.models import Javaseer, Chirp, ChirpRun, PencilCodeEvent, Student, QuickRef

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
		  Hostname = request.POST['hostname'],
		  TimeStamp = datetime.datetime.now(),
		  EditorMode = request.POST['editorMode'],
		  PaletteVisible = request.POST['paletteVisible'],
		  Condition = request.POST['condition'],
		  EventType = request.POST['eventType'],
		  Program = request.POST['program'],
		  FloatingBlocks = request.POST['floatingBlocks'],
		  ProjectHTML = request.POST['projectHTML'],
		  ProjectCSS = request.POST['projectCSS']
			)
		pencilCodeEvent.save()
		return HttpResponse('successfully created PencilCodeEvent: ' + str(pencilCodeEvent.id))
	return HttpResponse('faliure')

# store a user pencil code interaction
def pencilCodeQuickRef(request): 
	if request.method == 'POST':
		quickRef = QuickRef(
		  StudentID = request.POST['student_id'],
		  Assignment = request.POST['assignment'],
		  Hostname = request.POST['hostname'],
		  EditorMode = request.POST['editorMode'],
		  Condition = request.POST['condition'],
		  Page = request.POST['page'],
			)
		quickRef.save()
		return HttpResponse('successfully created QuickRef: ' + str(quickRef.id))
	return HttpResponse('faliure')

def get_data(request, table):
	if 'filter' in request.GET:
		inFilter = request.GET['filter']
		if table == 'Students':
			inSchool = inFilter
			inClass = ' '
			if ' - ' in inFilter:
				inSchool = inFilter.split(' - ')[0]
				inClass = inFilter.split(' - ')[1]

			admins = Student.objects.filter(School='Northwestern', Class="Admin").order_by("Name")
			teachers = Student.objects.filter(School=inSchool, Class="Admin").order_by("Name")
			students = Student.objects.filter(School=inSchool, Class=inClass).order_by("Name")

			# for both admins and teachers, take the condition from the first student as they're broken down by class
			admin_json = [({'studentID':a.StudentID, 'name': a.Name, 'username': a.Username, 'condition':students[0].Condition, 'password': a.Password}) for a in admins]
			teacher_json = [({'studentID':t.StudentID, 'name': t.Name, 'username': t.Username, 'condition':students[0].Condition, 'password': t.Password}) for t in teachers]
			student_json = [({'studentID':s.StudentID, 'name': s.Name, 'username': s.Username, 'condition':s.Condition, 'password': s.Password}) for s in students]
			data_json = admin_json + teacher_json + student_json
		return HttpResponse(json.dumps({'table' : table, 'values': data_json}))#, mimetype="application/json")
	else:
		return HttpResponse(table)

