from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
	poll_title = models.CharField(max_length=80)

	def __str__(self):
		return self.poll_title

class Question(models.Model):
	poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=255)

class Possible_ans(models.Model):
	poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
	ans_text = models.CharField(max_length=255)

class Actual_ans(models.Model):
	poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
	question_no = models.ForeignKey(Question, on_delete=models.CASCADE)
	ans_no = models.ForeignKey(Possible_ans, on_delete=models.CASCADE)

