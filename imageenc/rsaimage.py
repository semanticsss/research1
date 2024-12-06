import cv2
import numpy as np
import secrets
import matplotlib.pyplot as plt
import imageenc.torgb as rgb



#RSA
# STEP 1: Generate Two Large Prime Numbers (p,q) randomly
from random import randrange, getrandbits

class ImageEncryptor:

  def __init__(self):
    pass
  def power(self,a,d,n): # power lol
    # maybe tweak these numbers and parameters
    ans=1
    a = int(a)
    d = int(d)
    n = int(n)
    while d!=0:
      if d%2==1:
        ans=((ans%n)*(a%n))%n
      a=((a%n)*(a%n))%n
      d>>=1
    return ans;



  def MillerRabin(self,N,d): # this is a primality test
    a = randrange(2, N - 1)
    x=self.power(a,d,N);
    if x==1 or x==N-1:
      return True;
    else:
      while(d!=N-1):
        x=((x%N)*(x%N))%N;
        if x==1:
          return False;
        if x==N-1:
          return True;
        d<<=1;
    return False;

  def is_prime(self,N,K): # checks if prime
    if N==3 or N==2:
      return True;
    if N<=1 or N%2==0:
      return False;
    
    #Find d such that d*(2^r)=X-1
    d=N-1
    while d%2!=0:
      d/=2;

    for _ in range(K):
      if not self.MillerRabin(N,d):
        return False;
    return True;  
    
  def generate_prime_candidate(self,length): # this is good
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    # Set MSB to 1 to make sure we have an Even Number of 1024 bits.
    # Set LSB to 1 to make sure we get a Odd Number.
    p |= (1 << length - 1) | 1
    return p

  def generatePrimeNumber(self, length): # even better
    A=4
    while not self.is_prime(A, 128):
          A = self.generate_prime_candidate(length)
    return A
  
 

  #Step 3: Find E such that GCD(E,eulerTotient)=1(i.e., e should be co-prime) such that it satisfies this condition:-  1<E<eulerTotient

  def GCD(self,a,b):
    if a==0:
      return b;
    return self.GCD(b%a,a)

  


  # Step 4: Find D. 
  #For Finding D: It must satisfies this property:-  (D*E)Mod(eulerTotient)=1;
  #Now we have two Choices
  # 1. That we randomly choose D and check which condition is satisfying above condition.
  # 2. For Finding D we can Use Extended Euclidean Algorithm: ax+by=1 i.e., eulerTotient(x)+E(y)=GCD(eulerTotient,e)
  #Here, Best approach is to go for option 2.( Extended Euclidean Algorithm.)

  def gcdExtended(self, E, eulerTotient):
    a1, a2, b1, b2, d1, d2=1, 0, 0, 1, eulerTotient, E

    while d2!=1:

      # k
      k = (d1//d2)

      #a
      temp = a2
      a2 = a1-(a2*k)
      a1 = temp

      #b
      temp = b2
      b2 = b1-(b2*k)
      b1 = temp

      #d
      temp = d2
      d2 = d1-(d2*k)
      d1 = temp

      D = b2

    if D>eulerTotient:
      D=D%eulerTotient
    elif D<0:
      D=D+eulerTotient

    return D

  def temp(self, imagepath, imagepath2):

    my_img = cv2.imread(imagepath)
    if my_img is None:
        print("Error: Image not loaded. Please check the file path.")
    # cv2_imshow(my_img)
    plt.imshow(my_img)

    height, width, channels = my_img.shape
    print(f"{height} is the height of the first image.")
    print(f"{width} is the width of the first image.")
    print(f"There are {channels} channels of the first image.")
    plt.show()



    my_img2 = cv2.imread(imagepath2)
    plt.imshow(my_img2, cmap="gray")
    plt.show()
    length=15 # IMPORTANT LINE
    P=self.generatePrimeNumber(length)
    Q=self.generatePrimeNumber(length)

    print(f"{P} is the first prime number")
    print(f"{Q} is the second prime number")

    #Step 2: Calculate N=P*Q and Euler Totient Function = (P-1)*(Q-1)
    N=P*Q
    eulerTotient=(P-1)*(Q-1)
    print(f"{N} is P times Q")
    print(f"{eulerTotient} is the Euler Totient Function")
    E=self.generatePrimeNumber(4)
    while self.GCD(E,eulerTotient)!=1:
      E=self.generatePrimeNumber(4)
    print(f"{E} is a number such that GCD(E,eulerTotient)=1(i.e., e should be co-prime) such that it satisfies this condition:-  1<E<eulerTotient")
    D=self.gcdExtended(E,eulerTotient)
    
    print(f"{D} is a number such that it satisfies this property:(D*E)Mod(eulerTotient)=1")
    
    


      # defines stuff maybe idk
    row,col=my_img.shape[0],my_img.shape[1]
    enc = [[0 for x in range(3000)] for y in range(3000)]

    #Step 5: Encryption
    for i in range(100,700): # fix this to be image dimensions
      for j in range(100,1000):
        r,g,b=my_img[i,j]
        C1=power(r,E,N) # % 256
        C2=power(g,E,N) # % 256
        C3=power(b,E,N) # % 256
        enc[i][j]=[C1,C2,C3]
        C1=C1%256
        C2=C2%256
        C3=C3%256
        my_img[i,j]=[C1,C2,C3]

    plt.imshow(my_img, cmap="gray")
    plt.show()

    final = rgb.torgb(my_img)
    

    return final

