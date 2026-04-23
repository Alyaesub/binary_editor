from converter import text_to_hex, hex_to_text
from validator import is_valid_hex
from file_manager import read_text_file, save_text_file

def main():
  text = read_text_file("tests/sample.txt")
  
  if not text:
    print("Aucun texte lu.")
    return
  
  hex_value = text_to_hex(text)
  print("Text lu :")
  print(text)
  
  print("\nHexa :")
  print(hex_value)
  
  if not is_valid_hex(hex_value):
    print("Hexa invalide")
    return
  
  decoded = hex_to_text(hex_value)
  print("\nTexte reconverti :")
  print(decoded)
  
  save_text_file("tests/test_output.txt", decoded)

if __name__ == "__main__":
  main()