#!/usr/bin/env python
# coding: utf-8

# ![%C3%ADndice.png](attachment:%C3%ADndice.png)<center>

#  ## <center>Avaliação Parcial I</center> 
#  
#   <center>VE0063 - ANÁLISE E APRESENTAÇÃO DE DADOS OCEANOGRÁFICOS </center> 
#   
#    <center>Prof. Pedro Silveira Calixto</center> 

# In[ ]:





# <center> NOME: Mateus Santos Lopes
# 
# -------------------

# # Problema 1 

# 2) O Programa Nacional de Boias (PNBOIA), tem como objetivo a coleta de dados oceanográficos e meteorológicos no Atlântico, por meio de rede de boias rastreadas por satélite, em apoio às atividades de meteorologia e oceanografia do Brasil. O dado fornecido com nome "pnboiaFOR.csv", possui apenas duas das variaveis que são amostradas pela boia fundeada em Fortaleza. 
# 
# 

# a) Leia o arquivo de texto e plote um gráfico de barras da Velocidade do vento pelo tempo (Month). (2 pontos)
# 
# dica: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


dado = pd.read_csv(r'C:\Users\Mateusin\Desktop\Python\pnboiaFOR.csv')


# In[3]:


print(dado)


# In[4]:


from pandas import DataFrame


# In[5]:


data = {'Velocidade':[ 8.102172, 7.370115,6.066405, 7.439127,8.217988, 9.545318,9.693951,10.446830,11.371559,10.453986,9.251552,8.705012],
       'Mês':[1,2,3,4,5,6,7,8,9,10,11,12]}


# In[6]:


df = DataFrame(data,columns=['Velocidade','Mês'])
df.plot(x='Mês', y= 'Velocidade', kind = 'bar', figsize=(10,5), title = 'Velocidade do Vento durante os meses')
plt.show()


# In[7]:


texto = 'Prof sem querer apaguei o enunciado do item b :(, mas sei que de acordo com o gráfico os meses de mais intensidade de vento são agosto,setembro e outubro' 


# # Problema 2

# <p><b>CTD</b> (sigla derivada do inglês: <b>c</b>onductivity, <b>t</b>emperature and <b>d</b>epth) é um instrumento <a href="/wiki/Oceanografia" title="Oceanografia">oceanográfico</a> que possui sensores para registrar <a href="/wiki/Condutividade" class="mw-disambig" title="Condutividade">condutividade</a>, <a href="/wiki/Temperatura" title="Temperatura">temperatura</a> e <a href="/wiki/Press%C3%A3o" title="Pressão">pressão</a> na coluna de água. As medidas de condutividade e pressão podem ser convertidas em <a href="/wiki/Salinidade" title="Salinidade">salinidade</a> e profundidade, respectivamente. O CTD apresenta boa exatidão e elevadas taxas de amostragem (registro de suas medidas), sendo comumente empregado na obtenção de perfis verticais de importantes variáveis físicas da <a href="/wiki/%C3%81gua_do_mar" title="Água do mar">água do mar</a>. De uma maneira geral, o instrumento possui tamanho e peso reduzidos devido aos materiais empregados na sua fabricação, como <a href="/wiki/Tit%C3%A2nio" title="Titânio">titânio</a>, <a href="/wiki/Alum%C3%ADnio" title="Alumínio">alumínio</a> e plásticos especiais.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1"><span>[</span>1<span>]</span></a></sup> O CTD utiliza sensores modulares e intercambiáveis que possuem uma grande flexibilidade na configuração do instrumento, facilitando a manutenção e calibração dos mesmos.<sup id="cite_ref-:0_2-0" class="reference"><a href="#cite_note-:0-2"><span>[</span>2<span>]</span></a></sup> <sup id="cite_ref-:1_3-0" class="reference"><a href="#cite_note-:1-3"><span>[</span>3<span>]</span></a></sup> Além dos três sensores básicos, o CTD também pode ser configurado com outros sensores a fim de medir mais parâmetros da água, como <a href="/wiki/PH" title="PH">pH</a>, <a href="/wiki/Oxig%C3%AAnio_dissolvido" class="mw-redirect" title="Oxigênio dissolvido">oxigênio dissolvido</a>, <a href="/wiki/Turbidez" title="Turbidez">turbidez</a> e <a href="/wiki/Fluoresc%C3%AAncia" title="Fluorescência">fluorescência</a>.<sup id="cite_ref-:2_4-0" class="reference"><a href="#cite_note-:2-4"><span>[</span>4<span>]</span></a></sup>
# </p>

#     a) Utilizando o arquivo "CTD_raw.cnv" construa um painel com gráficos separados das seguintes propriedades em função da profundidade ou pressão SOMENTE para os primeiros 500 metros do perfil. (2 Pontos)
#      
#     
# * Temperatura
# * Salinidade
# * Densidade (sigma-t)
# 
# Dica: Trecho do arquivo CTD_raw.cnv:
# 
# Nome de cada uma das colunas do arquivo.
# 
# * Coluna 0 = prDM: Pressure, Digiquartz [db] 
# * Coluna 1 = t068C: Temperature [ITS-68, deg C]
# * Coluna 2 = c0S/m: Conductivity [S/m]
# * Coluna 3 = depSM: Depth [salt water, m], lat = -15
# * Coluna 4 = sal00: Salinity [PSU]
# * Coluna 5 = sigma-t00: Density [sigma-t, Kg/m^3 ]
# * Coluna 6 = density00: Density [density, Kg/m^3]
# * Coluna 7 = svCM: Sound Velocity [Chen-Millero, m/s]
# * Coluna 8 = dz/dtM: Descent Rate [m/s], WS = 2
# * Coluna 9 = flag: flag
# 

# In[8]:


dado1= pd.read_csv(r'C:\Users\Mateusin\Desktop\Python\CTD_raw.cnv', names=['prDM','t068C', 'c0S/m ','depSM','sal00','sigmat00','density00','svCM','dz/dtM','flag'], delim_whitespace=True, skiprows=70)


# In[9]:


dado1[dado1 == -9.990e-29]=np.nan


# In[10]:


fig, ax = plt.subplots(3, sharex = False, gridspec_kw={'hspace': 0.4}, figsize = (14,8))
fig.patch.set_facecolor('seagreen')
plt.rcParams['axes.facecolor']='white'
ax[0].plot(dado1.t068C,dado1.prDM, label = 'Temperatura', color ='red')
ax[1].plot(dado1.sal00,dado1.prDM,label='Salinidade', color='gray')
ax[2].plot(dado1.sigmat00,dado1.prDM, label = 'Densidade', color ='k')

ax[0].set_ylim(500,0)
ax[1].set_ylim(500,0)
ax[2].set_ylim(500,0)

ax[0].set_xlabel('Temperatura')
ax[1].set_xlabel('Salinidaade')
ax[2].set_xlabel('Densidade')

ax[0].set_title('Temperatura,Salinidade e Densidade pela Pressão', fontsize = 20)


# # Problema 3

# Prediction and Research Moored Array in the Tropical Atlantic (PIRATA) é uma rede de observação <i>in situ</i> composta por boias fundeadas planejadas para monitorar uma série de variáveis dos processos de interação oceano-atmosfera no oceano Atlântico Tropical.</p><p>O projeto PIRATA é um programa de cooperação multinacional entre o Brasil, França e Estados Unidos. Estes três países dividem as tarefas de implementação e manutenção da rede.</p><p>Todos as boias fundeadas durante a parte piloto do estudo foram construídas pelo <a href="http://www.pmel.noaa.gov/"><i>Pacific Marine Environmental Laboratory</i></a> (PMEL) da <a href="http://www.noaa.gov/">NOAA</a>. Sua responsabilidade também inclui o envio, calibração e reparo dos equipamentos.</p><p>O suporte logístico para o desenvolvimento e manutenção da rede é dividida entre o Brasil e França. O Brasil é responsável pela manutenção do lado oeste da rede, e a França, do leste.</p><p>O programa PIRATA é reconhecido e recomendado pela comunidade científica e programas de clima internacionais tais como o <a href="http://www.clivar.org/">CLIVAR</a> e <a href="http://www.ioc-goos.org/">GOOS</a>.</p>

# #### A figura abaixo mostra a distribuição dessas boias no Oceano Atlântico Tropical:

# ![Captura%20de%20tela%20de%202019-10-10%2013-40-38.png](attachment:Captura%20de%20tela%20de%202019-10-10%2013-40-38.png)

#     a) O arquivo "boias_pirata.zip" contém 4 arquivos diferentes representando 4 boias que estão ilustradas no mapa. Escolha um dos arquivos e construa uma SEÇÃO de temperatura na qual os eixos são a PROFUNDIDADE(Y) e TEMPO(X). (2 pontos)
#     
#     obs: Os arquivos .cdf são iguais aos arquivos netCDF que vimos durante o curso.
# 

# In[11]:


pip install cmocean


# In[12]:


import os
os.environ['PROJ_LIB'] = r'C:\Users\Mateusin\anaconda3\Library\share\proj'
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import cmocean as cm


# In[13]:


dado = Dataset(r'C:\Users\Mateusin\Desktop\Python\t0n0e_mon.cdf')


# In[14]:


print(dado)


# In[15]:


tempo = dado['time'][:]
temperatura = dado['T_20'][:,:,0,0]
profundidade = dado['depth'][:]


# In[16]:


P,T = np.meshgrid(-profundidade,tempo) 


# In[17]:


plt.figure(figsize = (10,8),facecolor = 'cyan')
ax = plt.gca()
ax.set_facecolor

levels = np.arange(temperatura.min().min(),temperatura.max().max(), 0.04)


cf = plt.contourf(T,P,temperatura,100,cmap = cm.cm.ice, extend = 'max')
c2 = plt.contour(T,P,temperatura,colors='g',linewidths=1)

clabels = plt.clabel(c2, fontsize=10,fmt='%1.2f',colors='r',use_clabeltext=True)
plt.colorbar(cf)

plt.title(u'Seção de Temperatura', fontsize = 14)
plt.xlabel('Tempo', color='k', fontsize=12)
plt.ylabel('Profundidade')


#     b) Construa um mapa indicando a localização das boias contidas no arquivo "boias_pirata.zip". (2 pontos)

# In[18]:


dado2=Dataset(r'C:\Users\Mateusin\Desktop\Python\t0n10w_mon.cdf')
dado3=Dataset(r'C:\Users\Mateusin\Desktop\Python\t0n23w_mon.cdf')
dado4=Dataset(r'C:\Users\Mateusin\Desktop\Python\t0n35w_mon.cdf')


# In[19]:


lat1 = dado['lat'][:]
lat2 = dado2['lat'][:]
lat3 = dado3['lat'][:]
lat4 = dado4['lat'][:]


# In[20]:


lon1 = dado['lon'][:]
lon2 = dado2['lon'][:]
lon3 = dado3['lon'][:]
lon4 = dado4['lon'][:]


# In[21]:


plt.figure(figsize=(12,10))
m = Basemap(projection='merc',llcrnrlat=-70,urcrnrlat=70,            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

m.drawcoastlines()
m.fillcontinents(color='0.4')
m.drawcountries(color='0.1')
m.drawmapboundary(fill_color='c')

m.drawparallels(np.arange(-60,60 +10,10),labels=[1,0,0,1],
                linewidth = 0,fontsize = 8 , fontweight = 'bold') 
m.drawmeridians(np.arange(-360,360,30),labels=[1,1,0,1],
                linewidth = 0 ,fontweight='bold')

m.plot(lon1,lat1, 'r.', latlon= True, ms= 20)
m.plot(lon1,lat1,'r.',latlon= True, ms= 10, label= 'Boia 1')
plt.legend()

m.plot(lon2,lat2, 'y.', latlon= True, ms= 20)
m.plot(lon2,lat2, 'y.',latlon= True, ms = 10, label= 'Boia 2')
plt.legend()

m.plot(lon3,lat3, 'g.', latlon= True, ms=20)
m.plot(lon3,lat3, 'g.', latlon= True, ms= 20)
m.plot(lon3,lat3, 'g.',latlon= True, ms= 10, label= 'Boia 3')
plt.legend()

m.plot(lon4,lat4, 'k.', latlon= True, ms= 20)
m.plot(lon4,lat4, 'k.',latlon= True, ms= 10, label= 'Boia 4')
plt.legend()

plt.title('Localização das boias PIRATA ', fontsize = 18, fontweight='bold')


#     c) Utilizando uma das boias, construa uma série temporal da temperatura em 100m de profundidade.(2 pontos)

# In[22]:


dado_r = Dataset(r'C:\Users\Mateusin\Desktop\Python\t0n0e_mon.cdf')


# In[23]:


time= dado_r['time'][:]
depth= dado_r['depth'][:]
T_20= dado_r['T_20'][:,:,0,0]
dado_r['time']


# In[24]:


prof=[dado_r['depth'] == 100]
temp20 = dado_r['T_20'][:,dado_r['depth'] == 100,0,0]


# In[25]:


fig = plt.figure(figsize=(12,10), facecolor='lightskyblue')
plt.axes(facecolor='whitesmoke')
plt.plot(temp20, color='g')

plt.xlabel('Tempo', fontsize=12)
plt.ylabel('Temperatura ºC', fontsize=12)
plt.title('Série temporal da temperatura da boia 3 em 100 metros de profundidade', fontsize = 15, fontweight= 'bold')

