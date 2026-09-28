# Bitácora

**Fecha:** 26/9/2026
**Consigna / ejercicio número:** Actividad 1 - práctica ("Organizando Información con Estructuras de Datos")

---

## Antes de resolver

**¿Qué creo que tengo que hacer?**
Guardar la info de cada columna del dataset nombre, tipo y completitud— y armar una forma de que distintos roles vean un subconjunto de esas columnas, ordenadas de una manera distinta según el rol.

**¿Qué dudas tengo antes de empezar?**
 Al principio no tenía claro cómo combinar "columnas" y "roles" en una sola estructura, ni para qué servía separar ROLES de la función que arma el informe.

**¿Qué palabras o indicios de la consigna me dan pistas de qué se espera, y por qué?**


**¿Necesitaste usar la IA para responder estas preguntas? ¿Qué dudas no pudiste
aclarar con los contenidos dados en la clase?**
_(Acá sé honesto: usé IA (Claude) para entender conceptos que la clase dio muy
rápido — sobre todo precedencia de operadores (and/or), mutabilidad y copias de
listas/diccionarios, y para entender qué hacían filter()/map()/lambda, que no
llegamos a ver en profundidad en clase.)_

---

## Mientras resolvía

**¿Qué opciones o caminos consideré antes de elegir uno, y por qué elegí ese?**
Pensé en usar una lista de tuplas para las columnas, pero un
diccionario me permite buscar por nombre de columna directamente con
columnas["EDAD"] en vez de recorrer toda la lista buscando el nombre.


**¿Cómo me di cuenta de que algo funcionaba o no funcionaba?**
Probé la función con cada rol por separado y comparé a mano
qué columnas esperaba ver contra lo que efectivamente imprimía.


## Al terminar

**¿Qué descubrí o entendí mejor a partir de esto?**
Entendí la diferencia entre modificar un diccionario/lista existente
y reasignarlo — algo que antes me confundía mucho — y para qué sirve tener
valores por defecto en una función.

**¿Qué me queda pendiente o sigo sin entender?**
_(Sé honesto acá también — por ejemplo, si todavía te cuesta lambda, o
namespaces/módulos de la Clase 3 que dejamos para después.)_

**¿Esto se relaciona con otro ejercicio o concepto que ya vimos?**
Usa directamente diccionarios y sorted() de la Clase 2, y funciones con parámetros por defecto y docstrings.

---

## Preguntas orientadoras de la consigna

**¿Qué ventajas tienen las estructuras elegidas (diccionarios) respecto a otras
vistas en la teoría?**
_(Por ejemplo: a diferencia de una lista, un diccionario permite acceder
directamente por nombre de columna sin tener que recorrer nada, y agrupa
varios datos de una misma columna (tipo, completitud) bajo una sola clave.)_

**¿Qué valores elegí para los roles y los porcentajes de completitud, y por qué?
¿Cómo garanticé que el programa pueda validarse con diferentes roles, criterios
y umbrales?**
_(Contá que probaste los 4 casos: sin rol, y los 3 roles con distinto
orden_por/direccion/minimo, y que revisaste a mano que el resultado fuera el
esperado en cada caso — incluí capturas o el resultado impreso si querés.)_

**¿Por qué conviene separar la configuración de los roles (ROLES) de la lógica
que genera el informe?**
_(Por ejemplo: porque así se puede agregar o modificar un rol sin tocar el
código de la función, y viceversa — reduce el riesgo de romper algo que ya
funcionaba.)_

**¿Qué parámetros se pueden definir con valores por defecto?**
_(rol=None, columnas=COLUMNAS, roles=ROLES — así se puede llamar a la función
sin argumentos y obtener el comportamiento por defecto pedido.)_

**Si agrego una nueva columna al dataset, ¿en qué partes del código impacta?
¿Y si solo quiero que un rol existente incluya esa columna?**
_(Agregar la columna: solo hay que tocar el diccionario COLUMNAS en datos.py.
Que un rol la incluya: solo hay que agregar el nombre a la lista "columnas" de
ese rol en ROLES, también en datos.py. La función informe.py no se toca en
ningún caso.)_

**¿Qué pasaría si un rol tuviera un criterio de orden distinto a "nombre" o
"completitud" (por ejemplo, "promedio")? ¿Cómo lo detectarías y qué harías
para que el programa no falle?**
_(La función levanta un ValueError explícito con un mensaje claro cuando
orden_por no es "nombre" ni "completitud", en vez de fallar con un error
confuso más adelante en el código.)_

**¿Qué cambiaría si por defecto el informe debiera salir según uno de los
roles?**
_(Bastaría con cambiar el valor por defecto del parámetro rol en la función,
por ejemplo rol="analista", en vez de rol=None.)_
