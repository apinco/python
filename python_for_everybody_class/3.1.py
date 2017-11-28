# Start functions
def computepay(h,r):

# End functions
hours = float(input("Enter hours worked:\n"))
hourly_pay_rate = float(input("Enter your hourly rate\n"))
overtime_pay_rate = hourly_pay_rate * 1.5
overtime_pay = 0
pay = 0



if (hours > 40):
    overtime_pay = (hours - 40) * overtime_pay_rate
    pay = overtime_pay + (40 * hourly_pay_rate)
else:
    pay = (hourly_pay_rate * hours)

print(pay)

