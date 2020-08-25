n1=int(input("digite um número: "))
n2=int(input("digite outro número: "))
while n2<n1:
	n1=int(input("digite um número: "))
	n2=int(input("digite outro número: "))
else:
	for i in range(n1,n2,1):
		print(i)