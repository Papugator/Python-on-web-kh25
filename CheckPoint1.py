isDot = False #Есть ли точка в адресе почты
isAt = False #Есть ли собачка в адресе почты
isCorrect = False #Корректен ли введенный пользователем адрес
isConnected = True #Есть ли соединение с сайтом, меняется вручную
if (isConnected == True): 
    while isCorrect == False:
        mailAdress = input("Введите адрес электронной почты: ")
        if (mailAdress.find('@') > 0):
            isAt = True
        if (mailAdress.find('.') > 0):
            isDot = True
        if (isDot == True and isAt == True):
            isCorrect = True
    print("Ваш ответ записан.")
else:
    print("Нет соединения с сервером, обновите страницу")
