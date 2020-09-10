from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    #M:N 관계설정 하기위해 ManyToManyField 사용
    #첫번째 인자: django 내장된 유저모델 사용하기위함
    #관계된 변수명 related_name속성의 속성값으로 표시

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    post = models.ForeignKey('myblog.Post', on_delete = models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content