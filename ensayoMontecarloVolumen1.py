import numpy as np

num = 10**6
u1 = np.random.uniform(0,1,num)
u2 = np.random.uniform(0,1,num)
#Funcion z = 8x + 6y con cambio de varialbe x = a + (b-a)u1 y analogo para y
z = 16*(u1**3) + 24*(u1**4)*u2
#Calculo de volumen por metodo de Monte Carlo
volumen1 = (1/num)*np.sum(z)
error1 = 2 * np.std(z) / np.sqrt(num)
interCon1 = (volumen1 - 1.96 * error1, volumen1 + 1.96 * error1)
print('------Metodo por cambio de variable-------\n')
print(f'El volumen aproximado es:{volumen1:.4f}')
print(f'El intervalo de confianza es: [{interCon1[0]:.4f},{interCon1[1]:.4f}]\n')

#Funcion Indicadora
indicadora = (u2 <= 2 * u1**2)
funcionZ = 8 * u1 + 6 * u2
volumen2 = np.mean(funcionZ * indicadora)

#Error estándar e intervalo de confianza al 95%
error2 = 2 * np.std(funcionZ * indicadora) / np.sqrt(num)
interCon = (volumen2 - 1.96 * error2, volumen2 + 1.96 * error2)

print('--------Metodo de Indicadora----------\n')
print(f'Volumen: {volumen2:.6f}')
print(f'Intervalo de confianza al 95 %: [{interCon[0]:.4f},{interCon[1]:.4f}]')