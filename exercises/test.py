print("test..");
# comment
x = 5;
if  x > 5 :
    print("x > 5");
    print("ddd")
else:
    print("x <= 5");
    print("ddd");

name = "Zoe"
print(type(x));b = "Hello, World!"
print(b[2:5]);
a,b = 5,4
print("a = ",a);
print("Hi" * 10);
print("num is %d name is %s"%(a,name) );

list = ["one", "two", "three"];
list.append("four");

map = { "one" : 1, "two" : 2, "three" : 3}
print(list[0])
# tuple immutable lists
tup =('one','two','three')
print("tup=", tup[0])
for i in tup:
    print(i)
    print("fff")
print("done for")

for i in range(0,10):
    print(i)

for i in range(0,10,2):
    print(i)

i = 0;
while ( i < 10):
    print(i)
    i = i + 1;

 # continue and break
def add(a,b):
    print("result: " , a+b)

def retadd(a,b):
    return(a+b)

add(1,2)
sum = retadd(1,2)
print("sum is ",sum)

class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age

    def getName(self):
        return(self.name)

    def getAge(self):
        return(self.age)


p = Person("Zoe",7)
print(p.getName())
