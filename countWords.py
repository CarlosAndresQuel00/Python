def readText(word):
    file = open("bookHarryPotter.txt", "r", encoding="utf8")
    line = file.readline()
    while line != "XX":
        words = line.split(" ")
        for wrd in words:
            list1.append(wrd)
        line = file.readline()
    if word in list1:
        print(word + "," + str(list1.count(word)))
    file.close()

list1 = []

word = input("Enter a word to look for: ")
readText(word)