"""from is_weekend import is_weekend_using_calendar
from calendar_file import MyCalendar
from unittest.mock import Mock


def test_weekend():
    mock_calendar_obj = Mock()
    mock_calendar_obj.get_current_day.return_value = 6
    result = is_weekend_using_calendar(mock_calendar_obj)
    return result is True

def test_is_weekend_using_calendar_on_weekend():
    mock_calendar_obj = Mock()
    mock_calendar_obj.get_current_day.return_value = 3
    result = is_weekend_using_calendar(mock_calendar_obj)
    return result is False


def test_is_weekend_using_calendar_on_weekend2():
    calendar_obj = MyCalendar()
    result = is_weekend_using_calendar(calendar_obj)
    assert result is False
"""
"""
from unittest.mock import patch
from is_weekend import is_weekend_using_get_current_day

@patch('calendar_file.get_current_day')
def test_is_weekend_using_get_current_day_on_weekend(get_current_day_mock):
    get_current_day_mock.return_value = 6
    result = is_weekend_using_get_current_day()
    assert result is True


def test_weekend():
    with patch('get_current_day.get_current_day') as get_current_day_mock:
        get_current_day_mock.return_value = 6

        result = is_weekend_using_get_current_day()

        assert result is True


from calendar_file import MyCalendar


@patch.object(MyCalendar, 'get_current_day', return_value=6)
def test_weekend(get_current_day):
    from is_weekend import is_weekend_using_get_current_day

    result = is_weekend_using_get_current_day()

    assert result is True
"""

from unittest.mock import Mock
def test_get_count_field_from_object():
    from example import get_count_field_from_object
    attributs_obj = Mock()
    attributs_obj.get().count=3
    expected_count = 3
    count = get_count_field_from_object(attributs_obj, 1)
    assert count == expected_count

import uuid
from unittest.mock import patch
from example import MyClass
@patch.object(uuid, "uuid4", return_value=333)
def test_init_(uuid4):
    myclass = MyClass("prathap", 20)
    assert myclass.id == 333


def test_get_epoch_time_stamp_as_str():
    with patch('time.time') as time_stamp_mock:
        from example import get_epoch_time_stamp_as_str

        time_stamp_mock.return_value="3.09"
        result = get_epoch_time_stamp_as_str()
        assert result is "3.09"

@patch('requests.get')
def test_stock_price(stock_mock_obj):
    from example import get_stock_price, TimeOut
    import pytest
    stock_mock_obj.side_effect = TimeOut
    with pytest.raises(Exception) as error:
        get_stock_price(3)
    assert str(error.value) =='Request timedout'

