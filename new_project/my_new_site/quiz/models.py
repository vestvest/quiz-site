from django.db import models
from django.core.validators import RegexValidator

# class User(models.Model):
# 	name = models.CharField(max_length=100, verbose_name='Participant  Name')
#     email = models.EmailField(unique=True, verbose_name='Participant  Email')


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Question(models.Model):
    statement = models.CharField(
        max_length=500, null=True, verbose_name="Question statement"
    )
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", max_length=500, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.statement


ANSWER_CHOICES = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(
        max_length=2, blank=False, null=False, choices=ANSWER_CHOICES
    )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", max_length=500, blank=True)

    def __str__(self):
        return self.question.statement


class Result(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.CharField(max_length=500, null=True, blank=True)
    answers = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user)
