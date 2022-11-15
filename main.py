from sympy.ntheory.factor_ import totient

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def Menu_EEA():
    print("first value:")
    first_value = int(input())
    print("second value")
    second_value = int(input())
    g, x, y =gcdExtended(first_value, second_value)
    print("gcd(", first_value , "," , second_value, ") = ", g)
    if (g == 1):
        print(f"{first_value} and {second_value} are coprime")
    else:
        print(f"{first_value} and {second_value} are not coprime")

def isCoprime(first_value, second_value):
    g, x, y =gcdExtended(first_value, second_value)
    print("gcd(", first_value , "," , second_value, ") = ", g)
    if (g == 1):
        print(f"{first_value} and {second_value} are coprime")
        return True
    else:
        print(f"{first_value} and {second_value} are not coprime")
        return False

def isCoprimeV2(first_value, second_value):
    g, x, y =gcdExtended(first_value, second_value)
    if (g == 1):
        print(f"phi and e are coprime")
        return True
    else:
        print(f"phi and e are not coprime")
        return False
    

def Menu_totient():
    print("Give n:")
    n = int(input())
    totient_n = totient(n)
    print("phi({}) =  {} ".format(n, totient_n))
    return totient_n

def MenuCheckE():
    print("Give e:")
    e = int(input())
    n_totient = Menu_totient()
    isCoprime(n_totient, e)

def MenuFindD():
    print("Give e:") 
    e = int(input())
    print("Give n:")
    n = int(input())
    phi = totient(n)
    g,x,y = gcdExtended(phi, e)
    if (g != 1):
        print("d doesnt exist (e and phi(n) not coprime)")
    print(f"res = {modinv(e, phi)}")
    
def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

def Menu5():
    print("Give n:")
    n = int(input())
    print("Give e:")
    e = int(input())
    phi = totient(n)
    print()

    if(isCoprimeV2(phi, e)):
        d = modinv(e, phi)
        print(f"d = {d}")
        print(f"(phi, d) = ({phi},{d})")
    else: 
        print("d doesn t exists")
        print("impossible")

def Menu6():
    print("Give n:")
    n = int(input())

    print("Do you have d ? [y/n]")
    ans = input()
    d = 0
    if (ans == "y"):
        print("Give d:")
        d = int(input())
    else:
        print("Give e:")
        e = int(input())
        d = modinv(e, totient(n))
    phi = totient(n)
    print()


    print(f"(n, d) = ({n},{d})")
    print(f"phi = {phi}")
    print()

    if(isCoprimeV2(phi, d)):
        e = modinv(d, phi)
        print(f"e = {e}")
        print(f"(phi, e) = ({phi},{e})")
    else: 
        print("e doesn t exists")
        print("impossible")
    
def Encypher():
    print("Give the plaintext m:")
    m = int(input())
    print("Give n of the sender:")
    n = int(input())

    print("Do you have e of the sender? [y/n]")
    ans = input()
    e = 0
    if (ans == "y"):
        print("Give e:")
        e = int(input())
    else:
        print("Give d:")
        d = int(input())
        e = modinv(d, totient(n))
    print()

    cyphertext = mod_power(m, e, n)
    print(f"Cyphertext = {cyphertext}")

def Decypher():
    print("Give the cyphertext c:")
    c = int(input())

    print("Give n of the receiver:")
    n = int(input())

    print("Do you have d of the receiver? [y/n]")
    ans = input()
    d = 0
    if (ans == "y"):
        print("Give d of the receiver:")
        d = int(input())
    else:
        print("Give e of the receiver:")
        e = int(input())
        d = modinv(e, totient(n))
    
    decrypted = mod_power(c, d, n)
    print(f"plaintext = {decrypted}")

def mod_power(a, n, m):
    r = 1
    while(n > 0):
        if n & 1 ==1:
            r = (r * a) % m
        a = (a * a) % m
        n >>= 1
    return r

def BuildSignature():
    print("Give signature:")
    signature = int(input())
    print("Give n of the sender:")
    n_sender = int(input())

    print("Do you have d of the sender? [y/n]")
    ans = input()
    d = 0
    if (ans == "y"):
        print("Give d of the sender:")
        d = int(input())
    else:
        print("Give e of the sender:")
        e = int(input())
        d = modinv(e, totient(n_sender))

    print("Give n of the receiver:")
    n_receiver = int(input())
    print("Give e of the receiver:")
    e = int(input())

    if (n_sender > n_receiver):
        res = mod_power(signature, e, n_receiver)
        res = mod_power(res, d, n_sender)
    if (n_receiver > n_sender):
        res = mod_power(signature, d, n_sender)
        res = mod_power(signature, e, n_receiver)
    print(f"Signature : {res}")

def CheckSignature():
    x = 0
    y = 0
    z = 0
    t = 0
    S = 0
    print("Give ciphered signature:")
    ciphered_signature = int(input())
    print("Give n_sender:")
    n_sender = int(input())
    print("Give e_sender:")
    e_sender = int(input())
    print("Give n_receiver:")
    n_receiver = int(input())

    print("Do you have d of the receiver? [y/n]")
    ans = input()
    d_receiver = 0
    if (ans == "y"):
        print("Give d_receiver:")
        d_receiver = int(input())
    else:
        print("Give e_receiver:")
        e_receiver = int(input())
        d_receiver = modinv(e_receiver, totient(n_receiver))

    if (n_sender > n_receiver):
        x = e_sender
        y = n_sender
        res = mod_power(ciphered_signature, e_sender, n_sender)
        z = d_receiver
        t = n_receiver
        res = mod_power(res, d_receiver, n_receiver)
        S = res
    elif (n_receiver > n_sender):
        x = d_receiver
        y = n_receiver
        res = mod_power(ciphered_signature, d_receiver, n_receiver)
        z = e_sender
        t = n_sender
        res = mod_power(res, e_sender, n_sender)
        S = res
    print(f"(x,y,z,t,S) = ({x},{y},{z},{t},{S})")
 
print("Choose:")     
print("Tools:")
print("1: Coprime Check via Compute Extended Euclidean algorithms")
print("2: Compute Phi(N)")
print("3: Given Phi(N), is e legitimate ?")
print("4: found d given e and Phi(n)")
print("Exercice Solver for test QCM:")
print("5: Compute (Phi(n), d) given n and e (Question 1 and 2)")
print("6. Compute (Phi(n), e) given n and d (Question 3 and 4)")
print("7. Encypher (Question 6 and 8)")
print("8. Decypher (Question 7 and 8)")
print("9. Build signature (Question 9)")
print("10. Check signature (Question 10)")
print()
print("Give a number between 1 and 10:")
selection = input()
if (selection == '1'):
    Menu_EEA()
elif (selection == "2"):
    Menu_totient()
elif (selection == "3"):
    MenuCheckE()
elif (selection == "4"):
    MenuFindD()
elif (selection == "5"):
    Menu5()
elif (selection == "6"):
    Menu6()
elif (selection == "7"):
    Encypher()
elif (selection == "8"):
    Decypher()
elif (selection == "9"):
    BuildSignature()
elif (selection == "10"):
    CheckSignature()

