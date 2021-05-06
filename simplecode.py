import sys

shift = int(sys.argv[1])

message=input()

print (shift)

print(message.upper())

message = message.upper()
for letter in message:
    if not letter.isalpha():
      continue
    offset = 65
    ord('A') = 65 
    pi = ord(letter) - offset
    ci = (pi + k) % 26
    message.append(chr(ci + offset))
return message
    