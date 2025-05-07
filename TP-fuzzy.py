import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


salado = ctrl.Antecedent(np.arange(0, 11, 1), 'salado')
dulce = ctrl.Antecedent(np.arange(0, 11, 1), 'dulce')
solido = ctrl.Antecedent(np.arange(0, 11, 1), 'solido')
caliente = ctrl.Antecedent(np.arange(0, 11, 1), 'caliente')
hambre = ctrl.Antecedent(np.arange(0,11,1,), 'hambre')

sugerencia = ctrl.Consequent(np.arange(0, 11, 1), 'sugerencia')


salado['bajo'] = fuzz.trimf(salado.universe, [0, 0, 5])
salado['medio'] = fuzz.trimf(salado.universe, [2, 5, 8])
salado['alto'] = fuzz.trimf(salado.universe, [5, 10, 10])

dulce['bajo'] = fuzz.trimf(dulce.universe, [0, 0, 5])
dulce['medio'] = fuzz.trimf(dulce.universe, [2, 4, 7])
dulce['alto'] = fuzz.trimf(dulce.universe, [5, 9, 10])

solido['bajo'] = fuzz.trimf(solido.universe, [0,0,3])
solido['medio'] = fuzz.trimf(solido.universe, [2,4,6])
solido['alto'] = fuzz.trimf(solido.universe, [5,8,10])

caliente['bajo'] = fuzz.trimf(caliente.universe, [0,1,4])
caliente['medio'] = fuzz.trimf(caliente.universe, [3,5,8])
caliente['alto'] = fuzz.trimf(caliente.universe, [6,10,10])

hambre['poca'] = fuzz.trimf(hambre.universe, [0,0,4])
hambre['medio'] = fuzz.trimf(hambre.universe, [3,5,7])
hambre['mucha'] = fuzz.trimf(hambre.universe, [6,8,10])

sugerencia['flan'] = fuzz.trimf(sugerencia.universe, [0, 1, 3])
sugerencia['helado'] = fuzz.trimf(sugerencia.universe, [1, 2, 4])
sugerencia['frutas'] = fuzz.trimf(sugerencia.universe, [2, 4, 6])
sugerencia['yogur'] = fuzz.trimf(sugerencia.universe, [3, 5, 7])
sugerencia['pasta'] = fuzz.trimf(sugerencia.universe, [5, 6, 8])
sugerencia['carne'] = fuzz.trimf(sugerencia.universe, [6, 7, 9])
sugerencia['sopa'] = fuzz.trimf(sugerencia.universe, [7, 8, 10])
sugerencia['guiso'] = fuzz.trimf(sugerencia.universe, [8, 9, 10])

rule1 = ctrl.Rule(salado['alto'] & solido['medio'] & hambre['medio'], sugerencia['pasta'])
rule2 = ctrl.Rule(dulce['alto'] & solido['bajo'], sugerencia['flan'])
rule3 = ctrl.Rule(caliente['alto'] & hambre['mucha'] & salado['alto'], sugerencia['guiso'])
rule4 = ctrl.Rule(salado['medio'] & dulce['medio'] & solido['medio'], sugerencia['frutas'])
rule5 = ctrl.Rule(caliente['alto'] & hambre['medio'], sugerencia['sopa'])
rule6 = ctrl.Rule(caliente['alto'] & hambre['medio'], sugerencia['pasta'])
rule7 = ctrl.Rule(caliente['bajo'] & solido['bajo'] & hambre['medio'], sugerencia['helado'])
rule8 = ctrl.Rule(salado['medio'] & dulce['medio'] & solido['bajo'], sugerencia['yogur'])
rule9 = ctrl.Rule(caliente['medio'] & solido['alto'], sugerencia['carne'])
rule10 = ctrl.Rule(caliente['alto'] & salado['alto'] & solido['bajo'], sugerencia['sopa'])
rule11 = ctrl.Rule(caliente['medio'] & salado['medio'] & solido['bajo'], sugerencia['sopa'])

sistema_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])  # incluir todas las reglas
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Prueba con tus valores
sistema.input['salado'] = 8
sistema.input['dulce'] = 2
sistema.input['solido'] = 2
sistema.input['caliente'] = 7
sistema.input['hambre'] = 4

sistema.compute()
print("Puntuación de sugerencia:", sistema.output['sugerencia'])

