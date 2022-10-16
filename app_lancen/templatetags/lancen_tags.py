from django import template
register = template.Library()


@register.simple_tag()
def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


@register.inclusion_tag('templatetags/breadcrumbs.html')
def breadcrums(list):
    return {'breadcrumbs': list}