text = input("Enter your text: ")

words = text.split()
characters = len(text)
characters_no_spaces = len(text.replace(" ", ""))
lines = len(text.splitlines())

print("\n===== WORD COUNTER =====")
print("Words              :", len(words))
print("Characters         :", characters)
print("Characters (no spaces):", characters_no_spaces)
print("Lines              :", lines)
print("========================")