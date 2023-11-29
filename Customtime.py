import datetime

class CustomTime:
    def __init__(self, custom_year=None, custom_month=None, custom_day=None, custom_hour=0, custom_minute=0, custom_second=0):
        if custom_year is None:
            current_custom_time = datetime.datetime.utcnow()
            self._custom_time = current_custom_time.replace(hour=custom_hour, minute=custom_minute, second=custom_second)
        else:
            self._custom_time = datetime.datetime(custom_year, custom_month, custom_day, custom_hour, custom_minute, custom_second)

    @classmethod
    def from_custom_iso_format(cls, custom_iso_string):
        try:
            custom_dt = datetime.datetime.fromisoformat(custom_iso_string)
            return cls(custom_dt.year, custom_dt.month, custom_dt.day, custom_dt.hour, custom_dt.minute, custom_dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid Custom ISO format: {custom_iso_string}") from e

    def to_custom_iso_format(self):
        return self._custom_time.isoformat()

    def to_readable_custom_format(self):
        return self._custom_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_custom_date(custom_year, custom_month, custom_day):
        try:
            datetime.datetime(custom_year, custom_month, custom_day)
            return True
        except ValueError:
            return False

    @classmethod
    def custom_date_difference(cls, custom_date1, custom_date2, unit='days'):
        if not isinstance(custom_date1, cls) or not isinstance(custom_date2, cls):
            raise ValueError("Both custom dates must be instances of CustomTime")
        
        delta = custom_date1._custom_time - custom_date2._custom_time

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return (custom_date1._custom_time.year - custom_date2._custom_time.year) * 12 + custom_date1._custom_time.month - custom_date2._custom_time.month
        else:
            raise ValueError("Invalid unit. Use 'days', 'weeks', or 'months'.")

    @staticmethod
    def custom_date_from_string(custom_date_string):
        try:
            custom_dt = datetime.datetime.strptime(custom_date_string, "%Y-%m-%d %H:%M:%S")
            return CustomTime(custom_dt.year, custom_dt.month, custom_dt.day, custom_dt.hour, custom_dt.minute, custom_dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid custom date string format: {custom_date_string}") from e

    # Properties to access individual parts of the custom datetime object
    @property
    def custom_year(self):
        return self._custom_time.year

    @property
    def custom_month(self):
        return self._custom_time.month

    @property
    def custom_day(self):
        return self._custom_time.day

    @property
    def custom_hour(self):
        return self._custom_time.hour

    @property
    def custom_minute(self):
        return self._custom_time.minute

    @property
    def custom_second(self):
        return self._custom_time.second
    
# Example usage:
# Creating instances using different methods
custom_time1 = CustomTime(2023, 1, 1, 12, 30, 45)
custom_time2 = CustomTime.from_custom_iso_format("2023-01-01T12:30:45")

# Printing in different formats
print("Custom ISO Format:", custom_time1.to_custom_iso_format())
print("This is Readable Custom Format:", custom_time1.to_readable_custom_format())

# Accessing individual parts of the custom datetime object
print("Custom Year:", custom_time1.custom_year)
print("Custom Month:", custom_time1.custom_month)
print("Custom Day:", custom_time1.custom_day)
print("Custom Hour:", custom_time1.custom_hour)
print("Custom Minute:", custom_time1.custom_minute)
print("Custom Second:", custom_time1.custom_second)

# Validating a custom date
print("Is 2023-01-01 a valid custom date or not ?", CustomTime.validate_custom_date(2023, 1, 1))
print("Is 2023-02-30 a valid custom date or not?", CustomTime.validate_custom_date(2023, 2, 30))

# Custom date difference
custom_time3 = CustomTime(2023, 1, 10)
print("Difference in custom days:", CustomTime.custom_date_difference(custom_time1, custom_time3, unit='days'))
print("Difference in custom weeks:", CustomTime.custom_date_difference(custom_time1, custom_time3, unit='weeks'))
print("Difference in custom months:", CustomTime.custom_date_difference(custom_time1, custom_time3, unit='months'))

# Creating a custom date from a string
custom_time4 = CustomTime.custom_date_from_string("2023-03-15 08:45:30")
print("Custom Date created from string:", custom_time4.to_readable_custom_format())
