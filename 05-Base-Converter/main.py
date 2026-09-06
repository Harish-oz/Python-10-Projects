number = input("Enter a number: ")
base = int(input("Enter its base (2, 8, 10, or 16): "))

decimal = int(number, base)

print("\n===== BASE CONVERTER =====")
print("Binary      :", bin(decimal))
print("Octal       :", oct(decimal))
print("Decimal     :", decimal)
print("Hexadecimal :", hex(decimal))
print("==========================")