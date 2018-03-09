from django import template

register=template.Library()

@register.filter(name="cutt")
def cutt(value, arg):
    '''
    this cuts out all values of 'arg' from string
    '''
    return value.replace(arg, "")
