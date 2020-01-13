import modFunction
#docs.python.org or list of python modules 

print(modFunction.getRandomNum(10))

kilometer_num = float(input("Enter any number in Kilometers: "))
meter_num = kilometer_num*modFunction.meter_in_kilo
print (str(kilometer_num)+" km = "+str(meter_num)+" m")

# use pip command to install/uninstall modules in python Ex:" pip install python-docx"