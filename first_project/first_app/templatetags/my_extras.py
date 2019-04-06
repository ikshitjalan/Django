from django import template

register = template.Library()

def cut(value,arg):
    """
    Cuts the "arg"  in the value
    """
    return value.replace(arg,'')

register.filter('cut',cut)
