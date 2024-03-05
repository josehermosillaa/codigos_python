import  sys
import time

i = int(sys.argv[1])# permite fijar valor inicial

while i>0:
    print(i)
    time.sleep(1)
    i-=1 #iremos disminuyendo en 1

print("BOOM!") #LA BOMBA EXPLOTAAAAAA!!!!