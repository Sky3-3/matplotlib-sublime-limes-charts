# Proyecto Python: Visualización Multivariada y Series Temporales con Matplotlib

Este repositorio contiene un proyecto práctico desarrollado en Python utilizando la librería **Matplotlib** enfocado en el diseño de tableros de control visual (*Dashboards*) mediante la configuración de subtramas múltiples concurrentes (`subplots`). El script procesa datos de tráfico web mensual y volumen de ventas segmentado por líneas de productos, implementando marcadores estructurales de control, paletas de colores personalizadas y mapas indexados de etiquetas temporales para optimizar la lectura de tendencias comerciales.

---

## Código Python del Proyecto

El programa genera un lienzo dimensionado, inicializa las regiones de graficación independientes y exporta la salida analítica a un archivo plano de mapa de bits:

```python
from matplotlib import pyplot as plt

# --- 1. Sets de Datos Base (Series Temporales Mensuales) ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# Volumen de ventas indexado por especies de producto
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# --- 2. Inicialización del Lienzo Principal ---
plt.figure(figsize=(12, 8))
x_values = range(len(months))

# --- 3. Región Izquierda: Tendencia de Tráfico Web (Subplot 1) ---
ax1 = plt.subplot(1, 2, 1)
plt.plot(x_values, visits_per_month, marker="o")
plt.xlabel("Months")
plt.ylabel("Visits per Month")
plt.title("Page of Visits per Month")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)

# --- 4. Región Derecha: Distribución de Ventas Multiclase (Subplot 2) ---
ax2 = plt.subplot(1, 2, 2)
plt.plot(x_values, key_limes_per_month, color="#5D6D7E")
plt.plot(x_values, persian_limes_per_month, color="#A569BD")
plt.plot(x_values, blood_limes_per_month, color="#E59866")
plt.legend(["Key Limes", "Persian Limes", "Blood Limes"])
plt.xlabel("Months")
plt.ylabel("Sales per Month")
plt.title("Page of Sales per Month")
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)

# --- 5. Persistencia y Exportación ---
plt.savefig("graphic_lines.png")
plt.close()

```

---

## Estructura de Salida Analítica (Dashboard)

El script genera una composición bidimensional que aísla las métricas operativas del negocio en dos bloques correlacionados por el mismo índice temporal:

### 1. Gráfico de Tendencia Uniclase (Visitas)

Modela el comportamiento de la demanda del sitio web a lo largo del año. La inclusión de marcadores de puntos (`marker="o"`) resalta de manera estricta los picos de tráfico estacionales, identificando el mes de **Junio** como el período de máximo rendimiento absoluto ($16,794$ visitas).

### 2. Gráfico Multiclase Comparativo (Ventas)

Superpone múltiples trazos lineales sobre el mismo plano coordenado utilizando un código de colores hexadecimal específico. Permite auditar qué variedad de producto lidera el mercado mes a mes, correlacionando de forma visual las caídas o subidas del volumen comercial de manera paralela.

#### Vista del Dashboard Exportado

<img width="573" height="410" alt="image" src="https://github.com/user-attachments/assets/715e6999-ff4e-47c3-a7b7-9d5baa677baf" />

---

## Conceptos Técnicos Aplicados

* **Manejo de Gráficos de Cuadrícula (`plt.subplot`)**: Estructura de sintaxis compacta definida por tres argumentos de control: `(filas, columnas, índice_activo)`. `(1, 2, 1)` configura un lienzo de una sola fila con dos posiciones de columnas disponibles, inicializando los trazos sobre la primera celda lógica izquierda.
* **Mapeo Customizado de Ejes (`set_xticklabels`)**: Por defecto, Matplotlib renderiza los valores del eje horizontal utilizando el rango numérico continuo de entrada (`0, 1, 2...`). Forzar los ticks mediante la lista de cadenas estáticas (`months`) mapea los índices posicionales convirtiendo los números en referencias cronológicas legibles (`Jan`, `Feb`...).
* **Segmentación por Atributos de Leyenda (`plt.legend`)**: Inyecta una caja de control semántica que asocia el orden secuencial de las líneas trazadas en el script con sus respectivas etiquetas de negocio, fundamental para la interpretación de gráficos multivariables complejos.
