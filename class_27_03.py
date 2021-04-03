def count_words(file_name):
    with open(file_name, 'r') as file:
        answ = 0
        for line in file:
            line = line.strip()
            line = line.split()
            for word in line:
                word = word.strip(",./<>?;:!@#$%^&*()-=_+'" + '"')
                if len(word) % 2 == 0:
                    answ += 1
        return answ


print(count_words('lol.txt'))
