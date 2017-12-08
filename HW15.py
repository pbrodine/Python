#Homework 15
#Programmer Paul Brodine
#Date of last revision Apr 25, 2016
#Purpose  Request user input n / output nth prime under 3 mins

numb=int(input('Enter a positive integer from 1-1000000: '))
primes_list=[2,3,5,7]
possible_prime=9

while len(primes_list) < numb+1:
    for x in primes_list:
        if possible_prime % x == 0:
            possible_prime += 2
            break
    else:
        primes_list.append(possible_prime)
        possible_prime += 2
        
print(primes_list[numb-1])








    
