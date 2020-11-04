n = int(input())
m = int(input())
k = int(input())

chocArea = n * m                    # var to hold the area

if k < chocArea:                    # if the K value is smaller than the total amount of squares proceed
  if k % n == 0 or k % m == 0:      # if the modulus result of k%n or k%m equals 0 then it is divisible in some way
    print("YES")
    
  else:                             # Anything else print NO
    print("NO")

else:                               
  print("NO")