import sys

def main():
	if len(sys.argv) < 2:
		return
	shift = int(sys.argv[1])

	input_text = sys.stdin.read().upper()

	encoded_chars = []
	for char in input_text:
		if 'A' <= char <= 'Z':
			new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
			encoded_chars.append(new_char)


	output = ""
	for i in range(len(encoded_chars)):
		output += encoded_chars[i]
		if (i + 1) % 5 == 0:
			if (i + 1) % 50 == 0:
				output += "\n"
			else:
				output += " "

	print(output.strip())

if __name__ == "__main__":
	main()
