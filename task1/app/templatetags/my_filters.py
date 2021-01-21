from django import template

register = template.Library()


@register.filter
def colorize(value):
    try:
        if float(value) < 0:
            return 'green'
        elif 1 < float(value) <= 2:
            return 'lightsalmon'
        elif 2 < float(value) <= 5:
            return 'salmon'
        elif 5 < float(value) <= 100:
            return 'red'
    except ValueError:
        return 'white'

