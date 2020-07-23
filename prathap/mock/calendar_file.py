
class MyCalendar:
    @staticmethod
    def get_current_day():
        import datetime
        now = datetime.datetime.now()
        return now.isoweekday()
"""
def get_current_day():
    import datetime
    now = datetime.datetime.now()
    return now.isoweekday()
"""
