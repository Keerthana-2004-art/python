num=int(input('enter the number:'))
temp=num
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
print('Latest values of sum:',sum)
print('Latest values of temp:',temp)
if sum==num:
    print(num,'is armstrong number')
else:
    print(num,'is not armstrong number')
