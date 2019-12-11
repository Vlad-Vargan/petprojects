from random import choice


a=["ебанутый","ёбаный","пиздатый","хуёвый","грёбаный"]
b=["рэпер","флоу","блант","рэп","братик"]
c=["базарить","пиздеть","ебашить","ебать","проёбывать"]
d=["похуй","нахуй","нахер","типа","дохуя","убъют"]
e=["блять","воу","слышь","йоу","окей","мышь","йес"]

r = "выть награда драка приглашать веселье пнул батон гад битва истина братец лишать зритель заплатить теряться леди кепка рэпчик мэн ебашить стул замес студия нрав ноздря мутить пробка обойма кент пост убиваться панч потухать айфон салют почерк движ поступок музло борт вата"
f = r.split(" ")
print("\n")

st0=[]
st1=[]

for j in range(4):
    st0.append(choice(a+b+c+d+e+f))
    st1.append(choice(a+b+c+d+e+f))
print(" ".join(st0),"\n")
print(" ".join(st1),"\n")

for i in a+b+c+d+e+f:
    riph0 = i
    if riph0[-2:] == st0[-1][-2:] and riph0!=st0[-1]:
        break

for i in a+b+c+d+e+f:
    riph1 = i
    if riph1[-2:] == st1[-1][-2:] and riph1!=st1[-1]:
        break

st0.clear()
st1.clear()


for j in range(3):
    st0.append(choice(a+b+c+d+e+f))
    st1.append(choice(a+b+c+d+e+f))
st0.append(riph0)
st1.append(riph1)

print(" ".join(st0),"\n")
print(" ".join(st1),"\n")

st0.clear()
st1.clear()