import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

#FAKE POP SCRIPT
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fake_generator = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get the foreign key for the topic entry
        top = add_topic()

        #fake data for data entry
        fake_url = fake_generator.url()
        fake_name = fake_generator.company()
        fake_date = fake_generator.date()

        #create new web entry
        web_page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create fake access AccessRecord
        access_record = AccessRecord.objects.get_or_create(name=web_page, date= fake_date)

if __name__ == '__main__':
    print("populating script!")
    populate()
    print("populating complete!")
