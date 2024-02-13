number_of_pages_of_book = int(input())
number_of_pages_for_hour_read = int(input())
number_of_days = int(input())

time_to_read_book = (number_of_pages_of_book / number_of_pages_for_hour_read)
total_reading_time = time_to_read_book // number_of_days
print(total_reading_time)
