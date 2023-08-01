while True:
  kol = 0
  vsego = 5

  otv = input("В каком году родился Пушкин?") #Правильный ответ 1799
  if otv == "1799":
      print("Верно")
      kol = kol + 1
  else:
      print("Не верно")

  otv = input("В каком году родился Лермонтов?") #Правильный ответ 1814
  if otv == "1814":
      print("Верно")
      kol = kol + 1
  else:
      print("Не верно")

  otv = input("В каком году родился Чехов?") #Правильный ответ 1860
  if otv == "1860":
      print("Верно")
      kol = kol + 1
  else:
      print("Не верно")

  otv = input("В каком году родился Толстой?") #Правильный ответ 1828
  if otv == "1828":
      print("Верно")
      kol = kol + 1
  else:
      print("Не верно")

  otv = input("В каком году родился Гоголь?") #Правильный ответ 1809
  if otv == "1809":
      print("Верно")
      kol = kol + 1
  else:
      print("Не верно")

  print(kol," верных ответов из ", vsego)

  proc = int(kol) * 100 / int(vsego)
  proc_pravilno = round(proc, 2)
  proc_nepravilno = 100 - proc_pravilno
  print (f"Правильных ответов: {proc_pravilno}%")
  print(f"Неправильных ответов: {proc_nepravilno}%")

  repit = input("Желаете повторить игру? (Введите 'да' для повтора): ")
  if repit != 'да':
    break