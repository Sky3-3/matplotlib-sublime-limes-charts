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
