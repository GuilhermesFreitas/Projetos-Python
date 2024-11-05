from math import floor  

# salário mensal
s = float(input("Digite seu salário mensal: "))  

# horas por dia
hd = float(input("Digite quantas horas você trabalha por dia: "))

# dias por semana
ds = int(input("Digite quantos dias por semana você trabalha: "))

ht = hd * ds  # horas trabalhadas por semana
semanas_mes = 4.33  # semanas em um mês
hm = floor(ht * semanas_mes)  # horas mensais

# valor por hora 
hr = s / hm

print(f"O funcionário recebe {hr:.2f} por hora trabalhada, levando em conta que recebe {s:.2f} por mês e trabalha {hm} horas mensais.")
# "." indica que estamos especificando o numero de casas decimais
# "2" siginifica que quero duas casa decimais apos o ponto.
# "f" siginifica que sera float 