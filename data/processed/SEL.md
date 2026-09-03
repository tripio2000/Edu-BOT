# Sistemas de Ecuaciones Lineales

## 1 Introducción

En **numerosos problemas de ingeniería** es fundamental **resolver sistemas de ecuaciones lineales (SEL)**. En un SEL, las incógnitas se combinan linealmente con coeficientes constantes, y esta combinación se iguala a una constante conocida. Desde la perspectiva del Álgebra Lineal, un SEL puede interpretarse como la **obtención de los coeficientes (incógnitas) que linealmente combinan vectores de una base (columnas de la matriz de coeficientes) para generar un vector conocido (término independiente)**.

Los métodos computacionales para resolver ecuaciones diferenciales de forma discreta a menudo conducen a SEL de N ecuaciones con N incógnitas. Estos métodos, como las **diferencias finitas, elementos finitos o volúmenes finitos**, son cada vez más aplicados en ingeniería, y los sistemas resultantes pueden tener un **orden N muy grande (cientos de miles o incluso millones)**. Por esta razón, es **crucial recurrir a métodos eficientes** para resolverlos.

Los métodos para resolver sistemas de ecuaciones lineales se dividen principalmente en dos grandes grupos: **métodos de factorización** y **métodos iterativos**.

## 2 Métodos de Factorización

Los métodos de factorización son **particularmente útiles** en dos escenarios:
*   Cuando la **matriz de coeficientes tiene pocos ceros** (denominada "matriz llena").
*   Cuando, con la **misma matriz de coeficientes, se deben resolver varios sistemas** en los que solo cambia el término independiente.

Existen numerosos métodos de factorización basados en propiedades de la matriz de coeficientes o sus equivalentes. Algunos ejemplos incluyen **Doolittle, Crout y Cholesky**.

### 2.1 Método de Factorización LU

Una matriz `A` puede factorizarse en una **matriz triangular inferior `L` (lower)** y una **triangular superior `U` (upper)** si y solo si el sistema lineal `A x = b` puede resolverse de manera única por eliminación de Gauss.

El proceso para resolver un SEL `A x = b` mediante factorización LU es el siguiente:
1.  **Dado:** `A x = b`.
2.  **Factorización:** `A = L U`.
3.  **Sustitución:** `(L U) x = b`.
4.  **Propiedad asociativa:** `L (U x) = b`.

Se definen tres fases:
*   **Primera Fase: Descomposición en LU**: `L U = A`.
*   **Segunda Fase: Sustitución Progresiva**: Si se define `(U x) = z`, entonces `L z = b`. A partir de `L` y `b`, se obtiene el vector `z` por sustitución progresiva.
*   **Tercera Fase: Sustitución Regresiva**: Con `(U x) = z`, se obtiene el vector `x` por sustitución regresiva.

La obtención de los coeficientes de las matrices triangulares `L` y `U` se basa en el método de eliminación de Gauss. La sistematización de este proceso da origen a los métodos de **Crout y Doolittle**. Para este curso, se adopta el método de Doolittle.

Una ventaja clave de este método es que **cuando el término independiente `b` cambia, solo se necesitan realizar las fases 2 y 3** para obtener la nueva solución, lo que simplifica el cálculo de la matriz inversa del sistema.

### 2.2 Método de Doolittle

El método de Doolittle busca factorizar `A = L U` imponiendo la condición de que los **elementos diagonales de `L` sean 1** (`l_ii = 1`). Un elemento `a_ij` de la matriz `A` es igual al producto escalar de la i-ésima fila de `L` por la j-ésima columna de `U`.

Los pasos de resolución son:
1.  **Multiplicar la fila 1 de L por todas las columnas de U** para obtener los elementos `u_1j`.
2.  **Multiplicar las filas restantes de L por la columna 1 de U** para obtener los elementos `l_i1` (donde `l_i1 * u_11 = a_i1`).
3.  **Continuar con la fila 2 de L por las columnas de U**, omitiendo la primera, para obtener la fila 2 de U (`u_2j = a_2j - l_21 * u_1j`).
4.  **Multiplicar las filas restantes de L por la columna 2 de U**.
5.  En **forma general**, para cada paso `r` (desde 1 hasta N), se calculan los elementos de `U` (`u_rj`) y luego los elementos de `L` (`l_ir`).

**Procedimiento sintetizado**:
1.  Determinar los coeficientes de la **primera fila de U** (desde el elemento diagonal hacia la derecha). Luego los de la **primera columna de L** (desde el elemento diagonal hacia abajo).
2.  Determinar los coeficientes de la **segunda fila de U** (desde el elemento diagonal hacia la derecha). Luego los de la **segunda columna de L** (desde el elemento diagonal hacia abajo).
3.  Y así sucesivamente hasta terminar todas las filas y columnas.

### 2.3 Síntesis del Método de Doolittle

Dada una matriz `A` de `NxN`, los elementos de `L` y `U` se buscan como `A = L U`.
Se realizan `N` pasos (`r` de 1 a `N`):
*   Para los elementos de **U**: `u_rj = a_rj - sum(l_rk * u_kj)` para `j = r, ..., N`.
*   Para los elementos de **L**: `l_ir = (a_ir - sum(l_ik * u_kr)) / u_rr` para `i = r+1, ..., N`.

Una vez que `L` y `U` han sido determinadas, se procede con:
*   **Sustitución progresiva para obtener `z`**: `z_i = (b_i - sum(l_ik * z_k)) / l_ii` para `i = 1, ..., N`.
*   **Sustitución regresiva para obtener `x`**: `x_i = (z_i - sum(u_ik * x_k)) / u_ii` para `i = N, ..., 1`.

### 2.4 Planteo del Método de Doolittle a partir de Matrices Elementales

Es posible obtener una matriz equivalente triangular superior `U` a partir de una matriz `A` mediante **operaciones elementales de filas**. Estas operaciones consisten en reemplazar una fila por una combinación lineal de esa fila y otra, con un coeficiente que anule un elemento específico.

Cada operación elemental puede ser representada por una **matriz elemental `E_k`** que, al premultiplicar `A`, produce la matriz modificada. Por ejemplo, para anular `a_21`, se usa `E_1` tal que `A_r1 = E_1 A`. Si `A_r3 = E_3 E_2 E_1 A` es la matriz triangular superior `U`, entonces se puede escribir `U = P A` donde `P` es el producto de todas las matrices elementales (`P = E_3 E_2 E_1`).

Premultiplicando por la inversa de `P`, se obtiene `A = P^-1 U`. La matriz `P^-1` es el producto de las inversas de las matrices elementales (`P^-1 = E_1^-1 E_2^-1 E_3^-1`). Es importante destacar que las inversas de las matrices elementales son **triangulares inferiores y simples de calcular** (cambiando el signo del coeficiente no nulo fuera de la diagonal). Por lo tanto, `P^-1` resulta ser la matriz triangular inferior `L` buscada en el método de Doolittle.

Aunque este planteo ilustra la relación teórica, **no es una forma práctica para la implementación computacional**; el algoritmo presentado en la sección 2.3 es más conveniente.

### 2.5 Cálculo de la Matriz Inversa Aplicando Doolittle

La factorización `L` y `U` puede usarse para calcular la matriz inversa `A^-1` de una matriz `A` de `NxN`.

#### 2.5.1 Alternativa Directa

Dado que `A * A^-1 = I` (matriz identidad), cada columna `a_k` de `A^-1` se obtiene resolviendo un sistema de ecuaciones `A * a_k = i_k`, donde `i_k` es la k-ésima columna de la matriz identidad.

Utilizando la factorización LU:
*   Se obtiene `z` por sustitución progresiva (`L z = i_k`).
*   Luego, se obtiene `a_k` por sustitución regresiva (`U a_k = z`).
Este proceso requiere **N sustituciones progresivas y regresivas** para obtener todas las columnas de la matriz inversa.

#### 2.5.2 Alternativa Indirecta

Con la factorización `A = L U`, se sabe que `A^-1 = U^-1 L^-1`.
*   La matriz `L^-1 = C` se obtiene resolviendo `L C = I`, donde cada columna de `C` se halla por sustitución progresiva tomando como término independiente cada columna de `I`.
*   La matriz `U^-1 = D` se obtiene resolviendo `U D = I`, donde cada columna de `D` se halla por sustitución regresiva tomando como término independiente cada columna de `I`.
Así, las inversas de `L` y `U` se obtienen mediante **simples sustituciones hacia adelante y hacia atrás**, respectivamente.

## 3 Métodos Iterativos

Los métodos iterativos son una alternativa a la eliminación de Gauss, **especialmente útiles y eficientes** cuando:
*   El **número de ecuaciones es grande** (generalmente N > 50).
*   La **matriz de coeficientes es "rala"** (tiene muchos elementos nulos).
Estos métodos insumen **menor tiempo de proceso** y alcanzan los objetivos con **menos complejidad de cálculo** en estos escenarios.

### 3.1 Método de Jacobi

También conocido como **Iteración de Jacobi** o **Método de los Desplazamientos Simultáneos**.
Comienza con una **aproximación inicial `x^(0)`** al vector solución `x` y genera una **serie de vectores `x^(k)`** que converge hacia `x`.

El método transforma el sistema `A x = b` en una forma equivalente: **`x^(k) = T x^(k-1) + c`**.
Para un SEL de `n x n`, la i-ésima ecuación se resuelve para `x_i^(k)` siempre que `a_ii` sea distinto de cero:
`x_i^(k) = (b_i - sum(a_ij * x_j^(k-1) for j != i)) / a_ii`.

**Criterios de detención**:
*   Una **tolerancia máxima de error** (`|x^(k) - x^(k-1)| / |x^(k)| < ε`). Generalmente se utiliza la **norma infinita**.
*   Un **número máximo de iteraciones**.

**Consideraciones**:
*   **`a_ii` debe ser siempre distinto de cero**. Si no, se debe reorganizar el sistema.
*   Se recomienda que los valores de la diagonal sean lo **más grandes posible** para lograr una **convergencia más veloz**.
*   El método **solo se aproxima a la solución**, alcanzándola teóricamente solo con infinitas iteraciones.

### 4) Método de Gauss Seidel

Es una **mejora del Método de Jacobi**. La principal diferencia es que, al calcular `x_i^(k)`, se utilizan los **valores actualizados (recién calculados) de las componentes `x_r^(k)` para `r < i`** en la misma iteración, en lugar de los valores de la iteración anterior `x_r^(k-1)`.

La fórmula de recurrencia para `x_i^(k)` es:
`x_i^(k) = (b_i - sum(a_ij * x_j^(k) for j < i) - sum(a_ij * x_j^(k-1) for j > i)) / a_ii`.
Esta actualización inmediata de valores puede llevar a una **convergencia más veloz** en muchos casos. Sin embargo, **no siempre es mejor que Jacobi**, y hay sistemas que pueden ser resueltos por uno pero no por el otro.

**Estudio de la convergencia**:
Para que las soluciones converjan, una condición importante es que los **términos de la diagonal principal sean dominantes**. Es decir, para cada fila `i`, el valor absoluto del elemento `a_ii` debe ser mayor o igual a la suma de los valores absolutos de los otros elementos en esa fila (`|a_ii| >= sum(|a_ij| for j != i)`). Si esta desigualdad es **estrictamente mayor para al menos una fila**, el método converge.
*   Si las "pendientes" (`m_1`, `m_2`) tienen el **mismo signo**, hay convergencia hacia un solo lado.
*   Si las "pendientes" tienen **signos distintos**, hay convergencia oscilante.

## 4 Planteo Alternativo para el Método Iterativo de Jacobi

Dado el sistema `A x = b`, donde `A` es una matriz `NxN` y `b` un vector `N`.
Es posible reescribir `A` como `A = D + L + U`, donde `D` es la matriz diagonal, `L` la parte triangular inferior (con ceros en la diagonal), y `U` la parte triangular superior (con ceros en la diagonal) [Not in source, but implied by the alternative formulation, I will flag this as external].
El sistema `(D + L + U) x = b` se puede reorganizar para Jacobi como `D x = b - (L + U) x` [Not in source, but implied].
De donde se obtiene la forma iterativa: **`x^(k) = D^-1 (b - (L + U) x^(k-1))`**.
Se puede iterar con esta fórmula hasta que el error sea tan pequeño como se desee.

## 5 Planteo Alternativo para el Método Iterativo de Gauss Seidel

A partir del método de Jacobi, `x^(k) = T x^(k-1) + c`.
El método de Gauss-Seidel se puede expresar como **`x^(k) = T_l x^(k) + T_s x^(k-1) + c`**.
Donde `T_l` representa la parte de `T` que utiliza las componentes `x_j^(k)` ya calculadas en la iteración actual, y `T_s` utiliza las componentes `x_j^(k-1)` de la iteración anterior.

**Características clave de la actualización en Gauss-Seidel**:
*   Para calcular `x_1^(k)`, se utilizan todas las componentes de `x^(k-1)`.
*   Para calcular `x_2^(k)`, se utiliza `x_1^(k)` (recién calculado) y las demás componentes de `x^(k-1)`.
*   Este patrón continúa: para `x_i^(k)`, se utilizan `x_1^(k), ..., x_{i-1}^(k)` y `x_{i+1}^(k-1), ..., x_N^(k-1)`.
Así, `x_N^(k)` se calcula utilizando todas las componentes `x_1^(k), ..., x_{N-1}^(k)` ya actualizadas en la iteración actual.

---

**Nota:** La descomposición de la matriz `A` en `D`, `L`, `U` para las formulaciones alternativas de Jacobi y Gauss-Seidel (`A = D + L + U`, donde `D` es la matriz diagonal, `L` la parte triangular inferior y `U` la parte triangular superior) es una práctica común en el análisis de métodos iterativos, aunque no se explicita en las fuentes proporcionadas.
