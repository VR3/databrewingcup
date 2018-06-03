# BREWING DATA CUP

## Edición 2018

El BDC es el Hackathon de Ciencia de Datos más importante de la CDMX. Es organizado por [Grupo Modelo](https://en.wikipedia.org/wiki/Grupo_Modelo), [Microsoft](https://www.microsoft.com) y [The Data Pub](https://facebook.com/thedatapub), la comunidad de Ciencia de Datos más grande de México. El objetivo es seleccionar a los mejores Científicos de Datos para ingresar a las filas del grupo de Innovación & Analytics en la cervecer

- Fecha: 02/06/18 - 03/06/18
- Desafío: Comercial
- Equipo: VR3

	> Oscar Chavez **<oscar@vr3.io>**
	> 
	> Patrick Moss **<patrick@vr3.io>**

---

### INDEX

- RETO
- ESTRATEGIA
- RESULTADOS

## RETO

**Grupo Modelo** debe pronosticar la demanda 
de más de **250 SKUs** en más de **200 Subagencias** *(Restaurantes, Bares, Tiendas, etc.)* con *2 Meses* de anticipación.

Este pronóstico es la entrada para determinar el **volumen de producción**, es por eso que debe hacerse con 2 meses de anticipación.

#### PREGUNTA

> ¿Cuántos **hectolitros** de cada **SKU** debe proveer **Grupo Modelo** a cada **Subagencia**, en función de los *datos históricos de venta*?

#### OBJETIVO

> Generar un modelo predictivo que utilice datos históricos para pronosticar la demanda.

#### DICCIONARIO

| Variable | Tipo |
|:-:|:-:|
| Mes | Fecha |
| Subagencia | Carácter |
| SKU | Carácter |
| Hectolitros | Numérico |

| Variable | Tipo |
|:-:|:-:|
| Subagencia | Carácter |
| Desc_Subagencia | Carácter |
| Latitud | Numérico |
| Longitud | Numérico |

## ESTRATEGIA

El contexto del reto nos habla de un problema al que podemos aproximar una solución utilizando algoritmos de **regresión**, para generar un modelo de **aprendizaje supervisado**.

1. Revisar Dataset y entender el problema
2. Integrar datos de **factores externos** al Dataset.
2. Ingestar Dataset => **Azure ML Studio**
3. Split 70/30 del Dataset (Training/Test)
4. Seleccionar Modelo de **Machine Learning => Regression**
5. Entrenar Modelo
6. Puntuar Modelo
7. Evaluar Modelo

Revisamos el dataset provisto y ploteamos el area de interés:

![plot](https://static.vr3.io/vr3/img/projects/dbc/plot.jpg)

Hectolitros/SKU

![ggplot](https://static.vr3.io/vr3/img/projects/dbc/skuplot.jpg)

Una vez limpiado el dataset, procedimos a ingestar el dataset y a partirlo en 70/30 para tener nuestro **Training Set (70)** y nuestro **Test Set (30)**

Utilizando la información histórica de venta del dataset, implementamos 2 algoritmos de **regresión**:

- **Decision Forest Regression**
- **Poisson Regression**

para generar nuestro **análisis predictivo** utilizando **Microsoft Azure ML Studio**.

![model](https://static.vr3.io/vr3/img/projects/dbc/model.png)


Gráfica de Pronostico Incial

![model](https://static.vr3.io/vr3/img/projects/dbc/histogram.jpg) 


#### FACTORES EXTERNOS

Usamos `python` para generar 5 scripts que consumen y limpian los datasets de los siguientes factores externos que consideramos pertinentes para tener un Dataset más acercado a la realidad.

Primero utilizamos la `latitud y longitud` para encontrar la **ENTIDAD** y a partir de este resultado, consumir los siguientes datasets de [datos.gob.mx](datos.gob.mx
)

- [Clima (Temperatura Máxima/Mínima)](https://datos.gob.mx/busca/dataset/temperatura-maxima-excel)
- [PIB (Estrato Socioeconómico)](https://datos.gob.mx/busca/dataset/el-pib-y-variables-demograficas-entidades)
- [Indicador GINI (Distribución de Ingreso)](https://datos.gob.mx/busca/dataset/valor-del-coeficiente-de-desigualdad-gini-nacional-y-por-entidad-federativa-2010-2012) 
- [Actividad Turística (Derrama Económica)](https://datos.gob.mx/busca/dataset/actividad-hotelera-por-entidad-federativa-ocupacion-y-llegada-de-turistas)


## RESULTADOS

| DESC  | RES |
|:-:|:-:|
| % Error de Modelo Pronosticado Mayo 2018  | **.22364001** | 
| Herramientas Utilizadas  |  Azure ML Studio, R, Python, Pandas, ggplot, googlemaps, numpy |
| Factores Externos | Temperatrua, PIB Estatal, Indicador GINI, Actividad Turística


> #### El **Dataset** de resultados de pronosticos se encuentra en *./data/output/forecast_result.csv*

#### FOLDER STRUCTURE

![model](https://static.vr3.io/vr3/img/projects/dbc/tree.png)

## INSIGHTS

Usar datos externos puede parecer buena idea pero encontramos que los datos disponibles utilizados tienden a generar ruido en las predicciones de los modelos utilizados

- No encontramos correlación con la temperatura del estado y los hectolitros vendidos.
- Hay una correlación muy tenue con la ocupación hotelera por estado y la venta de hectolitros.

---
