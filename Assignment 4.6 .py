# Write a program to prompt the user for hours
# and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40
# and time-and-a-half for the hourly rate for all hours worked above 40 hours.

def computepay(h, r):

	if h <= 40:
		pay = h* r
	else:
		pay = (h * r) + (h - 40.0) * (r*0.5)

	return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r=float(rate)

p = computepay(h, r)
print("Pay", p)
