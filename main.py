myFile = open('file','a',encoding='utf-8')

lastName = input('Фамилия: ')
firstName = input('Имя: ')
middleName = input('Отчество: ')
fio = lastName + ' ' + firstName + ' ' + middleName + '\n'

myFile.write(fio)
myFile.close()
 
