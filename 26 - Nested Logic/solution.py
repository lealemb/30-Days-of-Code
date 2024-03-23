# Enter your code here. Read input from STDIN. Print output to STDOUT
actual_return_date = list(map(int, input().split()))
expected_return_date = list(map(int, input().split()))

actual_day, actual_month, actual_year = actual_return_date
expected_day, expected_month, expected_year = expected_return_date

fine = 0

if actual_year > expected_year:
    fine = 10000
elif actual_year == expected_year:
    if actual_month > expected_month:
        fine = 500 * (actual_month - expected_month)
    elif actual_month == expected_month and actual_day > expected_day:
        fine = 15 * (actual_day - expected_day)

print(fine)
