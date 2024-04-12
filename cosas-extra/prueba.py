def count_up_to(n):
    count = 0
    while count <= n:
        yield count
        count += 1

for number in count_up_to(4):
    print(number)
