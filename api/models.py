from django.db import models


class Collection(models.Model):
    class Grade(models.IntegerChoices):
        SEVENTH = 7
        EIGHTH = 8
        NINTH = 9

    grade = models.IntegerField(choices=Grade.choices)
    name = models.CharField(max_length=50)


class Question(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    options = models.CharField(max_length=1000, default="[{}, {}, {}, {}]")
    correct_option_index = models.IntegerField(default=0)
    date_update = models.DateTimeField('Update Date', auto_now=True)
