import random

heads = 0
tails = 0

times = int(input("How many times do you want to toss? "))

for i in range(times):
    result = random.choice(["Heads", "Tails"])
    print("Toss", i + 1, ":", result)

    if result == "Heads":
        heads += 1
    else:
        tails += 1

print("\n===== COIN TOSS RESULTS =====")
print("Total Tosses:", times)
print("Heads:", heads)
print("Tails:", tails)
print("=============================")