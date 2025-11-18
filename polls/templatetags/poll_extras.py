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
    final_price = int(round(value - (value / 100) * discount, 0))
    return final_price
