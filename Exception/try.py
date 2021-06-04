'''
else block is executed only if no exception is thrown
finally block is always executed whether or not exception thrown
'''
import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
try:
    f = open("myfile","w")
    a, b = [int(x) for x in input("Enter the two number").split()]
    logging.info("Division in progress")
    c = a / b
    f.write("Writing to file %d" %c)
    print(c)

except ZeroDivisionError:
    print("Division by zero not allowed. Please enter a non zero number")
    logging.error("Division by Zero")

else:
    print("You have entered a non zero number")

finally:
    f.close()
    print("file is closed")

print("After handling Exception")
