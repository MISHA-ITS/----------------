# Завдання 1

# Маємо два текстові файли.
# З'ясуйте, чи співпадають їхні рядки.
# Якщо ні, то виведіть із кожного файлу рядок, який не співпадає. 

with open("test.txt", "r") as file,open("test1.txt", "r") as file1, open("task1.txt", "w") as file2:
  for line in file:
    if line not in file1.read():
      file2.write(line)

# Завдання 2

# Маємо текстовий файл.
# Створіть новий файл і запишіть до нього наступну статистику за вихідним файлом:

# •	кількість символів;
with open("test.txt", "r") as file, open("task2_total.txt", "w") as file2:
    count = 0
    for line in file:
        count += len(line)-1 #програма рахує перенос рядка (\n) як символ, тому -1
    count+=1 #в останньому рядку перенос (\n) відсутній, тому +1
    print('Count of symbols = ', count)
    file2.write (f"Count of symbols = {count}")

# •	кількість рядків;
with open("test.txt", "r") as file, open("task2_total.txt", "a+") as file2:
    count = len(file.readlines())
    print('Count of lines = ', count)
    file2.write (f"\nCount of lines = {count}")

# •	кількість голосних літер(для кирилиці);
with open("test.txt", "r") as file, open("task2_total.txt", "a+") as file2:
    count = 0
    vowels = "АаЕеИиІіОоУуЄєЮюЯя"
    for line in file:
        for symbol in line:
            if symbol.isalpha and symbol in vowels:
                print(symbol, end=", ")
                count+=1
    print('\nCount of vowels = ', count)
    file2.write (f"\nCount of vowels = {count}")

# •	кількість приголосних літер (для кирилиці);
with open("test.txt", "r") as file, open("task2_total.txt", "a+") as file2:
    count = 0
    consonants = "БбВвГгҐґДдЖжЗзКкЛлМмНнРпРрСсТтФфХхЦцЧчШшЩщ"
    for line in file:
        for symbol in line:
            if symbol.isalpha and symbol in consonants:
                print(symbol, end=", ")
                count+=1
    print('\nCount of consonants = ', count)
    file2.write (f"\nCount of consonants = {count}")

# •	кількість цифр.
with open("test.txt", "r") as file, open("task2_total.txt", "a+") as file2:
    count = 0
    digits = "0123456789"
    for line in file:
        for symbol in line:
            if symbol in digits:
                count += 1
                print(symbol, end=", ")
    print('\nCount of digits = ', count)
    file2.write (f"\nCount of digits = {count}")
    
# Завдання 3

# Маємо текстовий файл.
# Видаліть з нього останній рядок.
# Результат запишіть до іншого файлу. 

with open("test.txt", "r") as file, open("task3.txt", "w") as file2:
    temp = (file.readlines())
    temp = temp[:-1]
    for line in temp:
        file2.write(line)

# Завдання 4

# Маємо текстовий файл.
# Знайдіть довжину найдовшого рядка.

with open("test.txt", "r") as file:
    count = 0
    for line in file:
        if len(line) > count:
            count = len(line)
    print(f"Max line of file has {count} symbols.")

# Завдання 5

# Маємо текстовий файл.
# Підрахуйте кількість заданого користувачем слова у ньому.

word=input("\tEnter your word: ")
with open("test.txt", "r") as file:
  count = 0
  for line in file:
    if word in line:
      count += 1
print(f"The word \"{word}\" is found {count} times in the file.")

# Завдання 6

# Маємо текстовий файл.
# Знайдіть і замініть у ньому задане слово.
# Яке слово шукати і на яке замінювати – встановлюється користувачем.

word1=input("\tEnter your word to replace: ")
word2=input("\tEnter your word to replace with: ")
with open("test.txt", "r") as file, open("task6.txt", "w") as file2:
    temp = file.read()
    temp = temp.replace(word1, word2)
    file2.write(temp)