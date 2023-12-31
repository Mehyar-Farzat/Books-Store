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


# add_Auther(49)


#____________________________________#


def add_books(n):
    fake = Faker()
    for x in range(n):
       Book.objects.create(
           title = fake.text(max_nb_chars=20),
           auther=Auther.objects.get(id=random.randint(1,50)),
           price=round(random.uniform(10.99,90.99),2),

       )

    print(f'{n} Books was created successfully')


# add_books(998)


#______________________________________________#

def add_review(n):
    fake = Faker()

    for x in range(n):
        Review.objects.create(
            book= Book.objects.get(id=random.randint(1,1000)),
            reviewer_name= User.objects.get(id=random.randint(1,5)),
            content=fake.text(max_nb_chars=200),
            rate = random.randint(1,5)
        )

    print(f'{n} Reviews was created successfully')



# add_review(2998)

