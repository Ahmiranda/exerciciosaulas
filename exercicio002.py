m = input("Digite um valor para caracterização: ")

a = m.isalnum()
b = m.isalpha()
c = m.istitle()
d = m.isidentifier()

print("\n é alfanumérico? {} \n é alfabético? {} \n é título? {} \n é identificador? {}".format(a,b,c,d))