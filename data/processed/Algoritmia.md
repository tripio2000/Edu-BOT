Como programador Python, especialista en DevOps e ingeniero de IA, y como profesor universitario de métodos numéricos, aquí tienes el capítulo "Algoritmia. Conceptos Básicos" de las notas de teoría, optimizado para RAG y presentado en formato Markdown.

Este capítulo introduce los conceptos fundamentales de la algoritmia, esenciales para la resolución computacional de problemas en ingeniería, enfocándose en la definición de algoritmos, variables, operadores y estructuras de control, además de ejemplos prácticos.

---

# Notas de Teoría: Cálculo Numérico y Computación

## Capítulo: Algoritmia. Conceptos Básicos

Este capítulo presenta estructuras algorítmicas de gran utilidad en procesos de cálculo y decisión en ingeniería, buscando ilustrarlas con ejemplos propios de operaciones matriciales y métodos de cálculo numérico. Aunque no se profundiza en la sintaxis de lenguajes de programación, los algoritmos se expresan en forma de **pseudocódigos**.

### 1.1 Introducción

Se presentan **estructuras algorítmicas** de amplio uso en procesos de cálculo y decisión en ingeniería. El objetivo es mostrarlas a través de ejemplos relacionados con **operaciones matriciales** y **métodos de cálculo numérico**. Los algoritmos se expresan en **pseudocódigo**.

### 1.2 Definiciones

#### Algoritmo

Un **algoritmo** es una **forma ordenada de describir un procedimiento**. La manera más básica de representarlo es el **pseudocódigo**, que consiste en la expresión de los pasos a seguir mediante palabras y ecuaciones. Otras formas incluyen diagramas de flujo y diagramas de bloques.

Para describir un proceso algorítmico, se utilizan elementos como:
*   **Variables**.
*   **Constantes**.
*   **Operadores** algebraicos y lógicos.
*   **Estructuras típicas**: secuenciales e iterativas (como "repetir" o "mientras").

Todo algoritmo debe contener los siguientes elementos:
*   **Declaración de variables**.
*   **Ingreso de datos** o asignaciones primarias.
*   **Proceso propiamente dicho**.
*   **Entrega de resultados**.

#### Variables

Una **variable** es como un **recipiente** en la memoria de la computadora, identificada por un nombre, que puede alojar cierta información.
*   Los **nombres** de las variables deben comenzar con una letra y no deben exceder los 10 caracteres.
*   Se sugiere que el nombre de la variable sea **representativo** de la información que almacena.

A una variable se le puede:
*   **Asignar valores**: mediante constantes, otras variables o expresiones algebraicas/lógicas. El símbolo " " (flecha izquierda) se usa para la asignación.
    *   Ejemplo: `altura 10` (se asigna el valor 10 a la variable `altura`).
    *   Ejemplo: `altura (base * 2) / 10` (se asigna el resultado de la operación a `altura`).
*   **Modificarla**: reasignando un valor que involucre a la propia variable.
    *   Ejemplo: `altura altura + 2`.
*   **Borrarla**.
*   **Mostrar** (escribir en pantalla o archivo): `Escribir altura`.
*   **Leer** (ingresar información por teclado): `Leer altura`.

##### Clasificación de las variables según su dimensión

*   **Variables simples**: Guardan un único valor (ej., `altura`, `base`).
*   **Variables Dimensionadas**: Representan o guardan información referida a un mismo dato, pero que por su magnitud requieren una dimensión.
    *   **Variables de una dimensión (Vectores)**: Representadas como `A(i)`.
        *   Ejemplo: `Notas(i)` para las notas de un examen.
    *   **Variables de más de una dimensión (Matrices)**.
        *   **Dos dimensiones (Matrices plano)**: Representadas como `B(i; j)`, donde `i` es fila y `j` es columna.
            *   Ejemplo: `B(4;8)` en la declaración de variables define una matriz de 4 filas y 8 columnas. En el desarrollo del algoritmo, `B(4;8)` se refiere al casillero en la fila 4, columna 8.
        *   **Tres dimensiones (Matrices espacio)**: Representadas como `C(i; j; k)`, donde `i` es fila, `j` es columna y `k` es profundidad.
            *   Ejemplo: `C(4;8;3)`.

##### Clasificación de las variables según su contenido

Los tipos de variables dependen del lenguaje de programación. En pseudocódigo se usarán 4 tipos:
*   **Numérico-Enteros**: Contienen números enteros (ej., `4`, `-8`, `4875`).
*   **Numérico-Reales**: Contienen números con decimales (ej., `4.2`, `-5.88`). Los reales incluyen a los enteros.
*   **Lógicas**: Contienen solo `[V]` (Verdadero) o `[F]` (Falso).
*   **Carácter**: Contienen cadenas de caracteres (ej., `"mamá"`, `"casa"`). Para distinguirlos de los nombres de variables, el contenido se coloca entre comillas.

Las variables siempre deben ser **declaradas al inicio** del algoritmo, especificando su nombre y tipo.
*   Ejemplo de declaración en pseudocódigo: `Var (Var1:Entero; Var2, Var3:Real; Var4:Carácter)`.

#### Constantes

Las **constantes** pueden ser del mismo tipo que las variables, pero su **valor no cambia** durante la ejecución del algoritmo. No se les asigna un nombre ni se declaran.

#### Operadores

Los **operadores** permiten realizar **operaciones algebraicas** o establecer **relaciones** entre variables o constantes. Tienen un **orden de prioridad** establecido:

| Prioridad | Operador | Nombre             | Resultado      |
| :-------- | :------- | :----------------- | :------------- |
| 1         | `^`      | Potencia           | Numérico       |
| 2         | `*`, `/` | Producto - Cociente | Numérico       |
| 3         | `+`, `-`, ` ` | Suma - Resta - Concatenación de caracteres | Numérico (Suma/Resta), Carácter (Concatenación). |
| 4         | `<` `>`, `<=` `>=`, `=`, `<>` | Relación (Igual, distinto, mayor, menor, etc.) | Lógico         |
| 5         | `.NOT.`  | Negación           | Lógico         |
| 6         | `.AND.`  | Conjunción [Y]     | Lógico         |
| 7         | `.OR.`   | Disyunción [O]     | Lógico         |

Cuando hay dos operadores de la misma prioridad, se resuelven de **izquierda a derecha**. Los **paréntesis, corchetes o llaves** anulan el orden de prioridad, resolviéndose primero lo que encierran.

### 1.3 ALGORITMO TIPO Secuencia

La **secuencia** es la relación más simple en un algoritmo. Establece que una línea de código no se ejecuta hasta que la anterior haya terminado, y la siguiente no puede ejecutarse hasta que la actual haya finalizado.

**Esquema**:
```
Cuerpo de líneas de código
```

**EJEMPLO 1**: Calcular el valor medio de dos valores dados (`a`, `b`).
*   **Datos**: Valores `ExtrA`, `ExtrB`.
*   **Fórmula**: `PtoMedC = (ExtrA + ExtrB) / 2`.
*   **Pseudocódigo**:
    ```pseudocode
    Var (ExtrA, ExtrB, PtoMedC: Real)
    Escribir "Ingrese extremo inferior del intervalo"
    Leer ExtrA
    Escribir "Ingrese extremo superior del intervalo"
    Leer ExtrB
    PtoMedC  (ExtrA + ExtrB) / 2
    Escribir "El valor medio es", PtoMedC
    ```

**EJEMPLO 2**: Encontrar las raíces de una ecuación de segundo grado (`ax² + bx + c = 0`).
*   **Datos**: Coeficientes `a`, `b`, `c`.
*   **Fórmula**: `Raiz = (-b ± √(b² - 4ac)) / 2a`.
*   **Pseudocódigo**:
    ```pseudocode
    Var (a, b, c, Raiz1, Raiz2: Real)
    Escribir "Ingrese coeficiente a"
    Leer a
    Escribir "Ingrese coeficiente b"
    Leer b
    Escribir "Ingrese coeficiente c"
    Leer c
    Raiz1  (-b + (b^2 - 4*a*c)^0.5) / (2*a)
    Raiz2  (-b - (b^2 - 4*a*c)^0.5) / (2*a)
    Escribir "La raiz 1 es", Raiz1
    Escribir "La raiz 2 es", Raiz2
    ```

### 1.4 ALGORITMO TIPO Decisión simple

La **decisión simple** ocurre cuando, a través de una pregunta con resultado lógico (`[V]` o `[F]`), se ejecuta una acción preestablecida si la respuesta es **Verdadera**. Si la respuesta es **Falsa**, el programa continúa sin realizar la acción.

**Esquema**:
```
        ¿ ?
       / \
      [V] [F]
       |   |
  Cuerpo de líneas
   de código
       |
Fin de la estructura de decisión
```

**Pseudocódigo**:
```pseudocode
IF (¿Pregunta ?) THEN
    Cuerpo de líneas de código
ENDIF
```

**EJEMPLO**: Incrementar la variable `ExtrA` en 1 si no es negativa.
```pseudocode
IF (ExtrA  0) THEN
    ExtrA  ExtrA + 1
ENDIF
```

**EJEMPLO**: Encontrar las raíces de una ecuación de segundo grado, **solo si el discriminante es positivo o cero**.
```pseudocode
Var (a, b, c, Discrim, Raiz1, Raiz2: Real)
Escribir "Ingrese coeficiente a"
Leer a
Escribir "Ingrese coeficiente b"
Leer b
Escribir "Ingrese coeficiente c"
Leer c
Discrim  (b^2 - 4*a*c)
IF ((Discrim > 0) .OR. (Discrim = 0)) THEN
    Raiz1  (-b + (Discrim)^0.5) / (2*a)
    Raiz2  (-b - (Discrim)^0.5) / (2*a)
ENDIF
Escribir "La raiz 1 es", Raiz1
Escribir "La raiz 2 es", Raiz2
```

### 1.5 ALGORITMO TIPO Decisión Compuesta

La **decisión compuesta** también se basa en una pregunta lógica (`[V]` o `[F]`), pero **siempre ejecuta un cuerpo de líneas de código**. Si la respuesta es **Verdadera**, ejecuta un cuerpo de código, y si es **Falsa**, ejecuta un cuerpo de código distinto.

**Esquema**:
```
        ¿ ?
       / \
      [V] [F]
       |   |
Cuerpo de líneas   Cuerpo de líneas
 de código para    de código para
   opción [V]        opción [F]
       \   /
        \ /
Fin de la estructura de decisión
```

**Pseudocódigo**:
```pseudocode
IF ¿Pregunta ? THEN
    Cuerpo de líneas de código para opción [V]
ELSE
    Cuerpo de líneas de código para opción [F]
ENDIF
```

**EJEMPLO**:
```pseudocode
IF ExtrA  ExtrB THEN
    PtoMedC  ExtrA
ELSE
    PtoMedC  ExtrB
ENDIF
```

### 1.6 ALGORITMO TIPO Estructuras Iterativas

Las **estructuras iterativas** (o repetitivas) se utilizan para **repetir un cuerpo de líneas de código** en un algoritmo, evitando la duplicación y haciendo el proceso más eficiente. Se presentan cuatro tipos principales:
*   `Mientras` (DO WHILE)
*   `Variar` (DO FOR)
*   `Repetir`
*   `Iterar`

#### Mientras (DO WHILE)

Esta estructura repite un cuerpo de código **mientras una pregunta lógica sea Verdadera** (`[V]`). Si la pregunta es **Falsa** (`[F]`), el cuerpo de código no se ejecuta y el algoritmo continúa. El análisis de la condición se realiza **antes** de la ejecución del cuerpo de código, lo que significa que el cuerpo podría no ejecutarse nunca si la condición es falsa desde el inicio. Es crucial asegurar que la respuesta a la pregunta **tienda a ser Falsa** para evitar bucles infinitos.

**Esquema**:
```
¿ ?
[V] \
 |  \
Cuerpo de líneas de código
 |   /
[F] /
Fin de la estructura repetitiva
```

**Pseudocódigo**:
```pseudocode
DO WHILE ¿ ?
    Cuerpo de líneas de código
ENDDO
```

**Ejemplo**:
```pseudocode
DO WHILE ExtrA  ExtrB
    ExtrA  ExtrA + 1
    Escribir ExtrA
ENDDO
```

#### Variar (DO FOR)

Este es un caso especial de la estructura `Mientras`, utilizada cuando se conoce **exactamente el número de veces** que un cuerpo de código debe repetirse. Utiliza una **variable auxiliar** (generalmente entera) que varía desde un valor inicial hasta un valor final, con un paso determinado.

**Esquema**:
```
Mientras la variable auxiliar no alcance el valor final
    Cuerpo de líneas de código
Fin de la estructura repetitiva
```

**Pseudocódigo**:
```pseudocode
DO FOR VarAux OF VI TO VF STEP P
    Cuerpo de líneas de código
ENDDO
```

**Ejemplo**:
```pseudocode
DO FOR Aux OF 1 TO 20 STEP 1
    Escribe PtoMedC
    PtoMedC  PtoMedC / 2
ENDDO
```

#### Repetir

En esta estructura, el análisis de la condición se realiza **después** de la ejecución del cuerpo de código. El cuerpo de código se repite **mientras una pregunta lógica sea Falsa** (`[F]`). Cuando la respuesta es **Verdadera** (`[V]`), la repetición se detiene. La estructura garantiza que el cuerpo de código se ejecute **al menos una vez**. Es importante que la respuesta a la pregunta **tienda a ser Verdadera** para evitar bucles infinitos.

**Esquema**:
```
Comienzo de la estructura
Cuerpo de líneas de código
¿ ? [F]
[V] \
     Fin de la estructura repetitiva
```

**Pseudocódigo**:
```pseudocode
DO
    Cuerpo de líneas de código
    IF ¿ ? EXIT
ENDDO
```

**Ejemplo**:
```pseudocode
DO
    ExtrA  ExtrA - 1
    Escribir ExtrA
    IF ExtrA  10 EXIT
ENDDO
```

#### Iterar

Esta estructura tiene **dos cuerpos de líneas de código** (`Cp1` y `Cp2`) y el análisis de la condición se realiza **entre ellos**. La repetición de ambos cuerpos ocurre **mientras una pregunta lógica sea Falsa** (`[F]`). Si la respuesta es **Verdadera** (`[V]`), el cuerpo `Cp2` no se ejecuta y el algoritmo continúa. El cuerpo `Cp1` se ejecuta al menos una vez, y siempre una vez más que `Cp2`. La condición debe **tender a ser Verdadera** para evitar bucles infinitos.

**Esquema**:
```
Comienzo de la estructura repetitiva
Cuerpo de líneas de código Cp1
¿ ? [F]
[V] \
     Cuerpo de líneas de código Cp2
      /
     /
Fin de la estructura repetitiva
```

**Pseudocódigo**:
```pseudocode
DO
    Cuerpo de líneas de código Cp1
    IF ¿ ? EXIT
    Cuerpo de líneas de código Cp2
ENDDO
```

**Ejemplo**:
```pseudocode
DO
    ExtrA  ExtrA * 10
    IF 100  ExtrA EXIT
    Escribir ExtrA
ENDDO
```

### 1.7 EJEMPLO. Algoritmo del Método de Bisección

El **Método de Bisección** se utiliza para encontrar la abscisa `sx` tal que `f(sx) = 0` para una función `f(x)` conocida y **continua** en un intervalo `[a, b]` donde `f(a) * f(b) < 0`. La función `f(x)` debe programarse para cada nueva oportunidad.

El algoritmo tiene las siguientes **Entradas**: `a`, `b`, `Error E`. La **Salida** es la solución aproximada `p`.

#### Alternativa 1

Un posible algoritmo es el siguiente:
```pseudocode
Algoritmo Bisección para función f(x)
Var(a, b: entero; p, E: real)

Escribir ("ingrese el valor de a")
Leer (a) // ingresa el valor de 'a'
Escribir ("ingrese el valor de b")
Leer (b) // ingresa el valor de 'b'
Escribir ("ingrese el valor del error admisible")
Leer (E) // ingresa el valor de 'E'

p  (a + b) / 2 // Calcula la primera aproximación de la raíz

DO WHILE ((f(p)  0) .AND. ( (b - a) / 2  E ))
    IF (f(a) * f(p) < 0) THEN
        b  p // Se reasigna 'b' y se mantiene 'a'
    ELSE
        a  p // Se mantiene 'b' y se reasigna 'a'
    ENDIF
    p  (a + b) / 2 // Se calcula la nueva aproximación
ENDDO

Escribir ("la solución aproximada es:", p)
END
```

**Características de la Alternativa 1**:
*   Los **controles de detención** (o medidas del error) se calculan en la misma sentencia `DO WHILE`.
*   Las **raíces aproximadas** en iteraciones anteriores se **pierden**.
*   Los **límites del intervalo** donde está la raíz en cada iteración se **pierden**.
*   El **control del número de iteraciones** que se realiza **no se efectúa**.

#### Alternativa 2

Otro posible algoritmo:
```pseudocode
Algoritmo Bisección para función f(x)
Var(a, b, N, i: entero; p: real)

Escribir ("ingrese el valor de a")
Leer (a) // ingresa el valor de 'a'
Escribir ("ingrese el valor de b")
Leer (b) // ingresa el valor de 'b'
Escribir ("ingrese el Nº máx de iteraciones")
Leer (N) // ingresa el valor de 'N'

p  (a + b) / 2 // Calcula la primera aproximación

DO FOR i = 1 TO N STEP 1
    IF (f(a) * f(p) < 0) THEN
        b  p // Se reasigna 'b' y se mantiene 'a'
    ELSE
        a  p // Se mantiene 'b' y se reasigna 'a'
    ENDIF
    p  (a + b) / 2 // Se calcula la nueva aproximación
ENDDO

Escribir ("la solución aproximada es:", p) // Se tiene una aproximación luego de N iteraciones
END
```

**Características de la Alternativa 2**:
*   Los valores iniciales de `a` y `b` deben cumplir la **condición de inicialización** del método de bisección.
*   Los **controles de detención no existen**, ya que la tarea se realizará `N` veces.
*   La **raíz aproximada** que se retiene es la **última**.
*   Los **límites del intervalo** donde está la raíz en cada iteración se **pierden**.

#### Alternativa 3

Esta alternativa combina los dos algoritmos anteriores:
```pseudocode
Algoritmo Bisección para función f(x)
Var(a, b, N: entero; p, E: real)

Escribir ("ingrese el valor de a")
Leer (a) // ingresa el valor de 'a'
Escribir ("ingrese el valor de b")
Leer (b) // ingresa el valor de 'b'
Escribir ("ingrese el valor del error admisible")
Leer (E) // ingresa el valor de 'E'
Escribir ("ingrese el Nº máx de iteraciones")
Leer (N) // ingresa el valor de 'N'

p  (a + b) / 2 // Se calcula la primera aproximación de la raíz
i  1 // Se inicia el control de número de iteraciones

DO WHILE ( (f(p)  0) .AND. ( (b - a) / 2  E ) .AND. (i  N ) )
    // Se detiene cuando una de las tres condiciones se cumple
    IF (f(a) * f(p) < 0) THEN
        b  p // Se reasigna 'b' y se mantiene 'a'
    ELSE
        a  p // Se mantiene 'b' y se reasigna 'a'
    ENDIF
    p  (a + b) / 2 // Se calcula la nueva aproximación de la raíz
    i  i + 1 // Se calcula el número de iteración a realizar
ENDDO

Escribir ("la solución aproximada es:", p)
END
```

**Características de la Alternativa 3**:
*   Los valores iniciales de `a` y `b` deben cumplir la **condición de inicialización** del método de bisección.
*   La **raíz aproximada** que se retiene es la **última**.
*   Los **límites del intervalo** donde está la raíz en cada iteración se **pierden**.
*   Los **controles de detención** (o medidas del error) se calculan en la misma sentencia `DO WHILE`.
*   El control de detención se basa en que se cumpla alguna de las siguientes condiciones:
    *   El **valor de la función es cero** (`f(p) = 0`).
    *   El **valor de la longitud del intervalo es menor que E** (`(b-a)/2 < E`).
    *   El **número de iteración superó el valor máximo de iteraciones** (`i > N`).

---
