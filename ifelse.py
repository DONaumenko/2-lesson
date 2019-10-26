age = int(input('Input your age: '))

if age < 18:
    print('Ждем тебя в школе')
else:
    print('Ты уже не в школе')
    print('Иди в универ')
    why = input('Почему ты хочешь в школу')
    print(why)

print('end')