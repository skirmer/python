# Practice page for Python course

#Chapter 3, conditional steps

def computepay(h,r):
	if h<=40:
		return h*r
	else:
		hh=h-40
		rr=r*1.5
		return (hh*rr)+(40*r)
    

hrs = raw_input("Enter Hours:")
h = float(hrs)
pay = raw_input("Enter pay per hour:")
r = float(pay)

p = computepay(h,r)
print "Pay",p