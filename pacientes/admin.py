from django.contrib import admin
from .models import Pacientes, Tarefas, Visualizacoes

admin.site.register(Pacientes)
admin.site.register(Tarefas)
admin.site.register(Visualizacoes)
