from django.db import models

class YandexKeyModel(models.Model):
    key = models.CharField(max_length=100, verbose_name='Ключ апи')

    def __str__(self) -> str:
        return "{}".format(self.id)



class KeysModel(models.Model):
    targetLanguageCode = models.CharField(max_length=10, verbose_name='Язык в который переводить ')
    sourceLanguageCode = models.CharField(max_length=10, verbose_name='Язык с которого переводить ')

    def __str__(self) -> str:
        return " c {} в {}".format(self.sourceLanguageCode, self.targetLanguageCode)

