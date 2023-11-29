# tests_customdatetime.py
import pytest
from custom_datetime_module import CustomDateTime

# Test creating CustomDateTime with specific arguments
def test_custom_constructor_with_arguments():
    custom_dt = CustomDateTime(2024, 2, 15, 10, 45, 30)
    assert custom_dt.custom_year == 2024
    assert custom_dt.custom_month == 2
    assert custom_dt.custom_day == 15
    assert custom_dt.custom_hour == 10
    assert custom_dt.custom_minute == 45
    assert custom_dt.custom_second == 30

# Test creating CustomDateTime with no arguments (defaults to current date and time)
def test_custom_constructor_defaults():
    custom_dt = CustomDateTime()
    now = CustomDateTime.from_iso_format(CustomDateTime().to_iso_format())
    assert custom_dt.to_iso_format().startswith(now.to_iso_format())

# Test to_custom_iso_format method
def test_custom_iso_format():
    custom_dt = CustomDateTime(2024, 2, 15, 10, 45, 30)
    assert custom_dt.to_custom_iso_format() == "2024-02-15T10:45:30"

# Test to_readable_custom_format method
def test_readable_custom_format():
    custom_dt = CustomDateTime(2024, 2, 15, 10, 45, 30)
    assert custom_dt.to_readable_custom_format() == "2024-02-15 10:45:30"

# Test validate_custom_date class method
def test_validate_custom_date():
    assert CustomDateTime.validate_custom_date(2024, 2, 15) == True
    assert CustomDateTime.validate_custom_date(2024, 4, 30) == False

# Test custom_date_difference class method
def test_custom_date_difference():
    custom_dt1 = CustomDateTime(2024, 2, 15)
    custom_dt2 = CustomDateTime(2024, 2, 25)
    assert abs(CustomDateTime.custom_date_difference(custom_dt1, custom_dt2, unit='days')) == 10

# Test custom_date_from_string static method
def test_custom_date_from_string():
    custom_dt_str = "2024-05-20 15:30:00"
    custom_dt = CustomDateTime.custom_date_from_string(custom_dt_str)
    assert custom_dt.to_readable_custom_format() == "2024-05-20 15:30:00"
