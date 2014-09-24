from django.contrib import admin

from oas.models import Javaseer, Chirp

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

admin.site.register(Javaseer, JavaseerAdmin)
admin.site.register(Chirp, ChirpAdmin)
