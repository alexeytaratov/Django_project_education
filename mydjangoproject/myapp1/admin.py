from django.contrib import admin
from myapp1.models import Worker # импортируем модель Воркер

admin.site.register(Worker) # регистрируем модель Воркер
