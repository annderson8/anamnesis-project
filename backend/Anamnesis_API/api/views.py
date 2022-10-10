import json

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Question

class QuestionView (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            questions = list(Question.objects.filter(id=id).values())
            if len(questions) > 0:
                question = questions[0]
                data = {'message':'Success', 'question': question}
            else:
                data = {'message': 'question not found'}
            return JsonResponse(data)
        else:
            questions = list(Question.objects.values())
            if len(questions) > 0:
                data = {'message':'Success', 'questions': questions}
            else:
                data = {'message': 'questions not found'}
            return JsonResponse(data)

    def post(self, request):
        json_data = json.loads(request.body)
        Question.objects.create(course=json_data['course'], topic=json_data['topic'], question_text=json_data['question_text'], answer_a=json_data['answer_a'], answer_b=json_data['answer_b'], answer_c=json_data['answer_c'], answer_d=json_data['answer_d'], correct_answer=json_data['correct_answer'], comment=json_data['comment'], image_url=json_data['image_url'], pub_date=json_data['pub_date'])

        data = {'message': 'Success'}
        return JsonResponse(data)
    
    def put(self, request, id):
        json_data = json.loads(request.body)
        questions = list(Question.objects.filter(id=id).values())
        if len(questions) > 0:
            question = Question.objects.get(id=id)
            question.course = json_data['course']
            question.topic = json_data['topic']
            question.question_text = json_data['question_text']
            question.answer_a = json_data['answer_a']
            question.answer_b = json_data['answer_b']
            question.answer_c = json_data['answer_c']
            question.answer_d = json_data['answer_d']
            question.correct_answer = json_data['correct_answer']
            question.comment = json_data['comment']
            question.image_url = json_data['image_url']
            question.pub_date = json_data['pub_date']
            question.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Question not found'}
        return JsonResponse(data)
    
    def delete(self, request, id):
        products = list(Question.objects.filter(id=id).values())
        if len(products) > 0:
            Question.objects.filter(id=id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Question not found'}
        return JsonResponse(data)