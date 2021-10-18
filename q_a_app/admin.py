from django.contrib import admin
from django.db.models.query_utils import Q

from q_a_app.models import Answer, Question, User

# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)