number = [1, 2, 3, 4, 5]
name = ['ประสพชัย', 'สิงห์น้อย']
mix = [10, 1.2, 'mee']

print(number[4])
print(name[1])

print("สมาชิกมีทั้งหมด ", len(number))

data = []
data.append(1)
data.append(2)

print(data)

data[1] = 12

print(data)

sum=0
for num in number:
    sum += num
    print(int (sum))
