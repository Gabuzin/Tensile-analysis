#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


#Gegrando Tabela 
ensaio_aço = pd.read_excel('D:/faculdade/Semestre 5/Ensaios macanicos/Relatorio 1- Tensão/T.A.AÇO.xlsx')
ensaio_inox= pd.read_excel('D:/faculdade/Semestre 5/Ensaios macanicos/Relatorio 1- Tensão/T.A.INOX.xlsx')
ensaio_FF= pd.read_excel('D:/faculdade/Semestre 5/Ensaios macanicos/Relatorio 1- Tensão/T.A.FF.xlsx')

comprimento_aço= 51,5
r_aço= 4,95
A0_aço=76,97687399

Carga_aço= ensaio_aço['Força(N)']
Alongamento_aço=ensaio_aço['Alongamento(mm)']
Tensão_aço=[]
Deformação_aço=[]
ensaio_aço.head(640)


# In[16]:


ensaio_inox.head(640)


# In[25]:


ensaio_FF.head(8)


# In[3]:


#Gerando grafico do aço
Tensão= ensaio_aço.loc[0:632,['Tensão(Mpa)']]
Deformação= ensaio_aço.loc[0:632,['Deformação(mm/mm)']]

plt.plot(Deformação, Tensão, linestyle = "-")
plt.title("Curva Tensão-Deformação de Engenharia")
plt.xlabel("Deformação(mm/mm)")
plt.ylabel("Tensão(MPa)")
plt.xlim(0, None)
plt.ylim(0, None)
plt.grid()

plt.show


# In[42]:


#Calculo modulo de young

#E=F*Lo/Dl*A
F1= ensaio_aço.loc[5,['Força(N)']]
Lo1= ensaio_aço.loc[0,['Comprimento(mm)']]
Dl1= ensaio_aço.loc[5,['Alongamento(mm)']]
A1= ensaio_aço.loc[0,['Area de secção transverssal(mm²)']]
F=float(F1)
Lo=float(Lo1)
Dl=float(Dl1)
A=float(A1)


E=((F*Lo)/(Dl*A))*10**(-3)
print('O modulo de Elasticidade é {:.3f} GPa'.format(E)) 


# In[52]:


# Gerando grafico de limite de escoamento
x=[]
y=[]
i=0
t1=ensaio_aço['Tensão /fator de ajuste']
t= ensaio_aço['Tensão(Mpa)']
d=  ensaio_aço['Deformação(mm/mm)']

#for i in range(300):
#    y.append(t1/d)
#    x.append(0.002 +(t1/d))
#    if y == x:
#        print(i)
       

plt.plot(d, t, linestyle = "-")
plt.plot(d + 0.002, t+ 0.002, linestyle= "--")
plt.xticks([0,0.02,0.04,0.06,0.08,0.1])
plt.title("Curva Tensão-Deformação de Engenharia")
plt.xlabel("Deformação(mm)")
plt.ylabel("Tensão(MPa)")
plt.xlim(0, 0.1)
plt.ylim(0, None)
plt.grid()
plt.show



# In[53]:


#Calculando Limite de Resistencia

print('Limite de Resistência =',LR,'MPa')

LR = 0
for i in range(n):
  if tensao[i] > tensao[i-1] :
    LR = tensao[i]
    LRx = alongamento[i]

print('Limite de Resistência =',LR,'MPa')    
    


# In[8]:


#Gerando Grafico do Ferro Fundido

Tensão= ensaio_FF.loc[0:632,['Tensão(Mpa)']]
Deformação= ensaio_FF.loc[0:632,['Deformação(mm/mm)']]

plt.plot(Deformação, Tensão, linestyle = "-")
plt.title("Curva Tensão-Deformação de Engenharia")
plt.xticks([0,0.02,0.04,0.06,0.08,0.1])
plt.xlabel("Deformação(mm/mm)")
plt.ylabel("Tensão(MPa)")
plt.xlim(0, None)
plt.ylim(0, None)
plt.grid()

plt.show


# In[40]:


#Calculo modulo de young FF

#E=F*Lo/Dl*A
D1= ensaio_FF.loc[300,['Deformação(mm/mm)']]
T1= ensaio_FF.loc[300,['Tensão(Mpa)']]
F1= ensaio_FF.loc[300,['Força(N)']]
Lo1= ensaio_FF.loc[0,['Comprimento(mm)']]
Dl1= ensaio_FF.loc[300,['Alongamento(mm)']]
A1= ensaio_FF.loc[0,['Area de secção transverssal(mm²)']]
D=float(D1)
T=float(T1)
F=float(F1)
Lo=float(Lo1)
Dl=float(Dl1)
A=float(A1)


E1= T/D
print('O modulo de Elasticidade é {:.2f} MPa'.format(E1))


E=((F*Lo)/(Dl*A))*10**(-3)
print('O modulo de Elasticidade é {:.3f} GPa'.format(E)) 


# In[24]:



#Grafico do Inox


Tensão= ensaio_inox.loc[0:632,['Tensão(Mpa)']]
Deformação= ensaio_inox.loc[0:632,['Deformação(mm/mm)']]

plt.plot(Deformação, Tensão, linestyle = "-")
plt.title("Curva Tensão-Deformação de Engenharia")
plt.xticks([0,0.02,0.04,0.06,0.08,0.1])
plt.xlabel("Deformação(mm/mm)")
plt.ylabel("Tensão(MPa)")
plt.xlim(0, None)
plt.ylim(0, None)
plt.grid()

plt.show


# In[41]:


#Calculo modulo de young
# E1= Tensão/ Deformação
#E=F*Lo/Dl*A
D1= ensaio_inox.loc[170,['Deformação(mm/mm)']]
T1= ensaio_inox.loc[170,['Tensão(Mpa)']]
F1= ensaio_inox.loc[170,['Força(N)']]
Lo1= ensaio_inox.loc[0,['Comprimento(mm)']]
Dl1= ensaio_inox.loc[170,['Alongamento(mm)']]
A1= ensaio_inox.loc[0,['Area de secção transverssal(mm²)']]
F=float(F1)
Lo=float(Lo1)
Dl=float(Dl1)
A=float(A1)
D=float(D1)
T=float(T1)

E1= T/D
print('O modulo de Elasticidade é {:.2f} MPa'.format(E1))

E=((F*Lo)/(Dl*A))*10**(-3)
print('O modulo de Elasticidade é {:.3f} GPa'.format(E)) 

