from django.db import models


class Collection(models.Model):
    class Grade(models.IntegerChoices):
        SEVENTH = 7
        EIGHTH = 8
        NINTH = 9

    grade = models.IntegerField(choices=Grade.choices)
    name = models.CharField(max_length=50)

    def __str__(self):
        if self.grade == self.Grade.SEVENTH:
            return "هفتم" + "--" + self.name
        elif self.grade == self.Grade.EIGHTH:
            return "هشتم" + "--" + self.name
        elif self.grade == self.Grade.NINTH:
            return "نهم" + "--" + self.name
        else:
            return self.name


class Question(models.Model):

    class OptionChoice(models.IntegerChoices):
        OPTION1 = 1
        OPTION2 = 2
        OPTION3 = 3
        OPTION4 = 4

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField(choices=OptionChoice.choices, default=OptionChoice.choices[0])
    date_update = models.DateTimeField('Update Date', auto_now=True)

    def __str__(self):
        if self.collection.grade == Collection.Grade.SEVENTH:
            return "هفتم" + "--" + self.collection.name + "--" + self.question_text
        elif self.collection.grade == Collection.Grade.EIGHTH:
            return "هشتم" + "--" + self.collection.name + "--" + self.question_text
        elif self.collection.grade == Collection.Grade.NINTH:
            return "نهم" + "--" + self.collection.name + "--" + self.question_text
        else:
            return self.question_text