from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Question, Answer

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        models = User
        fields = ('id', 'username', 'password')

# ----------------------------------------------------------------

class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        models = Question
        fields = ('id', 'question', "user")

# ----------------------------------------------------------------

class AnswerSerializers(serializers.ModelSerializer):

    class Meta:
        models = Answer
        fields = ('id', 'answer')

