
P = int(input('Enter Prime Number P: '))
G = int(input('Enter Prime Number G: '))


a = int(input('Enter Private KeyA for Alice: '))
x = int(pow(G,a,P))

b = int(input('Enter Private KeyB for Bob: '))
y = int(pow(G,b,P))

ka = int(pow(y,a,P))

kb = int(pow(x,b,P))

print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))



