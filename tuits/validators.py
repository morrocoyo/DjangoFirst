#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:32:57 2017

"""
from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever', 'Pizza']

def validate_category(value):
    cat=value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} No es un tipo de categoria aceptado')
        