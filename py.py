try:
    num1,num2= eval(input("Enter 2 numbers, seperated by a comma :"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("Division by 0 is not possible")
except SyntaxError:
    print("comma is missing , stupid")
except:
    print("Wrong input , Really...............")
else:
    print("No errors , im watching you")
finally:
    print("If this does not get executed , you are blind")