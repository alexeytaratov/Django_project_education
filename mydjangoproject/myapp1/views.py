from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):

    worker_to_change = Worker.objects.get(id=3) # используем этот метод, когда нужно получить 1 запись с точным условием
                                                # (например, с айдишником 5)
    worker_to_change.name = 'Абоба' # меняем имя на другое
    worker_to_change.save() # записываем в базу данных

    Worker.objects.get(id=2).delete() # так мы удаляем конкретный элемент в базе данных

    #new_worker = Worker(name='Ваня', second_name='Иванов', salary=200000) # создаём новый объект класса нашей таблицы,
                                                                          # то есть создаём новую строчку в таблице
    #new_worker.save() # сохраняем объект в базу данных

    # две эти вышеописанные строчки можно заменить одной:
    # Worker.objects.create(name='Иван', second_name='Иванов', salary=200000)

    #all_workers = Worker.objects.all() # олл_воркерс - просто переменная, в которую записывается результат
                                       # Воркер - наша модель (её надо не забыть импортировать в этот файл
                                       # обджектс - в Джанго называется менеджер
                                       # олл - метод этого менеджера
    # то есть, конструкция Worker.objects.all() вызывает список всех объектов этой модели
    # или по-другому всех строк из нашей таблицы в базе данных
    #all_workers = Worker.objects.filter(salary=100000) # выводит только те объекты, в которых истинн фильтр
    all_workers = Worker.objects.all()


    for i in all_workers:
        print(i.second_name, i.name, i.salary, i.id)

    #print(all_workers) # выводим всё на терминале
    return render(request, 'index.html')
