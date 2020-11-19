import urllib.request
from time import sleep

offline = True
while offline:
  try:
    response = urllib.request.urlopen('http://lad.ufcg.edu.br/loac/uploads/OAC/anon.txt')
    offline = False
    break
  except:
    print("Site offline, tentando novamente...")
    sleep(1)

def filtraNotas(notas, idAlvo):
  listaSplit = notas.split("\n")
  nota = listaSplit[0].split(" ")
  i = 0
  while (nota[0] != idAlvo):
    i += 1
    nota = listaSplit[i].split(" ")
  
  notaAluno = 0
  while(idAlvo == listaSplit[i].split(" ")[0]):
    notaAluno += int(listaSplit[i].split(" ")[2])
    i += 1
  return notaAluno

notas = response.read().decode('utf-8')
idAlvo = input("Digite o id a ser procurado: ")

print(filtraNotas(notas, idAlvo))
