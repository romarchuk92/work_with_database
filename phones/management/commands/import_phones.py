import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


from django.http import HttpResponse
# with open('phones.csv', 'r') as file:
#         phones = list(csv.DictReader(file, delimiter=';'))

#         for phone in phones:
#             print(phone)
#             # Phone.objects.create(name = phone.name)



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # phones_list = Phone.objects.all()

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            # print(phones)
            for phone in phones:

                Phone.objects.create(
                    id = phone['id'], 
                    name = phone['name'], 
                    image = phone['image'],
                    price =  phone['price'],
                    release_date = phone['release_date'],
                    lte_exists = phone['lte_exists'],
                    slug = phone['name']
                )
        return HttpResponse('Все ОК')        
            # TODO: Добавьте сохранение модели
            # pass
