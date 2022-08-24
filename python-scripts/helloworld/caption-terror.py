text2 = input("Type in your text")
text = ("Das ist ein langer Text")
text = text2
neuertext = ("")

print(text[2])
print(len(text))
j = 0
for i in range(0,len(text)):
    j = 0
    j = i + 1
    neuertext += text[i].upper()
    neuertext += text[j].lower()

print(neuertext)