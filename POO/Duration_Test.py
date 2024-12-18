from duration import Duration

t1 = Duration(2, 63, 120)
t2 = Duration(0,0,0,t1)
print(t1)

t1.sumar_segundos(5)
t1.sumar_minutos(10)
t1.sumar_horas(3)

print(t1)
