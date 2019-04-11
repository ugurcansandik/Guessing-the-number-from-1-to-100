from random import randint
from time import clock

a=randint(1,100)

b=int(input("In order to find the number, please enter your guess.\n"))
c=(clock())

while a!=b:
    if b<a:
        b=int(input("Enter a larger number.\n"))
    else:
        b=int(input("Enter a smaller number.\n"))
        
sure=c-clock()
if c<10:
    print("Congratulations, you found the number in an incredibly short time like ", c,". You're too good :)")
elif c>10 and c<25:
    print("Congratulations, you found the number as good as time like ", c,". You can do better if you keep your hand up.")
else:
    print("Congratulations, you found the number, but you have a speed equivalent to the speed of a turtle.")
