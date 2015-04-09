from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.db.models import Avg, Count, Max
from django.http import HttpResponse

from dashboard.models import Question, Anser, User

import json

class QuestionApi(View):

    def get(self, request, *args, **kwargs):
        self.query = {}
        response = {}
        self.query.update(self.request.GET)
        self.question = get_object_or_404(Question, pk=kwargs['pk'])
        self.ansers = self.question.anser_set

        for attr in dir(self):
            if attr.startswith('hydrate_'):
                response.update(getattr(self, attr)())

        return HttpResponse(json.dumps(dict(response)), content_type='application/json')

    def hydrate_anser_choice(self):
        data = self.ansers.values('choice').annotate(Count('choice'))
        for item in data:
            for field in ['sex', 'birthday', 'income', 'education']:
                item[field] = self.ansers.filter(
                    choice=item['choice']
                ).values('user__{}'.format(field)).annotate(count=Count('user__{}'.format(field))).order_by('-count')
                item[field] = list(item[field])
        return {'ansers_count': list(data)}
