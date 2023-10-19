from django.db import models

# Create your models here.
class BoardMessage(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тип задания")
    content = models.TextField(null=True, blank=True, verbose_name="Задание")
    deadline = models.DateField(verbose_name="Дедлайн")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    subject = models.ForeignKey("Subject", verbose_name="Предмет", on_delete=models.PROTECT, null=True)


    class Meta: 
        verbose_name="Задание"
        verbose_name_plural="Задания"
        ordering =  ['-published']
    
class Subject(models.Model): 
    name = models.CharField(max_length=50, verbose_name="Название", db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta: 
        verbose_name="Предмет"
        verbose_name_plural="Предметы"
        ordering =  ['name']