height=int(input ("Enter height in cm3: "))
width=int (input ("Enter width in cm3: "))
depth=int (input ("Enter depth in cm3: "))

volume= (height) * (width) * (depth)

print("volume of cube is:",volume)

if (volume<0):
    print("Enter valid dimension values")
elif (volume>=1 and volume<= 10 ):
    print("Extra Small")
elif (volume>=11 and volume<= 25 ):
    print("Small")
elif (volume>=26 and volume<= 75 ):
    print("Medium")
elif (volume>=76 and volume<= 100 ):
    print("Large")
elif (volume>=101 and volume<= 250 ):
    print("Extra Large")
else:
    print("Extra-Extra Large")
