# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")

# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	string = ""	
	for i in msg:
		if(i == " "):
			string += " "
		else:
			print(string)
			if(ord(i)<=90 and ord(i)>=65):
				val = ord(i) + shift
				if(val > 90):
					val = (val - 90) + 64
					string += chr(val)
				elif(val < 65):
					print(val)
					val = 90-(65-val)
					string += chr(val)
				else:
					string += chr(val)
					

			if(ord(i)<=122 and ord(i)>=97):
				val = ord(i) + shift
				if(val > 122):
					val = (val - 122) + 96
					string += chr(val)
				elif(val < 97):
					val = 122-(97-val)
					string += chr(val)
				else:
					string += chr(val)
	return string					

print(fun_applycaesarcipher("zodiac", -2))   						
					




