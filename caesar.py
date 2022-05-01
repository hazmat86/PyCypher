alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Welcome to PyCypher!\n')

mode = input('Please enter whether you want to encode or decode a message: ').lower()

if mode == 'encode':
	user_text = input(f'Enter the text you want to {mode}: ')
	shift = int(input('Enter the number of characters you want to shift your message: '))
	if shift > 26:
		shift = shift % 26
	def encrypt(cipher_text, shift_amount):
		final = ''
		for char in cipher_text:
			if char in alphabet:
				position = alphabet.index(char)
				new_position = position + shift_amount
				final += alphabet[new_position]
			else:
				final += char
		print(f'Your encoded message is {final}')
	encrypt(cipher_text=user_text, shift_amount=shift)

elif mode == 'decode':
	user_text = input(f'Enter the text you want to {mode}: ')
	shift = int(input('Enter the number of characters you want to shift your message: '))
	if shift > 26:
		shift = (shift % 26) 
	shift_neg = shift * -1
	def decrypt(cipher_text, shift_amount):
		final = ''
		for char in cipher_text:
			if char in alphabet:
				position = alphabet.index(char)
				new_position = position + shift_amount
				final += alphabet[new_position]
			else:
				final += char
		print(f'Your decoded message is {final}')
	decrypt(cipher_text=user_text, shift_amount=shift_neg)

else:
	print(f'I\'m sorry but {mode} is not a valid option.')

