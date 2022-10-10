from django.db import models

class Question(models.Model):
    course = models.CharField(max_length = 40)
    topic = models.CharField(max_length = 40)
    question_text = models.TextField()
    answer_a = models.TextField()
    answer_b = models.TextField()
    answer_c = models.TextField()
    answer_d = models.TextField()
    correct_answer = models.CharField(max_length=2)
    comment = models.TextField()
    image_url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')


