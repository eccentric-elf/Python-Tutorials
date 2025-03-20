n = int(input("Enter the number of elements: "))

evn_cnt = 0
odd_cnt = 0

for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        evn_cnt += 1
    else:
        odd_cnt += 1

print(f"Even numbers: {evn_cnt}")
print(f"Odd numbers: {odd_cnt}")
