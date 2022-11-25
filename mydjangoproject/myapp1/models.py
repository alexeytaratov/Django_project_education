from django.db import models

class Worker(models.Model): # создали модель (таблицу)
    name = models.CharField(max_length=20, blank=False) # тут описываем столбцы.
                                                        # CharField - строковый тип данных
                                                        # max_length - максимальная длина
                                                        # blank=False - указываем, что не может быть пустым
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0) # IntegerField - число, default=0 - по-умолчанию = 0

    def __str__(self): # это метод, который позвоняет переименовать название строк в админке Джанго
        return self.second_name # переименовываем на фамилию