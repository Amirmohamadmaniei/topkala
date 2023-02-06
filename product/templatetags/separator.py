from django import template

register = template.Library()


@register.filter(name='separator')
def separator(value):
    value = str(value)
    copy_value = ''
    c = 1
    lv = len(value) - 1

    for i in range(lv, -1, -1):
        copy_value += value[i]
        if c % 3 == 0 and c <= lv:
            copy_value += ','
        c += 1
    return copy_value[::-1]
