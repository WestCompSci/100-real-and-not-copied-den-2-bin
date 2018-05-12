binary = ""
denary = ""
denary = int(input("decimal number pls"))
org = denary
list = []
fliplist = []

while denary > 0:
	denary = denary//2
	rem = denary%2
	if rem <=0:
		list.append("0")
	elif rem >0:
		list.append("1")
		
#if org % 2 == 0:
#	list.append("0")
		
#elif org % 2 >0:
#	list.append("1")

fliplist = list[::]
print (fliplist)

