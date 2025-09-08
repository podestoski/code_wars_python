def to_roman(val : int) -> str:
    roman_mappings = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    roman_value = ""
    for rom_value, rom_symbol in roman_mappings:
        while(val >= rom_value):
            val = val - rom_value
            roman_value += rom_symbol
        if(val == 0):
            break 
    return roman_value


def from_roman(roman_num : str) -> int:
    values = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    total = 0
    for i in range(len(roman_num)):
        current_value = values[roman_num[i]]
        if i + 1 < len(roman_num) and current_value < values[roman_num[i+1]]:
            total -= current_value
        else:
            total += current_value
    return total




print(to_roman(2000))
print(from_roman("MM"))