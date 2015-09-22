import csv, codecs, cStringIO
from django.contrib import admin
from django.http import HttpResponse

from oas.models import Javaseer, Chirp, ChirpRun, PencilCodeEvent, Student, QuickRef

class JavaseerAdmin(admin.ModelAdmin):
  list_display = ('StudentID', 'TimeStamp', 'JavacCall')
  list_filter = ('StudentID', 'JavacCall')
  # actions = ['export_snapTextInteractions']

  # def export_snapTextInteractions(studentadmin, request, queryset):
  #       response = HttpResponse(content_type='text/csv')

  #       writer = UnicodeWriter(response)
  #       writer.writerow(['SnapRun DB ID', 'Student ID', 'Pair ID', 'TimeStamp', 'Interaction Type', 'Condition', 'Text'])

  #       for run in queryset:
  #           run_info = [run.id, run.StudentID, run.PairID, run.TimeStamp, run.InteractionType, run.Condition, run.Text]
  #           writer.writerow(run_info)

  #       response['Content-Disposition'] = 'attachment; filename="snapinteractions.csv"'
  #       return response

class ChirpAdmin(admin.ModelAdmin):
  list_display = ('StudentID', 'TimeStamp', 'JavacCall')
  list_filter = ('StudentID', 'JavacCall')

class ChirpRunAdmin(admin.ModelAdmin):
  list_display = ('StudentID', 'TimeStamp', 'ClassName')
  list_filter = ('StudentID', 'ClassName')

class PencilCodeEventAdmin(admin.ModelAdmin):
  list_display = ('id', 'StudentID', 'Hostname', 'Assignment', 'ProjectName','TimeStamp', 'Condition', 'EventType')
  list_filter = ('TimeStamp', 'Assignment', 'Condition', 'StudentID')
  actions = ['export_pencil_code_events']

  def export_pencil_code_events(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    header = ['DB ID', 'studentID', 'assignment', 'url', 'ProjectName', 'TimeStamp', 'condition', 'EditorMode', 'PaletteVisible', 'EventType', 'Program', 'FloatingBlocks', 'ProjectHTML', 'ProjectCSS']

    has_header = False

    for a in queryset:
      a_info = [a.id, a.StudentID, a.Assignment, a.Hostname, a.ProjectName, a.TimeStamp, a.Condition, a.EditorMode, a.PaletteVisible, a.EventType, a.Program, a.FloatingBlocks, a.ProjectHTML, a.ProjectCSS]
      if not has_header:
        writer.writerow(header)
        has_header = True
      writer.writerow([unicode(a).encode("utf-8") for a in a_info])
    response['Content-Disposition'] = 'attachment; filename="pencilcodeevents.csv"'

    return response

class StudentAdmin(admin.ModelAdmin):
  list_display = ('StudentID', 'Name', 'School', 'Class', 'Condition')
  list_filter = ('School', 'Condition')

class QuickRefAdmin(admin.ModelAdmin):
  list_display = ('id', 'StudentID', 'Condition', 'Page', 'TimeStamp')
  list_filter = ('Condition', 'Page')



admin.site.register(Javaseer, JavaseerAdmin)
admin.site.register(Chirp, ChirpAdmin)
admin.site.register(ChirpRun, ChirpRunAdmin)
admin.site.register(PencilCodeEvent, PencilCodeEventAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(QuickRef, QuickRefAdmin)


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
