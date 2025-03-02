import math
import time

number = int(input())  
delay = int(input())   
time.sleep(delay / 1000)  
result = math.sqrt(number)

print(f"Square root of {number} after {delay} milliseconds is {result}")
