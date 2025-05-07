import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


salado = ctrl.Antecedent(np.arange(0, 11, 1), 'salado')
dulce = ctrl.Antecedent(np.arange(0, 11, 1), 'dulce')
#solido = ctrl.Antecedent(np.arange(0, 11, 1), 'solido')
#caliente = ctrl.Antecedent(np.arange(0, 11, 1), 'caliente')
#hambre = ctrl.Antecedent.(np.arange(0,11,1, 'hambre'))

sugerencia = ctrl.Consequent(np.arange(0, 11, 1), 'sugerencia')


salado['bajo'] = fuzz.trimf(salado.universe, [0, 0, 5])
salado['medio'] = fuzz.trimf(salado.universe, [2, 5, 8])
salado['alto'] = fuzz.trimf(salado.universe, [5, 10, 10])

dulce['bajo'] = fuzz.trimf(dulce.universe, [0, 0, 5])
dulce['medio'] = fuzz.trimf(dulce.universe, [2, 4, 7])
dulce['alto'] = fuzz.trimf(dulce.universe, [5, 9, 10])
# Repetir lo mismo para las demás variables...

# 3. Definir las funciones de pertenencia para la salida (sugerencia)
# Podés definir por ejemplo:
# 0-2: postre, 3-5: snack, 6-8: plato principal, 9-10: sopa caliente, etc.

sugerencia['papas fritas'] = fuzz.trimf(sugerencia.universe,[6,8,10])
sugerencia['flan con dulce de leche'] = fuzz.trimf(sugerencia.universe, [0,1,3])

# 4. Crear las reglas difusas
rule1 = ctrl.Rule(salado['alto'] & dulce['bajo'], sugerencia['papas fritas'])
rule2 = ctrl.Rule(salado['bajo'] & dulce['alto'], sugerencia['flan con dulce de leche'])
# Agregá más reglas según tu lógica

# 5. Crear el sistema de control
sistema_control = ctrl.ControlSystem([rule1, rule2])  # incluir todas las reglas
sistema = ctrl.ControlSystemSimulation(sistema_control)

# 6. Ingresar valores
sistema.input['salado'] = 7
sistema.input['dulce'] = 2

# 7. Calcular y mostrar salida
sistema.compute()
print(sistema.output['sugerencia'])
