from django.db import models

# Create your models here.

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255, unique=True)
    Email = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    #   0:user , 1:admin
    Role = models.IntegerField(default=0)
    def __str__(self):
        return f'id : {self.Id}, username : {self.Username}, email : {self.Email}, password : {self.Password}, role : {self.Role}'
class Post(models.Model):
    Id = models.AutoField(primary_key=True)
    Content = models.TextField(max_length=10240)
    Date = models.DateTimeField(auto_now_add=True)
    By = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, null=True)
    def __str__(self):
        return f'id: {self.Id}, content : {self.Content}, date : {self.Date}, By : {self.By}'


