from django.db import models

class MyModel(models.Model):
    user = models.TextField (max_length=100)
    name = models.TextField(max_length=200)
    value = models.TextField(max_length=100)



    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'user': self.user,
            'value': self.value,
        }
