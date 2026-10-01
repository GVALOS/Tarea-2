# Documentación del reto del Hospital Diagnóstico

## Descripción general
El sistema registra a un nuevo empleado y evalúa el estado de los documentos requeridos.
La estructura lógica condicional consta de los siguientes pasos:
1. Se registra al nuevo empleado.
2. Se muestra el listado de documentos a presentar.
3. Por cada documento se muestra el estado de Completo o Faltante.
4. Si el nuevo empleado no es médico, el estado global será Completo al tener todos los documentos requeridos, sin contar el carnet médico.
5. Si el nuevo empleado es médico, se requiere el carnet de certificación y el resto de documentos.
6. Si faltan documentos, el estado global será Incompleto.
7. Si no tiene ningún documento adjuntado, se mostrará Ningún documento adjuntado.

## Documentos evaluados
Los documentos utilizados en la lógica son:
- DUI
- Antecedentes penales
- Carnet de certificación médica
- CV
- Solvencia policial
El carnet de certificación médica se solicita únicamente si el empleado es médico.

## Estados de los documentos
Cada documento puede tener uno de los siguientes estados:
- Completo
- Faltante
Todos los documentos están definidos con `False` y cambian a `True` cuando el usuario indica que el documento fue presentado.

## Estado global
El estado global puede ser:
- Completo
- Incompleto
- Ningún documento adjuntado

## Empleado no médico
Para que el estado sea Completo, debe tener:
- DUI
- Antecedentes penales
- Solvencia policial
- CV
Si falta uno de los documentos, el estado será Incompleto.
Si todos los documentos están en `False`, el estado será Ningún documento adjuntado.

## Empleado médico
Para que el estado sea Completo, debe tener:
- DUI
- Antecedentes penales
- Carnet de certificación médica
- Solvencia policial
- CV
Si falta uno o más documentos, el estado será Incompleto.
Si los tres documentos están en `False`, el estado será Ningún documento adjuntado.

## Preguntas de análisis

### ¿Cuáles son los estados posibles reales del dato que van a evaluar?

Por documento:
- Completo
- Faltante

Estado general:
- Completo
- Incompleto
- Ningún documento adjuntado

### ¿Qué valor o condición define cada estado?
- `True`: documento completo.
- `False`: documento faltante.
El estado global depende del tipo de empleado y de los documentos requeridos.

### ¿Hay reglas de negocio confirmadas que aún no están reflejadas?
Sí. Antes del registro y evaluación de documentos, el usuario debe iniciar sesión con usuario y contraseña.

### ¿Qué pasa si el dato no encaja en ningún estado esperado?
Los documentos se inicializan en `False` y solo cambian a `True` cuando así se indica.
Si el tipo de empleado no es válido, se debe mostrar un mensaje de error, que menciona que dicho estado no es existente.
