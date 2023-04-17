time=float(input ("Enter Time required for a worker to complete a job in hrs: "))

if (time<2):
    print("Enter valid value")
elif (time>=2 and time<= 3 ):
    print("highly efficient")
elif (time>=3 and time<= 4):
    print("improve speed")
elif (time>=4 and time<= 5 ):
    print("take training to improve speed")
else:
    print("leave the company")
