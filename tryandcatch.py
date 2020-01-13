try:
    # vaalue = 10 / 0
    number=int(input("Injiza umubare: "))
    print(number)
# except:
#     print("Warasaze!!, wakinjije umubare...")
except ZeroDivisionError as err:
    print(err)
    # print("Yewe, uri kugabanya zero!!")
except ValueError as err:
    print(err)
    # print("Wakinjije umubare jama, cg wasaze!!!")