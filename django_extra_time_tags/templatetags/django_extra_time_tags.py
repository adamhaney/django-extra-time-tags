# -*- coding: utf-8 -*-

from timedelta import nice_repr

from django import template

from ..formatters import humanize_minutes


register = template.Library()


register.filter('humanize_minutes', humanize_minutes)


@register.filter(name='timedelta')
def timedelta(value, display="long"):
    if value is None:
        return value
    return nice_repr(value, display)
