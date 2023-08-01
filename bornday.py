answer = input('В каком году родился А.С. Пушкин?')

if answer == '1799':
  print("Всё верно!")
  dr = input('Какого числа у него ДР?')
  if dr == '6 июня':
    print('Верно')
  else:
    print('Неверный день рождения')

else:
  print("Неверный год рождения!")

print('end')