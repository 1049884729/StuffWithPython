

name=input("what is your name?")
age  =int(input("how old are you?"))
if name =='Alice':
    print("Hi, ALice")
elif age <12:
    print("You are not Alice ,Kiddo")
elif age >2000:
    print("Unlike you,Alice  is not anundead,immortal vampire.")
elif age >100:
     print("You are not Alice ,grannie")
else:
    print("You age is %s"%age)

keys=["a","b"]
values=["a_values","b_values"]
for key,values in zip(keys,values):
    print("key:%r,values:%r"%(key,values))

