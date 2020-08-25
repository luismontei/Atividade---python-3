n1 = float ( input ( "digite o 1º numero " ))
n2 = float ( input ( "digite o 2º numero " ))
n3 = float ( input ( "digite o 3º numero " ))
n4 = float ( input ( "digite o 4º numero " ))
n5 = float ( input ( "digite o 5º numero " ))
if ( n1>n2 ) and (n1>n3) and (n1>n4 ) and (n1>n5):
	print( "o maior numero é o 1º {}".format(n1))
if (n2>n1) and (n2>n3) and (n2>n4) and (n2>n5):
	print( "o maior numero é o 2º{}".format(n2) )
if ( n3>n2) and (n3>n1) and (n3>n4) and (n3>n5):
	print( "o maior numero é o 3º {}".format(n3))
elif (n4>n2) and (n4>n3) and (n4>n1) and (n4>n5):
	print( "o maior numero é o 4º {}".format(n4) )
else:
	print( "o maior numero é o 5º {}".format(n5))