from django.db import models
from datetime import datetime
import string
import random


def generate_random_string(string_length=6):
    random_string = ''
    alpha_numerals = string.ascii_letters + string.digits
    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)
    return random_string


class Shortener(models.Model):
    long_url = models.URLField(null=False, blank=False, unique=True)
    short_url = models.CharField(max_length=6, primary_key=True, default=generate_random_string)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.long_url}: {self.short_url}'

    class Meta:
        ordering = ['-added']