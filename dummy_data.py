import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from books.models import Auther,Book,Review
from django.contrib.auth.models import User
import random
from faker import Faker

def add_Auther(n):
    fake = Faker()
    for x in range(n):
        Auther.objects.create(
            name = fake.name(),
            age = random.randint(25,75),
            biography= fake.text(max_nb_chars=500)
        )

    print(f'{n} Authers was created successfully')


#add_Auther(48)

