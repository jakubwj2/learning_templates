from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    """This cuts out all values of "arg" from the string."

    Args:
        value (String): the value to cut out from
        arg (String): the argument to cut out
    """
    return value.replace(arg, "")


# register.filter("cut", cut)
