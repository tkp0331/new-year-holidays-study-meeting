from django.db import models

# Create your models here.

class Faculty(models.Model):
    id = models.IntegerField(verbose_name = '学部ID', primary_key=True)
    name = models.CharField(verbose_name = '学部名', max_length=20)
    
    class Meta:
        verbose_name_plural = "学部"
        
    def __str__(self):
        return self.name


class Student(models.Model):
    faculty_id = models.ForeignKey(Faculty, verbose_name='学部ID', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='氏名', max_length=30)
    email = models.EmailField(verbose_name='メールアドレス', max_length=50)
    
    class Meta:
        verbose_name_plural = "生徒"
        
    def __str__(self):
        return self.name

