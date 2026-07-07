"""# =====================================================================
# CURSO: Python para la Innovación (CUGDL x GDG Jalisco)
# SEMANA 1: Mi Primer Script de Supervivencia Financiera
# ====================================================================="""


print("--- 🎒 BIENVENIDO A TU ASISTENTE FINANCIERO ---")

# 1. DEFINICIÓN DE VARIABLES (Datos de entrada)
# Cambia estos números con tus datos reales para probar el script
presupuesto_semanal = float(input("Presupuesto Semanal: "))  # Lo que tienes disponible en la semana (pesos)
print("Tu presupuesto semanal es:", presupuesto_semanal)

print("¿Cuanto gastas a la semana en?:")
gasto_transporte = float(input("Transporte: "))    # Mi macrobús / camión / uber
gasto_comida = float(input("Comida: "))        # Cafetería y snacks
gasto_copias_libros = float(input("Copias y libros: "))   # Material de clase
gasto_total = (gasto_transporte + gasto_comida + gasto_copias_libros)
print("Tus gastos semanales son:", gasto_total)

# 2. OPERACIONES ARITMÉTICAS (Procesamiento de datos)
balance_final = presupuesto_semanal - gasto_total

# 3. MOSTRAR RESULTADOS EN PANTALLA
print("\n=== RESUMEN DE LA SEMANA ===")
print("Presupuesto Inicial: $" + str(presupuesto_semanal))
print("Gasto Total: $" + str(gasto_total))
print("----------------------------")

# 4. TOMA DE DECISIONES LOGÍSTICA (Condicionales if / elif / else)
if balance_final > presupuesto_semanal*0.25:
    print("😎 ¡Vas excelente! Te quedan $" + str(balance_final) + " libres.")
    print("Recomendación: Guarda un poco para ahorrar o date un gusto el fin de semana")

elif balance_final >=0 and balance_final < presupuesto_semanal*0.75:
    print("😐 Presupuesto ajustado. Te quedan $" + str(balance_final) + ".")
    print("Recomendación: Evita gastos hormiga (cafés, papitas) el resto de la semana")

else:
    # El balance es negativo (conversión a positivo con abs() para que se lea bien)
    dinero_faltante = abs(balance_final)
    print("😰 ¡Alerta de quiebra! Te pasaste por: $" + str(dinero_faltante))
    print("Recomendación: Toca activar el modo austero y llevar lonche desde casa")