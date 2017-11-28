# Start functions
def computepay(h,r):
    overtime_pay_rate = r * 1.5
    pay = 0
    if (hours > 40):
        overtime_pay = (hours - 40) * overtime_pay_rate
        pay = overtime_pay + (40 * hourly_pay_rate)
    else:
        pay = (hourly_pay_rate * hours)

    return pay

# End functions
hours = float(input("Enter hours worked:\n"))
hourly_pay_rate = float(input("Enter your hourly rate\n"))

print(computepay(hours,hourly_pay_rate))

