from django.db import models
from datetime import timezone, datetime

class stockData_sam(models.Model):
    title = models.TextField()


    def __str__(self):
        return self.title

class stockData_lg(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class stockData_naver(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class stockData_kakao(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
class stockData_nc(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class user_post(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title