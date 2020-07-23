"""
def is_weekend_using_calendar(calendar_obj):
    day_as_number = calendar_obj.get_current_day()
    return day_as_number in [6, 7]
"""

def is_weekend_using_get_current_day():
    from calendar_file import MyCalendar
    calendar_obj = MyCalendar()
    day_as_number = calendar_obj.get_current_day()
    return day_as_number in [6, 7]

