hexy = str("47757220636e66666a62657120766620354772384c34716574504573506b386874716a68524b385853503678325248680a")
a = 0
b = 2
final = ''
count = 0

while count < len(hexy)/2:
	print 
	print ('start count: ' + str(count))
	hexL = hexy[a:b]
	print ('hexL: ' + str(hexL))
	hexL = int(hexL, 16)
	
	if 64 < hexL < 91: 
		print ('between 40 & 91: ' + str(hexL))
		hexL = hexL + 13
		
		if hexL > 91:
			print ('< 91: ' + str(hexL))
			hexL = hexL - 90
			hexL = hexL + 64
			print ('Adding to final: ' + hex(int(hexL))[2:])
			final = final + hex(int(hexL))[2:]
			count += 1
			a += 2
			b += 2
			print ('count: ' + str(count))
			
		else:
			print ('Adding to final: ' + hex(int(hexL))[2:])
			final = final + hex(int(hexL))[2:]
			count += 1
			a += 2
			b += 2
			print ('count: ' + str(count))
	
	elif 96 < hexL < 123:
		print ('between 96 & 123: ' + str(hexL))
		hexL = hexL + 13
		
		if hexL > 122:
			print ('< 122: ' + str(hexL))
			hexL = hexL - 122
			hexL = hexL + 96
			print ('Adding to final: ' + hex(int(hexL))[2:])
			final = final + hex(int(hexL))[2:]
			count += 1
			a += 2
			b += 2
			print ('count: ' + str(count))
		
		else:
			print ('Adding to final: ' + hex(int(hexL))[2:])
			final = final + hex(int(hexL))[2:]
			count += 1
			a += 2
			b += 2
			print ('count: ' + str(count))
	
	else:
		print ('Adding to final: ' + hex(int(hexL))[2:])
		final = final + hex(int(hexL))[2:]
		count += 1
		a += 2
		b += 2
		print ('count: ' + str(count))
		
	
print
print ('The answer is: ' + final)