import os

import django
from faker import Faker

from app1.models import Clients


os.environ.setdefault("DJANGO_SETTINGS_MODULES", "project_two.settings")
django.setup()





def generate_data(n):
    f = Faker()
    for entry in range(n):
        print("generating {}th".format(entry))
        generated_name = f.name().split(" ")
        first_name = generated_name[0]
        last_name = generated_name[1]
        e_email = f.email()
        try:
             new = Clients.objects.get_or_create(FIRST_NAME=first_name, LAST_NAME=last_name, E_MAIL=e_email) 
        except:
            print("one entry insertion failed")

# Clients.objects.all().delete()
# generate_data(20)
for aa in range(Clients.objects.count()):
    print(Clients.objects.all()[aa].id)
    print(Clients.objects.all()[aa])
