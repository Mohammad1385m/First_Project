from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()


# returns 1385/9/6
@register.filter(name="jalali_date_1")
def jalali_date_1(value):
    return date2jalali(value).strftime("%Y/%m/%d")


@register.filter(name="jalali_date_2")
def jalali_date_2(value):
    return date2jalali(value).strftime("%d %B %Y")


@register.filter(name="discounted_value")
def discounted_value(value, discount):
    final_price = int(round(value - (value * discount / 100), 0))
    return final_price


@register.filter(name="item_counter")
def item_counter(value: list):
    return len(value)


@register.filter(name="total_price")
def total_price(value, amount):
    return value * discounted_value(amount.final_price, amount.off)


@register.filter(name="final_total_price")
def final_total_price(value):
    total_amount = 0
    for item in value:
        total_amount += item.final_price * item.count
    return total_amount
