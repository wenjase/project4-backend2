from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.username)


class Question(models.Model):
    question = models.TextField(max_length=1000)
    # user = models.ForeignKey(
    #     User,
    #     related_name='questions',
    #     on_delete=models.CASCADE
    # )


    def __str__(self):
        return str(self.question)

class Answer(models.Model):
    answer = models.TextField(max_length=1000)
    # question = models.ForeignKey(
    #     Question,
    #     related_name='answers',
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        return str(self.answer)