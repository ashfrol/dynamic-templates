from datetime import datetime, time

from django import template


register = template.Library()


@register.filter
def format_date(value):
    today = int(datetime.now().timestamp())
    how_long = today - value
    if how_long // (60 * 60 * 24) > 24:
        return f'Дата публикации {time.ctime(value)}'
    elif 60 * 10 < how_long < 60 * 60 * 24:
        hours = int(how_long // (60 * 60))
        return f'{hours} часов назад'
    else:
        return 'Только что'

@register.filter
def format_score(value: int = 0):
    if value > 5:
        return 'Хороший пост'
    elif -5 < value < 5:
        return 'Неплохой пост'
    else:
        return 'Не стоит внимания'

@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return f'{value} комментариев'
    elif value > 50:
        return '50+ комментариев'

@register.filter
def format_selftext(text, count=5):
    post = text.split()
    short_post_start = ' '.join(post[:(count - 1)])
    short_post_end = ' '.join(post[-(count - 1):])
    return f'{short_post_start} ... {short_post_end}'





