words = ""

while True:
    a = input("Введіть рядок, розділений пробілами: ")
    if len(a) == 0:
        break
    words += a + " "

words = words.rstrip()

sp = words.split(" ")

unique_words = []

for word in sp:
    if not word in unique_words:
        unique_words.append(word)

unique_line = " ".join(unique_words)

print(unique_line)   
    