A= input('enter the month of year where march is 1 and february is 12')
B= input('day of the month 1-31')
C= input('year of century eg 89 for 1989 ,note if month is january or february write preceeding year ')
D= input ('centutry ')

W = (13*A-1)/5
X= C/4
Y= D/4
Z = W + X + 7 + C -2*D
R = Z%7

if R == 0:
    print 'Sunday'

elif R== 1:
    print 'Monday'

elif R== 2:
    print 'Tuesday'

elif R== 3:
    print 'Wednesday'

elif R== 4:
    print 'Thursday'

elif R== 5:
    print 'Friday'

elif R== 6:
    print 'Saturday'

else :
    print 'error'
