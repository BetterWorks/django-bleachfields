from django.db import models

from .bleachfield import BleachField


class BleachCharField(BleachField, models.CharField):

    def pre_save(self, model_instance, add):
        new_value = getattr(model_instance, self.attname)
        clean_value = self.clean_text(new_value)
        setattr(model_instance, self.attname, clean_value)
        return super(BleachCharField, self).pre_save(model_instance, add)
