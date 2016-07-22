#Calcula o tempo aproximado em horas para chegar em um destino, com base na distância e na velocidade média.
d = float(input('Distância em km: '))
v = float(input('Velocidade média em km/h: '))
t = d / v
print ('Tempo aproximado em horas: %.1f' %t)
