def int32_to_ip(int32):
    if(int32 == 0):
        return "0.0.0.0"
    binary_string_formatted = format(int32, 'b')
    if(len(binary_string_formatted) < 32):
        while(len(binary_string_formatted) < 32):
            binary_string_formatted = "0" + binary_string_formatted
    binaries = []
    for i in range(0, len(binary_string_formatted), 8):
        binaries.append(binary_string_formatted[i:i+8])
    ip = ""
    for bin in binaries:
        ip += str(int(bin,2)) + "."
    ip = ip[:-1]
    return ip
    
    

print(int32_to_ip(1457763694))


# return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


# from ipaddress import IPv4Address

# def int32_to_ip(int32):
#     return str(IPv4Address(int32))