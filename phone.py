phone=input("enter any number")
if (phone.isdigit()):
	if(len(phone)==8 or len(phone)==10 ):
			if (phone[0:4]=="7989"):
				print("valid jio number")
		
			elif(phone[0:4]=="9676"):
				print("valid airtel number")
			else:
				print("invalid ph number")

	else:
		print("enter 8 or 10 digits")

else:
	print("enter only digits")