#
# file = open("byron.txt", mode="r", encoding="utf-8")
# # .read() - считывает весь текс с файла
# # .readlines() - считает каждую строку сформировав список строк
# # .readline() - считает каждую строку по очереди
#
# # text = file.read()
# # text = file.readlines()
# text = file.readline()
# text = file.readline()
# text = file.readline()
# # text = file.writable()
#
# print(text)
# file.close()
#
# file = open("byron.txt", mode="r", encoding="utf-8")
# # .read() - считывает весь текс с файла
# # .readlines() - считает каждую строку сформировав список строк
# # .readline() - считает каждую строку по очереди
#
# # text = file.read()
# # text = file.readlines()
# text = file.readline()
# text = file.readline()
# text = file.readline()
# # text = file.writable()
#
# print(text)
# file.close()
#
# # запись данный в файл
#
# file2 = open('new_file.txt', mode="w", encoding="utf-8")
# # .write() - записывает тест в одну строку
# # .writelines(список_строк) - принимает список строку и записывает в файл
# # file2.write('Hello world\n')
# # file2.write('Привет мир')
#
# lines = [f'{i} строка\n' for i in range(1, 101)]
# file2.writelines(lines)
# file2.close()

# работа с бинарными файлами

# img = open('nature.jpg', mode='rb')
# content = img.read()
# print(content)
# img.close()


# with - контекстный менеджер, позволяющий не закрывать соединение

# with open('nature.jpg', mode="rb") as img:
#     content = img.read()
#     for i in range(1, 11):
#         new_img = open(f'{i}.jpg', mode="wb")
#         new_img.write(content)
#         new_img.close()
#     print(img.closed)
#
# print(img.closed)

# file2 = open('new_file.txt', mode="a", encoding="utf-8")
# lines = [f'{i} строка\n' for i in range(101, 201)]
# file2.writelines(lines)
# file2.close()