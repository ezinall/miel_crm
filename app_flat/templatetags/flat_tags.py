from django import template

register = template.Library()


@register.filter
def status_len(flats, status_id):
    if status_id == 6:
        flat_list_1 = flats.filter(status=status_id)
        flat_list_2 = flats.filter(status=status_id+1)
        flat_list = len(flat_list_1) + len(flat_list_2)
        return int(flat_list / len(flats) * 100)
    else:
        flat_list = flats.filter(status=status_id)
        return int(len(flat_list) / len(flats) * 100)


@register.filter
def sep_price(price):
    counter = 0
    format_price = ''
    for i in reversed(str(price)):
        counter += 1
        format_price += i
        if not counter % 3 and counter < len(str(price)):
            format_price += ' '
    return format_price[::-1]
