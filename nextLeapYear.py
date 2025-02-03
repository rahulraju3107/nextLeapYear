year = int(input("Year: "))

past_leap = year % 4
years_to_next_leap = 4 - past_leap
next_leap = year + years_to_next_leap

if(next_leap % 100 == 0):
    if(next_leap % 400 != 0):
        next_leap = next_leap + 4

print(f"The next leap year after {year} is {next_leap}")