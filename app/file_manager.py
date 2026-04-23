def read_text_file(path):
  try:
    with open(path, "r", encoding="utf-8") as file:
      content = file.read()
      return content
  except Exception as e:
    print(f"Erreur lors de la lecture du fichier : {e}")
    return None


def save_text_file(path, content):
  try:
    with open(path, "w", encoding="utf-8") as file:
      file.write(content)
  except Exception as e:
    print(f"Erreur lors de l'écriture du fichier : {e}")