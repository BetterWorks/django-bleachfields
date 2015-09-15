=====
django-bleachfields
=====
.. image:: https://travis-ci.org/BetterWorks/django-bleachfields.png
  :target: https://travis-ci.org/BetterWorks/django-bleachfields

django-bleachfields is a Python module that utilizes existing bleach and HTML parser modules to remove HTML tags and unescape text from a field before saving it to a Django model.
To use, simply call BleachJSONField or BleachTextField in place of a Django text field, such as models.TextField or models.CharField.

Install
--------
.. code-block:: python

    pip install bleachfields

Usage
--------
.. code-block:: python

    from django.db import models
    from bleachfields import BleachJSONField, BleachTextField

    class Person(models.Model):
      name = BleachTextField(max_length=256)
      response = BleachJSONField()

Contact
--------
Email: afrancis@betterworks.com

Changes
--------
None to date.
