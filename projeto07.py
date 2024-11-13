from InquirerPy import prompt

num=[
  {
    "type": "list",
    "message": "Escolha um numero entre 0-10",
    "name":"num",
    "choices":[1,2,3,4,5,6,7,8,9,10]
  }
]

num2=[
  {
    "type": "list",
    "message": "Escolha um numero entre 0-10",
    "name":"num2",
    "choices":[1,2,3,4,5,6,7,8,9,10]
  }
]

calculo = [
    { 
        "type": "list",
        "message": "Escolha um operador aritmético",
        "name":"operador",
        "choices": ["+", "-", "*", "/"]
    }
]

num = prompt(num)["num"]
num2 = prompt(num2)["num2"]
escolha = prompt(calculo)
operador = escolha["operador"]

if operador == "+":
  soma=(num+num2)
  print(f"o resultado é {soma}")
elif operador=="-":
  sub=(num-num2)
  print(f"o resultado é {sub}")
elif operador=="*":
  mult=(num*num2)
  print(f"o resultado é {mult}")
elif operador=="/":
  divi=(num%num2)
  print(f"o resultado é {divi}")
else:
  print("Digite um operador aritmético")