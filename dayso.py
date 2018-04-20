n=int (input("Nhap vao n: "))
s=0
print ("Day so vua nhap: ")
for i in range(1,n+1):
	print i

for m in range(1,n+1):	
	if(m%2==0):
		s=s+m
print "Tong cac day so chan vua nhap: " ,s
		
	
