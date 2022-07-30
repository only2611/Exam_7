from django.db import models

# Create your models here.
from django.urls import reverse

# from trecker.validate import summary_max_10_len




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract=True

class Poll(BaseModel):
    question = models.TextField(max_length=500, null=False, blank=False, verbose_name="Вопрос")

    def __str__(self):
        return f"{self.id}.{self.question} - {self.created_at}"

    def get_absolute_url(self):
        return reverse("poll-view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "questions"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    variant = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Текст варианта")
    poll = models.ForeignKey("interview.Poll", on_delete=models.CASCADE, related_name="polls",
                                     verbose_name="Опрос",)


    def __str__(self):
        return f"{self.id}--{self.variant}"




    class Meta:
        db_table = "variant"
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"




#
#
# class Task(BaseModel):
#     summary = models.CharField(max_length=30, null=False, blank=False, verbose_name="Заголовок", validators=[summary_max_10_len])
#     description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание задачи")
#     status = models.ForeignKey("trecker.Status", on_delete=models.PROTECT, related_name="statuses", verbose_name="Статус")
#     types = models.ManyToManyField("trecker.Type", related_name="tasks", blank=True)
#     project = models.ForeignKey("trecker.Project", on_delete=models.CASCADE, related_name="taskss",
#                                  verbose_name="Проект", default=1)
#
#
#     def __str__(self):
#         return f"{self.id}.{self.summary} - {self.description}"
#
#     # def get_absolute_url(self):
#     #     return reverse("project-view", kwargs={"pk": self.pk})
#
#
#     class Meta:
#         db_table = "tasks"
#         verbose_name = "Задача"
#         verbose_name_plural = "Задачи"
#
#
# class Status(models.Model):
#     name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Статус")
#
#     def __str__(self):
#         return f"{self.name}"
#
#     class Meta:
#         db_table = "statuses"
#         verbose_name = "Статус"
#         verbose_name_plural = "Статусы"
#
#
# class Type(models.Model):
#     name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Тип")
#
#     def __str__(self):
#         return f"{self.name}"
#
#     class Meta:
#         db_table = "types"
#         verbose_name = "Тип"
#         verbose_name_plural = "Типы"
#
#
#
# class Project(models.Model):
#     name = models.CharField(max_length=30, verbose_name="Наименование проекта")
#     description = models.TextField(max_length=500, verbose_name="Описание проекта")
#     start_date = models.DateField(verbose_name="Дата начала")
#     finish_date = models.DateField(null=True, blank=True, verbose_name="Дата завершения")
#
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def get_absolute_url(self):
#         return reverse("project-view", kwargs={"pk": self.pk})
#
#     class Meta:
#         db_table = "projects"
#         verbose_name = "Проект"
#         verbose_name_plural = "Проекты"
