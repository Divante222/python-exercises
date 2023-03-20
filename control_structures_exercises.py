# Calculate a weekly paycheck, accounting for overtime pay. Create variables and make up values for:
# The number of hours worked in one week
# The hourly rate
total_pay = 0

number_of_hours_worked = input('how many hours did you work this week?')
number_of_hours_worked = int(number_of_hours_worked)


the_hourly_rate = input('what is your hourly rate')
the_hourly_rate = float(the_hourly_rate)

# For calculating pay:

# For working 40 hours or less, each hour is paid at the hourly rate
# For working more than 40 hours
if number_of_hours_worked <= 40:
    total_pay = number_of_hours_worked * the_hourly_rate
elif number_of_hours_worked > 40:
    the_extra = number_of_hours_worked - 40
    total_pay = 40 * the_hourly_rate
    total_pay = total_pay + (the_extra * (the_hourly_rate * 1.5))
print(total_pay)

# the first 40 hours are paid at the hourly rate

# each hour after 40 is paid at time and a half (hourly rate * 1.5)