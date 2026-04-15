import random
print("Добрый день")
start_playing = input("Хотите сыграть в игру? Да/Нет?")
while True:
    if start_playing == "Да":
        print("Отлично, давайте начнем")
        print("Загадываю число от 1 до 10, а вы должны его отгадать")
    else:
        print("Всего хорошего")
        break
    randomat = random.randint(1, 10)
    num = 0
    while num < 3:
        try:
            answer = int(input(f"У вас осталось {3 - num} попыток"))
        except ValueError:
            print("Нельзя вводить буквы")
            continue
        if answer == randomat:
            ans = ["Ура вы победили", "Вы такой молодец это правильный ответ", "У вас явно есть дар ясновидещего"]
            random_number = random.choice(ans) 
            print(random_number)
            break
        else:
            num += 1
    if num == 3:
        print("Вы проиграли")
    more_one = input("Хотите сыграть еще раз?")
    if more_one =="Нет":
        break


    
    


    