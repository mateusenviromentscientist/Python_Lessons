#!/usr/bin/env python
# coding: utf-8

# # Questão 1 

# <h1>O Conceito de Salinidade</h1>
# <p>
# Como mencionado anteriormente, a água do mar contem  em seu peso 3,5 % sais, mas também gases, substâncias orgânicas e material particulado. A presença  adicional dos sais influencia na maioria das propriedades físicas da água do mar (densidade, compressibilidade, ponto de congelamento, temperatura da densidade máxima) em algum grau, mas não são os fatores que os condicionam. Algumas propriedades (viscosidade, absorção de luz) não são significativamente afetada pela salinidade (detalhe: o material dissolvido e particulado afeta a absorção de luz, e de fato, essa influência é usada na maioria das aplicações ópticas). Duas propriedades que são determinadas pela quantidade de sais na água são a condutividade e a pressão osmótica.</p><p>
# 
# Numa maneira ideal, a salinidade deveria se a soma de todos os sais dissolvidos em gramas por cada quilograma de água. Na prática, isso é uma coisa difícil de medir. A constatação que - não importando quanto sal existe em uma parcela de água do mar - os vários componentes contribuem em uma razão ou proporção fixa, ajuda a solucionar as dificuldades. Essa fato permite a determinação do conteúdo em sal pela medida de uma quantidade substituta e o cálculo de material total  a partir dessa medida.</p><p>
# 
# A determinação da salinidade pode ser assim feita através da medida de seu componente mais importante, que é o cloreto. O conteúdo em cloreto foi definido em 1902 como a quantia total em íons cloreto em gramas presente em um quilograma de água do mar se todos os halogênios fossem substituídos por cloretos. A definição reflete no processo de titulação para a determinação de conteúdo em cloreto e é ainda tem importância quando lidamos com dados históricos.</p><p>
# 
# A salinidade foi definida em 1902 como a quantia total em gramas de todas as substâncias dissolvidas se todos os carbonatos fossem convertidos em óxidos, todos os brometos e iodetos fossem convertidos a cloretos e todas as substâncias orgânicas fossem oxidadas. A relação entre a salinidade e o conteúdo em cloretos foi estabelecida com uma série de medidas feitas em laboratório em amostras de água do mar coletadas em todas as regiões do oceano mundial e foi dada como:</p><p>
# </p><p>
# S (<sup>o</sup>/<sub>oo</sub>) = 0.03 +1.805 Cl (<sup>o</sup>/<sub>oo</sub>)  (1902)</p><p>
# </p><p>
# O símbolo<sup>o</sup>/<sub>oo</sub> significa  "partes por mil" ou"ppt"; um
# conteúdo em sal content de 3.5%  é equivalente a 35&nbsp;<sup>o</sup>/<sub>oo</sub>, or 35&nbsp;gramas de sais por quilograma de água do mar.</p><p>
# O fato de que a equação de 1902 dá um valor de salinidade igual a  0.03&nbsp;<sup>o</sup>/<sub>oo</sub> quando a cloridade é zero é um motivo de preocupação. Isso indica um problema nas amostras de água do mar usadas nas medidas de laboratório. A United Nations Scientific, Education 
# and Cultural Organization (UNESCO) decidiu repetir as análises usadas como base para essa relação inicial entre salinidade e clorinidade e introduziu uma definição nova, conhecida como <font color="#0000FF"> salinidade absoluta </font>,</p><p>
# </p><p>
# S (<sup>o</sup>/<sub>oo</sub>) = 1.80655 Cl (<sup>o</sup>/<sub>oo</sub>)  (1969)</p><p>
# </p><p>
# A definição de 1902 e 1969 dão resultados idênticos a uma salinidade de 35&nbsp;<sup>o</sup>/<sub>oo</sub> e não muda significativamente na maioria das aplicações.</p>
# [texto do link](https://incois.gov.in/Tutor/IntroOc/por/notes/lecture03.html)

# a) Para os seguintes valores de Salinidade, obtenha os respectivos valores de Clorinidade, utilizando as duas formulas citadas no texto acima. 
# 
# salinidade = [33,32.4,31.1,35,34,32.2,28.6,29,30,28.5,27,26,25,24]

# In[1]:


import numpy as np
import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# In[2]:


my_list = [33,32.4,31.1,35,34,32.2,28.6,29,30,28.5,27,26,25,24]


# In[3]:


mapped_list = list(map(lambda x:(x-0.003)/1.805, my_list))


# In[4]:


Equação_1 = [18.280886426592797, 17.94847645429363, 17.22825484764543, 19.388919667590027, 18.834903047091412, 17.83767313019391, 15.843213296398893, 16.064819944598337, 16.618836565096952, 15.787811634349032, 14.956786703601109, 14.402770083102494, 13.848753462603879, 13.294736842105264]


# In[5]:


mapped_list2 = list(map(lambda x:x/1.805, my_list)) 


# In[6]:


Equação_2 = [18.282548476454295, 17.950138504155124, 17.229916897506925, 19.390581717451525, 18.83656509695291, 17.839335180055404, 15.84487534626039, 16.066481994459835, 16.62049861495845, 15.789473684210527, 14.958448753462605, 14.40443213296399, 13.850415512465375, 13.29639889196676]


# In[7]:


salinidade = [33,32.4,31.1,35,34,32.2,28.6,29,30,28.5,27,26,25,24]


# b) Construa um gráfico 2d com os valores de Clorinidade que voce obteve, com marcadores vermelhos, e o de Salinidade com marcadores azuis.

# In[8]:


d = {'Equação_1' :[18.280886426592797, 17.94847645429363, 17.22825484764543, 19.388919667590027, 18.834903047091412, 17.83767313019391, 15.843213296398893, 16.064819944598337, 16.618836565096952, 15.787811634349032, 14.956786703601109, 14.402770083102494, 13.848753462603879, 13.294736842105264], 'Equação_2':[18.282548476454295, 17.950138504155124, 17.229916897506925, 19.390581717451525, 18.83656509695291, 17.839335180055404, 15.84487534626039, 16.066481994459835, 16.62049861495845, 15.789473684210527, 14.958448753462605, 14.40443213296399, 13.850415512465375, 13.29639889196676], 'salinidade': [33,32.4,31.1,35,34,32.2,28.6,29,30,28.5,27,26,25,24]}
df = pd.DataFrame(data=d)
columns = ['Equação_1', 'Equação_2', 'salinidade']


# In[9]:


ax1 = df.plot(kind='scatter', x='Equação_1', y='salinidade', color='r')
ax2 = df.plot(kind='scatter', x='Equação_2', y= 'salinidade', color= 'r')
print (ax1,ax2)


# b) Construa um gráfico 2d com os valores de Clorinidade obtidos a partir das duas diferentes formulas. Existe alguma diferença?

# In[10]:


Result = pd.DataFrame({'Eq_1':[18.280886426592797, 17.94847645429363, 17.22825484764543, 19.388919667590027, 18.834903047091412, 17.83767313019391, 15.843213296398893, 16.064819944598337, 16.618836565096952, 15.787811634349032, 14.956786703601109, 14.402770083102494, 13.848753462603879, 13.294736842105264],
                       'Eq_2':[18.282548476454295, 17.950138504155124, 17.229916897506925, 19.390581717451525, 18.83656509695291, 17.839335180055404, 15.84487534626039, 16.066481994459835, 16.62049861495845, 15.789473684210527, 14.958448753462605, 14.40443213296399, 13.850415512465375, 13.29639889196676]},
                     index=[33,32.4,31.1,35,34,32.2,28.6,29,30,28.5,27,26,25,24])

lines = Result.plot.line()
        


# praticamente os mesmos valores, fazendo com que os gráficos fiquem sobrexpostos

# # Questão 2 

# O Índice de Oscilação Sul (SOI) é um índice padronizado com base nas diferenças de pressão do nível do mar observadas entre o Taiti e Darwin, na Austrália. A SOI é uma medida das flutuações em larga escala na pressão do ar que ocorrem entre o Pacífico tropical ocidental e oriental (ou seja, o estado da Oscilação do Sul) durante os episódios de El Niño e La Niña. Em geral, as séries temporais suavizadas do SOI correspondem muito bem às mudanças nas temperaturas dos oceanos no Pacífico tropical oriental. A fase negativa do SOI representa pressão de ar abaixo do normal no Taiti e pressão de ar acima do normal em Darwin. Períodos prolongados de valores SOI negativos (positivos) coincidem com águas oceânicas anormalmente quentes (frias) em todo o Pacífico tropical oriental, típico dos episódios de El Niño (La Niña). Mais informações podem ser encontradas na página SOI do <a href="http://www.cpc.noaa.gov/products/analysis_monitoring/ensocycle/soi.shtml" id="anch_31">Climate Prediction Center SOI page</a>.

# Com base nessas informações, utilize o arquivo 'SOI.csv' para plotar uma série temporal com o Índice de Oscilação Sul. Como você destacaria os períodos em que temos fase positiva e negativa? Tente executar essa ideia que você teve.
# 
# Obs: As fases positivas e negativas devem ser explicitadas, por exemplo, utilizando cores diferentes para cada um dos modos.
# 

# In[11]:


dado  = pd.read_csv(r'C:/Users/ynoa_mota/Downloads/SOI.csv', names = ['Date', 'Value'], skiprows=1, parse_dates=['Date'])


# In[12]:


data =pd.date_range('1951-01', '2019-08', freq='M').strftime('%m-%Y')


# In[13]:


data


# In[14]:


fig = plt.figure(figsize=(20,10))
plt.rcParams['axes.facecolor'] = 'white'
plt.plot(dado.Date,dado.Value, color = 'black')
plt.xticks(range(0,dado.Date.size,24), data[::24], rotation=60)
plt.fill_between(dado.Date, dado.Value, where=dado.Value >=0, facecolor='b')
plt.fill_between(dado.Date, dado.Value, where=dado.Value <=0, facecolor='r')
plt.ylabel('Data', fontsize = 18)
plt.xlabel('Valor',fontsize = 18)
plt.title(u'Índice de Oscilação', color = 'black', fontsize=22)


# In[ ]:




