def rgb(r, g, b):
    hex_r = "0" + hex(0) if r <= 0 else "0" + hex(r) if r < 16 else hex(255) if r > 255 else hex(r)
    hex_g = "0" + hex(0) if g <= 0 else "0" + hex(g) if g < 16 else hex(255) if g > 255 else hex(g)
    hex_b = "0" + hex(0) if b <= 0 else "0" + hex(b) if b < 16 else hex(255) if b > 255 else hex(b)
    hex_value = hex_r + hex_g + hex_b
    hex_value = hex_value.replace("0x","").upper()
    return hex_value


print(rgb(-20,275,125))


# return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))