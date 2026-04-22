def text_to_hex(text):
  char_hexa = []
  
  for char in text:
    char_hexa.append(format(ord(char), "02x"))
    
  result = " ".join(char_hexa)
  return result

print(text_to_hex("salut"))


def hex_to_text(hex_string):
  blocks = hex_string.split(" ")
  chars = []
  
  for block in blocks:
    chars.append(chr(int(block, 16)))
    
  result = "".join(chars)
  return result

print(hex_to_text("73 61 6c 75 74"))


## teste
if __name__ == "__main__":
  text = "salut"
  hex_value = text_to_hex(text)
  decoded = hex_to_text(hex_value)

print(text)
print(hex_value)
print(decoded)