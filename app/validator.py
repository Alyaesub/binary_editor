def is_valid_hex(hex_string):
    if not hex_string:
        return False

    blocks = hex_string.split()

    for block in blocks:
        if len(block) != 2:
          return False

        try:
            int(block, 16)
        except:
            return False

    return True