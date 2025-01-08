#pip install base58
#pip intall base64

import base64
import base58
import sys
import binascii

#𐍄𝖔𝖔𝖑 𝖉𝖊 𝓒𐍄𐍆 𝖊𝖑𝖆𝖇𝖔𝖗𝖆𝖉𝖆 𝖕𝖔𝖗 ☧𝖆𝖚𝖑𝖔 ↁ𝖚𝖆𝖗♱𝖊 𝖊𝖒 𝖈𝖔𝖓Ĵ𝖚𝖓♱𝖔 𝖈𝖔𝖒 Ш𝖎𝖑𝖑𝖎𝖆𝖒 𐌰𝖒𝖔𝖗𝖎𝖒
#ↁê 𝖔𝖘 𝖈𝖗é𝖉𝖎♱𝖔𝖘 𝖘𝖊 ⨍𝖔𝖗 𝖚♱𝖎𝖑𝖎ʓ𝖆𝖗. ℒ𝖎𝖛𝖗𝖊 𝖕𝖆𝖗𝖆 𝖒𝖔𝖉𝖎⨍𝖎𝖈𝖆çã𝖔 𝖊 𝖚𝖕𝖌𝖗𝖆𝖉𝖊.

print('''

                    .00.   .00.
                    00000000000
                   .00000000000.
                   :00000000000:
                   0000000000000
                  .0000000000000.
              .´._               _.`.
         .;/000000000000000000000000000|\;.
      <000000000000000000000000000000000000>
          `````¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨´´´´´´
          /////| \HACKERSECURITY/ ||||||\.
      .;//////||\ `^^^´   `^^^´  /||||||||\;.
    `````^^:\||||\.             .//////:^´´´´´
            `\||||\.           ./////´´
           .;|\||||||\.     .///////|;.
                `^\|||||\ //////^´
                   ``\||\| ////´
                        `///´
                         ´´
                         ´

       ||||||||||||           ||||||||||||
       ||| |||| |||           |||  ____|||
       |||      |||           |||____  |||
       ||| |||| |||           |||      |||
       ||||||||||||           ||||||||||||

1- 𐌱𝖆𝖘𝖊64
2- 𝓒𝖎⨍𝖗𝖆 𝖉𝖊 𝓒é𝖘𝖆𝖗
3- 𝓥𝖎𝖌𝖊𝖓è𝖗𝖊
''')

escolha = input("ↁ𝖎𝖌𝖎♱𝖊 𝖔 𝖓ú𝖒𝖊𝖗𝖔 𝖈𝖔𝖗𝖗𝖊𝖘𝖕𝖔𝖓𝖉𝖊𝖓♱𝖊 à ♱𝖔𝖔𝖑 𝖉𝖊𝖘𝖊Ĵ𝖆𝖉𝖆: ")


if escolha == '1':
	try:
		import base58
	except ImportError:
		base58 = None
		print("Base58 𝖗𝖊𝖖𝖚𝖊𝖗 𝖔 𝖒ó𝖉𝖚𝖑𝖔 'base58'. 𐌹𝖓𝖘♱𝖆𝖑𝖊 𝖈𝖔𝖒 'pip install base58'.")


	while True:
		print('''
		1- 𐌱𝖆𝖘𝖊64
		2- 𐌱𝖆𝖘𝖊58
		3- 𐌱𝖆𝖘𝖊32
		0- 𐍃𝖆𝖎𝖗
		''')
		escolha_base = input("ↁ𝖎𝖌𝖎♱𝖊 𝖆 𝖔𝖕çã𝖔 𝖈𝖔𝖗𝖗𝖊𝖘𝖕𝖔𝖓𝖉𝖊𝖓♱𝖊: ")


		if escolha_base == '0':
			print("𐌴𝖓𝖈𝖊𝖗𝖗𝖆𝖓𝖉𝖔...")
			break


		if escolha_base not in ['1', '2', '3']:
			print("𐍉𝖕çã𝖔 𝖎𝖓𝖛λ𝖑𝖎𝖉𝖆, ♱𝖊𝖓♱𝖊 𝖓𝖔𝖛𝖆𝖒𝖊𝖓♱𝖊.")
			continue


		while True:
			texto = input("\nↁ𝖎𝖌𝖎♱𝖊 𝖔 ♱𝖊𝖝♱𝖔 𝖔𝖚 𝖛𝖆𝖑𝖔𝖗 𝖕𝖆𝖗𝖆 𝖈𝖔𝖓𝖛𝖊𝖗𝖘ã𝖔 (𝖔𝖚 𝖕𝖗𝖊𝖘𝖘𝖎𝖔𝖓𝖊 𐌴𝖓♱𝖊𝖗 𝖕𝖆𝖗𝖆 𝖛𝖔𝖑♱𝖆𝖗): ")
			if texto == "":
				break

			print("[0] 𝓒𝖔𝖓𝖛𝖊𝖗♱𝖊𝖗 ♱𝖊𝖝♱𝖔 𝖕𝖆𝖗𝖆 𝖇𝖆𝖘𝖊")
			print("[1] 𝓒𝖔𝖓𝖛𝖊𝖗♱𝖊𝖗 𝖉𝖊 𝖇𝖆𝖘𝖊 𝖕𝖆𝖗𝖆 ♱𝖊𝖝♱𝖔")
			escolha_tipo = input("ↁ𝖎𝖌𝖎♱𝖊 𝖆 𝖔𝖕çã𝖔 𝖈𝖔𝖗𝖗𝖊𝖘𝖕𝖔𝖓𝖉𝖊𝖓♱𝖊: ")

			if escolha_tipo not in ['0', '1']:
				print("𐍉𝖕çã𝖔 𝖎𝖓𝖛λ𝖑𝖎𝖉𝖆, 𝖘𝖔𝖒𝖊𝖓♱𝖊 0 𝖔𝖚 1.")
				continue

			try:
				if escolha_base == '1':  # Base64
					if escolha_tipo == '0':  # Texto para Base64
						resultado = base64.b64encode(texto.encode()).decode()
					else:  # Base64 para Texto
						resultado = base64.b64decode(texto.encode()).decode()

				elif escolha_base == '2':  # Base58
					if not base58:
						print("𐌱𝖆𝖘𝖊58 𝖓ã𝖔 𝖊𝖘♱λ 𝖉𝖎𝖘𝖕𝖔𝖓í𝖛𝖊𝖑. 𐌹𝖓𝖘♱𝖆𝖑𝖊 𝖔 𝖒ó𝖉𝖚𝖑𝖔 'base58'.")
						break
					if escolha_tipo == '0':  # Texto para Base58
						resultado = base58.b58encode(texto.encode()).decode()
					else:  # Base58 para Texto
						resultado = base58.b58decode(texto.encode()).decode()

				elif escolha_base == '3':  # Base32
					if escolha_tipo == '0':  # Texto para Base32
						resultado = base64.b32encode(texto.encode()).decode()
					else:  # Base32 para Texto
						resultado = base64.b32decode(texto.encode()).decode()

				print(f"𐍂𝖊𝖘𝖚𝖑♱𝖆𝖉𝖔: {resultado}")

			except (binascii.Error, ValueError) as e:
				print("𐌽ã𝖔 ⨍𝖔𝖎 𝖕𝖔𝖘𝖘í𝖛𝖊𝖑 𝖈𝖔𝖓𝖛𝖊𝖗♱𝖊𝖗.")
				identificada = False

				if escolha_tipo == '1':  # Tentar identificar base ao decodificar
					try:
						base64.b64decode(texto.encode())
						print("𐍄𝖊𝖓♱𝖊 𝖆 𝖇𝖆𝖘𝖊64.")
						identificada = True
					except binascii.Error:
						pass

					if base58:
						try:
							base58.b58decode(texto.encode())
							print("𐍄𝖊𝖓♱𝖊 𝖆 𝖇𝖆𝖘𝖊58.")
							identificada = True
						except (binascii.Error, ValueError):
							pass

					try:
						base64.b32decode(texto.encode())
						print("𐍄𝖊𝖓♱𝖊 𝖆 𝖇𝖆𝖘𝖊32.")
						identificada = True
					except binascii.Error:
						pass

				if not identificada:
					print("☧𝖗𝖔𝖛𝖆𝖛𝖊𝖑𝖒𝖊𝖓♱𝖊 𝖆 ⨍𝖗𝖆𝖘𝖊 𝖊𝖘♱λ 𝖊𝖒 𝖚𝖒 ♱𝖎𝖕𝖔 𝖉𝖎⨍𝖊𝖗𝖊𝖓♱𝖊 𝖉𝖊 𝖊𝖓𝖈𝖔𝖉𝖆𝖒𝖊𝖓♱𝖔.")

			except Exception as e:
				print(f"𐌴𝖗𝖗𝖔 𝖉𝖊𝖘𝖈𝖔𝖓𝖍𝖊𝖈𝖎𝖉𝖔: {e}")




elif escolha == '2':
	def generate_pattern(start_word, num_lines):
		words = start_word.split()
		for i in range(num_lines):
			line = ""
			for word in words:
				line += "".join([chr((ord(letter) - ord('A') + i) % 26 + ord('A')) if letter.isupper() else 
								 chr((ord(letter) - ord('a') + i) % 26 + ord('a')) if letter.islower() else 
								 chr((ord(letter) - ord('0') + i) % 10 + ord('0')) if letter.isdigit() else letter for letter in word]) + " "
			print(line.rstrip())

	while True:
		start_word = input("ↁ𝖎𝖌𝖎♱𝖊 𝖆 𝖕𝖆𝖑𝖆𝖛𝖗𝖆 𝖎𝖓𝖎𝖈𝖎𝖆𝖑: ")
		num_lines = int(input("ↁ𝖎𝖌𝖎♱𝖊 𝖔 𝖓ú𝖒𝖊𝖗𝖔 𝖉𝖊 𝖑𝖎𝖓𝖍𝖆𝖘: "))

		generate_pattern(start_word, num_lines)







elif escolha == '3':
	print('''
	1- 𝓒𝖔𝖉𝖎⨍𝖎𝖈𝖆𝖗
	2- ↁ𝖊𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆𝖗
	''')

	while True:
		escolha = input("ↁ𝖎𝖌𝖎♱𝖊 𝖔 𝖓ú𝖒𝖊𝖗𝖔 𝖈𝖔𝖗𝖗𝖊𝖘𝖕𝖔𝖓𝖉𝖊𝖓♱𝖊 à ⨍𝖚𝖓çã𝖔: ")

		if escolha == '1':
			text = input("ↁ𝖎𝖌𝖎♱𝖊 𝖔 ♱𝖊𝖝♱𝖔 𝖆 𝖘𝖊𝖗 𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆𝖉𝖔: ")
			key = input("ↁ𝖎𝖌𝖎♱𝖊 𝖆 𝖈𝖍𝖆𝖛𝖊 𝖉𝖊 𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆çã𝖔: ")
			encrypted_text = ""
			key = key.upper()
			key_index = 0

			for char in text:
				if char.isalpha():
					shift = ord(key[key_index % len(key)]) - ord('A')
					if char.isupper():
						encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
					else:
						encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
					key_index += 1
				else:
					encrypted_char = char
				encrypted_text += encrypted_char

			print("𐍄𝖊𝖝♱𝖔 𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆𝖉𝖔:", encrypted_text)

		elif escolha == '2':
			text = input("ↁ𝖎𝖌𝖎♱𝖊 𝖔 ♱𝖊𝖝♱𝖔 𝖆 𝖘𝖊𝖗 𝖉𝖊𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆𝖉𝖔: ")
			key = input("ↁ𝖎𝖌𝖎♱𝖊 𝖆 𝖈𝖍𝖆𝖛𝖊 𝖉𝖊 𝖉𝖊𝖈𝖔𝖉𝖎⨍𝖎𝖈𝖆çã𝖔: ")
			decrypted_text = ""
			key = key.upper()
			key_index = 0

			for char in text:
				if char.isalpha():
					shift = ord(key[key_index % len(key)]) - ord('A')
					if char.isupper():
						decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
					else:
						decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
					key_index += 1
				else:
					decrypted_char = char
				decrypted_text += decrypted_char

			print("Texto decodificado:", decrypted_text)

		else:
			print("𐌴𝖘𝖈𝖔𝖑𝖍𝖆 𝖎𝖓𝖛λ𝖑𝖎𝖉𝖆. 𐍄𝖊𝖓♱𝖊 𝖓𝖔𝖛𝖆𝖒𝖊𝖓♱𝖊.")

