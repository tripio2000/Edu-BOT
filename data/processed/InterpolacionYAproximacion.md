# INTERPOLACIÓN Y APROXIMACIÓN POLINOMIAL

## 1 INTRODUCCIÓN

En esta unidad temática, el objetivo principal es encontrar una forma analítica, **computacionalmente representable**, para una función `y=f(x)` dada en forma discreta. Se asume que se dispone de un conjunto de `(n+1)` puntos de coordenadas `(xi; yi)`, donde `i` varía de `0` a `n`, y que estos puntos pertenecen a una función cuya expresión analítica no se conoce.

Se propone representar esta función mediante una **combinación lineal de funciones base** `k(x)` (conocidas y linealmente independientes):
`y = Pm(x) = ∑ ak k(x)` (con `k` de `0` a `m`).

Para cada punto `xi`, se define un **residuo** `ri` como la diferencia entre el valor de la función discreta `yi=f(xi)` y el valor de la combinación lineal:
`ri = f(xi) - Pm(xi) = yi - ∑ ak k(xi)` (con `k` de `0` a `m`; `i` de `0` a `n`).

Se distinguen dos conceptos clave basados en la condición impuesta sobre el residuo:

*   **INTERPOLACIÓN**: Cuando se impone una condición de **nulidad "fuerte" del residuo** en cada punto. Esto significa `ri=0` para todo `i` (o `r=0`), haciendo que la función `Pm(x)` **pase por los puntos dados**.
*   **APROXIMACIÓN**: Cuando se impone una condición de **nulidad "débil" del residuo** en el dominio de interés. Esto permite que `ri` no sea cero para algún `i` (es decir, `r ≠ 0`). El **Método de Mínimos Cuadrados** es una forma de aproximación.

## 2 INTERPOLACIÓN

Dada una función `y=f(x)` definida en forma discreta por `(n+1)` puntos `(xi; yi=f(xi))` (con `i=0, n`), se busca una representación analítica mediante una combinación lineal de `n` funciones base `k(x)` conocidas. Es importante notar que, en el contexto de interpolación, el número de funciones base `m` se toma igual a `n` (`m=n`).

Se exige que el residuo sea nulo en cada punto dato de abscisa `xi`:
`ri = f(xi) - Pn(xi) = yi - ∑ ak k(xi) = 0` (para todo `i,k=0,n`).
Esto conduce a un **sistema de ecuaciones lineales**:
`∑ ak k(xi) = yi` (para todo `i,k=0,n`).

Este sistema permite encontrar los coeficientes `ai` de la combinación lineal.

**Observaciones importantes sobre Interpolación:**

*   Por `n+1` puntos pasa un **único polinomio de grado a lo sumo n**. Aunque existan diferentes métodos (Directo, Lagrange, Newton, etc.), todos conducen a expresiones distintas del mismo polinomio único, ya que utilizan funciones base linealmente independientes.
*   El **residuo `r(x) = f(x) - Pn(x)` es ortogonal** a las funciones delta de Dirac definidas en cada punto `xi`.

### 2.1 MÉTODO DIRECTO

En este método, se utilizan como **funciones base** `k(x)` los **polinomios elementales**: `{1, x, x², x³, ..., xⁿ}`.
Cuando estos polinomios base, evaluados en cada abscisa `xi`, se reemplazan en el sistema de ecuaciones, la matriz de coeficientes resultante se conoce como **determinante de Vandermonde**. Este determinante es nulo (y el sistema es singular) si y solo si hay más de un punto con el mismo valor de abscisa `xi`.

**Ventajas del Método Directo**:
*   Es de **simple interpretación y formulación**.

**Desventajas del Método Directo**:
*   La **matriz de coeficientes puede estar muy mal condicionada** si hay valores de `xi` próximos.
*   Para resolver el sistema, se debe **invertir una matriz donde, en general, todos los coeficientes son distintos de cero**.
*   **No es posible representar asíntotas verticales** que puedan existir en `f(x)` en el dominio de interés.
*   Si se busca **agregar un punto**, los polinomios base cambian todos y se debe **calcular todo de nuevo**.

### 2.2 MÉTODO DE POLINOMIOS DE LAGRANGE

Los polinomios de Lagrange `lk(x)` se toman como funciones base `k(x)`. La particularidad de estos polinomios es que **valen uno en la abscisa de un punto dato de referencia y cero en las abscisas del resto de los puntos datos**. Esto significa que el resto de los puntos datos son raíces (ceros) de ese polinomio de Lagrange.

Para un punto de abscisa `xi`, el polinomio de Lagrange `li(x)` se define como:
`li(x) = ∏ [(x - xj) / (xi - xj)]` (para `j=0, n`, con `j ≠ i`).

Los polinomios de Lagrange también generan un subespacio del espacio de funciones de todos los posibles polinomios.
La interpolación con polinomios de Lagrange es:
`Pn(x) = ∑ [yk lk(x)]` (con `k=0,n`).
Esto se debe a que, utilizando estos polinomios base, **los coeficientes `ai` de la combinación lineal son directamente los valores datos `yi`**.

**Ventajas del Método de Lagrange**:
*   Es de **simple interpretación**.
*   Es **simple su implementación computacional**.
*   **No se debe invertir ninguna matriz**.
*   La **matriz de coeficientes resulta siempre diagonal**.

**Desventajas del Método de Lagrange**:
*   Si se busca **agregar un punto**, los polinomios base cambian todos y se debe **calcular todo de nuevo**.
*   Puede ser **difícil obtener una expresión simplificada** del polinomio obtenido.
*   **No es posible representar asíntotas verticales**.

### 2.3 MÉTODO DE POLINOMIOS DE NEWTON

Este método utiliza los llamados **polinomios de Newton** `k(x)` como funciones base `k(x)`. Estos polinomios se basan en los polinomios base anteriores:
*   `0(x) = 1`.
*   `k(x) = k-1(x)·(x - xk-1)` para `k ≥ 1`.

Al reemplazar estos polinomios base de Newton en el sistema de ecuaciones, la matriz de coeficientes resultante permite obtener los coeficientes de la combinación lineal `ak` por **sustitución hacia adelante**. Estos coeficientes `ak` se conocen como **Diferencias Divididas de Newton**.

**Ejemplo Resuelto:**
Para los puntos `(1, 2)`, `(2, -3)` y `(5, 6)`:
*   `a0 = f(x0) = 2`.
*   `a1 = (f(x1) - f(x0)) / (x1 - x0) = (-3 - 2) / (2 - 1) = -5`.
*   `a2 = (((f(x2) - f(x1))/(x2 - x1)) - ((f(x1) - f(x0))/(x1 - x0))) / (x2 - x0) = ((6 - (-3))/(5 - 2) - (-5)) / (5 - 1) = (9/3 - (-5)) / 4 = (3 + 5) / 4 = 8 / 4 = 2`.
El polinomio es `P2(x) = a0 + a1(x - x0) + a2(x - x0)(x - x1)`.
Sustituyendo los valores: `P2(x) = 2 + (-5)(x - 1) + 2(x - 1)(x - 2)`.

**Ventajas del Método de Newton**:
*   Es de **simple interpretación**.
*   Es **simple su implementación computacional**.
*   **No se debe invertir ninguna matriz**.
*   Si se **agrega un punto**, los polinomios base **no cambian** y es fácil calcular el nuevo coeficiente; **no es necesario calcular todo de nuevo**.

**Desventajas del Método de Newton**:
*   Puede ser **difícil obtener una expresión simplificada** del polinomio obtenido.
*   **No es posible representar asíntotas verticales**.

### 2.4 ERROR DE INTERPOLACIÓN

El **Error de interpolación** `E(x)` es la diferencia entre la función `f(x)` y el polinomio de interpolación `Pn(x)`:
`E(x) = f(x) - Pn(x)`.
Esta función `E(x)` tiene `(n+1)` ceros, ya que en cada `xi` dato, `f(xi)` y `Pn(xi)` coinciden. Puede expresarse como un polinomio de al menos grado `(n+1)`:
`E(x) = C (x-x0)(x-x1)...(x-xn)`.

La constante `C` se determina para que la función auxiliar `W(x) = f(x) - Pn(x) - E(x)` sea cero para cualquier `x`. Tras aplicar el teorema de Rolle y propiedades de la diferenciación, se obtiene que `C` se relaciona con la `(n+1)`-ésima derivada de `f(x)`:
`C = f^(n+1)(ξ) / (n+1)!` (con `ξ` entre `x0` y `xn`).

Así, el error de interpolación se puede expresar como:
`E(x) = [(x-x0)(x-x1)...(x-xn) * f^(n+1)(ξ)] / (n+1)!`.

Esta expresión establece que:
*   El **error de interpolación en las abscisas datos es cero**.
*   La **interpolación es exacta si `f(x)` es un polinomio hasta de grado n**.

### 2.5 MÉTODO DE POLINOMIOS DE HERMITE

Uno de los inconvenientes de la interpolación con polinomios de Lagrange o Newton de grado superior al 4 son las **oscilaciones entre los puntos datos**. Para evitar esto, el método de Hermite **interpola no solo los valores de la función `y=f(x)` sino también los de su primera derivada `y'=f'(x)`**, que deben estar dados como datos.

Esto permite imponer `2n+2` condiciones (`P(xi)=yi` y `P'(xi)=y'i` para `i=0,n`), lo que a su vez permite determinar `2n+2` coeficientes. Así, el **polinomio resultante será de grado `2n+1`**.

Los polinomios de Hermite resultan de interpolar el valor de la función y su derivada primera **entre dos puntos**. Conociendo `(xi, yi)`, `(xi+1, yi+1)`, `(xi, y'i)` y `(xi+1, y'i+1)`, se tienen **cuatro condiciones** para un **polinomio cúbico**:
`P(x) = a0 + a1x + a2x² + a3x³`.
`P'(x) = a1 + 2a2x + 3a3x²`.

Al imponer las cuatro condiciones, se obtiene un sistema de ecuaciones lineales para los coeficientes `a0, a1, a2, a3`.

## 3 INTERPOLACIÓN CON SPLINES CÚBICOS

Dados `n+1` puntos o nodos `(xi, yi)` (con `i=0, ..., n`), se busca una **función spline `S(x)` de grado `k`** que cumpla ciertos requisitos:

*   `S(x)` es un **polinomio de grado `≤ k` en cada subintervalo** `[xi, xi+1]`.
*   `S(x)` tiene **derivada continua de orden `k-1` en todo el intervalo** `[x0, xn]`.
*   `S(x)` es un polinomio continuo en `[x0, xn]` de grado `≤ k`, con derivadas continuas de orden `k-1`, pero **definido por tramos**.

Los **splines más usados son los cúbicos**, que tienen las siguientes características:
*   En cada subintervalo `[xi, xi+1]`, el polinomio `Si(x)` es **cúbico** (4 coeficientes a determinar).
*   Existe **continuidad de `S(x)`, su derivada primera `S'(x)`, y su derivada segunda `S''(x)`** en todos los puntos del intervalo `[x0, xn]`.

Las condiciones disponibles son:
*   `2n` condiciones por el paso del polinomio por los puntos datos (`Si(xi)=yi` y `Si(xi+1)=yi+1` en `n` subintervalos).
*   `n-1` condiciones por la continuidad de `S'(x)` en los nodos interiores (`S'i-1(xi) = S'i(xi)` en `n-1` puntos).
*   `n-1` condiciones por la continuidad de `S''(x)` en los nodos interiores (`S''i-1(xi) = S''i(xi)` en `n-1` puntos).
Esto suma `4n-2` condiciones para `4n` coeficientes. Las **dos condiciones adicionales** se eligen según convenga.

Se define `S''(xi)=zi` y `S''(xi+1)=zi+1`. La curvatura `S''(x)` se puede escribir como una interpolación lineal entre `zi` y `zi+1`. Integrando `S''(x)` dos veces, y aplicando las condiciones de paso por los puntos datos, se obtienen las expresiones para `Si(x)` y `S'i(x)` en función de `yi, yi+1, zi, zi+1` y la longitud del intervalo `hi = xi+1-xi`.

La condición de continuidad de `S'(x)` (`S'i(xi) = S'i-1(xi)`) se plantea para `i=1` hasta `n-1`, generando un sistema de `(n-1)` ecuaciones con `(n+1)` incógnitas (`zi`).
La elección que origina los **SPLINES CÚBICOS NATURALES** es `z0 = zn = 0`. Esto reduce el sistema a uno tridiagonal de `(n-1)` ecuaciones por `(n-1)` incógnitas.

## 4 MÉTODO DE MÍNIMOS CUADRADOS

En este método, dados `n` puntos `(xi, yi)`, se busca **APROXIMAR** la función `y(x)` (desconocida) mediante una combinación lineal de `m` funciones base `j(x)` (conocidas y linealmente independientes):
`fm(x) = ∑ aj j(x)` (con `j=1,m`).

**Observación 1**: A diferencia de la interpolación, aquí se considera un **número `m < n` de funciones base**. Si `m=n` y no hay puntos con la misma abscisa, este método genera el mismo polinomio que los métodos de interpolación.
**Observación 2**: Al aproximar por mínimos cuadrados, **no hay problema si dos puntos tienen la misma abscisa**.

Cuando `fm(x)` se evalúa en `xi`, aparece un **residuo** `ri`:
`ri = yi - ∑ aj j(xi)`.
Los coeficientes `aj` se determinan de manera que **minimizan la Suma de los Cuadrados de los Residuos**:
`min(∑ ri²) = min(∑ (yi - ∑ aj j(xi))²)`.

La condición para que exista el mínimo es que la derivada parcial de la suma de cuadrados respecto a cada `aj` sea cero:
`∂(∑ ri²) / ∂aj = 0` (para `j=1,m`).
Esto conduce a un **sistema de ecuaciones lineales**, cuya resolución da los coeficientes `aj` buscados. Este sistema también puede interpretarse como la **Condición de Normalidad (ortogonalidad)** entre los residuos `ri` y las funciones base `j(xi)` como vectores.

El sistema de ecuaciones para los coeficientes `aj` se expresa matricialmente como:
`Φ^T Φ a = Φ^T y`
Donde:
*   `a` es el vector de coeficientes `(a1, ..., am)^T`.
*   `y` es el vector de valores `(y1, ..., yn)^T`.
*   `Φ` es la matriz de funciones base evaluadas en los puntos `xi`.

**Casos especiales:**
*   **Aproximación Lineal**: Se usa una base `{1, x}`.
*   **Aproximación Cuadrática**: Se usa una base `{1, x, x²}`.
