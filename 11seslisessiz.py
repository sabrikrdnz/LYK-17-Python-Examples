dize = "Yes we can"
tum = dize.count("") - dize.count(" ")
a = dize.count("a")
e = dize.count("e")
i = dize.count("i")
o = dize.count("o")
u = dize.count("u")


sesli = a + e + i + o + u
sessiz = tum - sesli - 1

print("Sesli harf sayısı:") 
print(sesli)

print("Sessiz harf sayısı:")
print(sessiz)