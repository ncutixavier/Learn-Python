print("-----------Exponent Function----------")
print("______________________________________")
def Exponent(base,power):
    result=1
    for i in range(power):
        result=result*base
        print(str(base)+"^"+str(i+1)+"="+str(result))
        print (result)    return result    

base_num=input("Base = ")
pow_num=input("Power = ")
Exponent(int(base_num),int(pow_num))
print("_______________________________________")