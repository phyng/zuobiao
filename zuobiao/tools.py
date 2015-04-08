

import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zuobiao.settings")

import django
django.setup()

from dashboard.models import Question, Anser, User
from dashboard.models import SEX_CHOICES, INCOME_CHOICES, EDU_CHOICES, ANSER_CHOICES

import datetime
import re

# Import date from csv
with open('2014data.csv', 'r') as f:
    reader = csv.reader(f)
    questions = []
    for i, row in enumerate(reader):
        print(i)
        if i == 0:
            for item in row[3:-4]:
                question = Question.objects.create(name=item.strip())
                questions.append(question)
        else:
            created, ip, = row[1:3]
            sex, birthday, income, education = row[-4:]
            if created == 'NULL' or sex == 'NULL' or not birthday:
                continue

            created = datetime.datetime.strptime(created, '%Y-%m-%d %H:%M:%S')
            education = [k for k, v in EDU_CHOICES if education == v][0]
            income = [k for k, v in INCOME_CHOICES if income == v][0]
            sex = 1 if sex == 'M' else 2

            user = User.objects.create(
                created=created,
                education=education,
                income=income,
                sex=sex,
                ip=ip,
                birthday=birthday
            )

            ansers = []
            for index, item in enumerate(row[3:-4]):
                ansers.append(Anser(
                    created=created,
                    question=questions[index],
                    user=user,
                    choice=[k for k, v in ANSER_CHOICES if item == v][0]
                ))
            Anser.objects.bulk_create(ansers)
