'''geneartor are function that return  a sequence of value back a geneartor function is just like any other
function but it uses a yield statement'''

def customegen(x,y):
    while x<y:
        yield x
        x+=1

result =customegen(20,30)

for i in result:print(i)

