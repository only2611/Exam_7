from django.db import models

# Create your models here.
from django.urls import reverse






class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")


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




class Answering(BaseModel):
    polls = models.ForeignKey("interview.Poll", on_delete=models.CASCADE, related_name="polles",
                                     verbose_name="Опрос",)
    variantes = models.ForeignKey("interview.Choice", on_delete=models.CASCADE, related_name="vars",
                                     verbose_name="Вариант",)





    class Meta:
        db_table = "answering"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответ"