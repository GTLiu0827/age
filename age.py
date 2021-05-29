driving = input ('Have you ever dirve car ? : ')
if driving != 'yes' or 'no' :
	print ('Please answer yes or no')
	raise SystemExit

age = input ('What is your age ? :')

if driving == 'yes' :
   if int(age) >= 18 :
   	print ('You Pass the test')
   else :
   	print ('You should not drive car !')
elif driving == 'no':
	if int(age) >= 18 :
		print ('You should go get a license')
	else :
		print ('wait for dew more years')