# INTEGRACIÓN NUMÉRICA

## 1 ACERCA DE LOS PROBLEMAS DE LA INTEGRACIÓN Y LA DERIVACIÓN NUMÉRICAS EN GENERAL

En diversas aplicaciones de la matemática, es fundamental calcular el valor de la **derivada de una función en un punto** o la **integral de una función** conocida analíticamente. Si bien estas operaciones suelen ser directas, pueden volverse complejas o difíciles de implementar computacionalmente en ciertas circunstancias.

El desafío se acentúa cuando la función se conoce de forma **discreta**. El objetivo de esta unidad es abordar el cálculo de **integrales definidas** de funciones dadas de forma analítica o discreta. Se asume que la función `y = f(x): R -> R` es **no singular** y **continua** (al menos por tramos) en el intervalo `[x0;xn]`.

Cuando `f(x)` se da de forma discreta (conocida en puntos `xi`, `i = 0,1,2,...,n`), es posible **interpolarla** con un polinomio `Pn(x)` de grado `n` que pase por `n+1` puntos datos. Si `f(x)` es analítica, se pueden "extraer" `n+1` puntos evaluando `f(x)` en `xi` para obtener `(xi; yi = f(xi))`.

La función `f(x)` puede expresarse como:
`f(x) = Pn(x) + En(x)`
Donde `En(x)` es el **error de interpolación**, dado por `(x-x0)...(x-xn) * f^(n+1)(xi) / (n+1)!`.
Cualquier operador lineal `L[x]` (como la integral o la derivada) aplicado a `f(x)` resulta en:
`L[f(x)] = L[Pn(x)] + L[En(x)]`.

## 2 INTEGRACIÓN NUMÉRICA

El objetivo principal es encontrar la **integral definida** `I` en `R`, dada por `I = Integral from X0 to Xn of f(x) dx`.
Basándose en la relación `Integral(f(x)dx) = Integral(Pn(x)dx) + Integral(En(x)dx)`, la integral definida `I` se evalúa como la suma:
`I = In + En`
Donde `In` se denomina **cuadratura** y `En` es el **error de truncamiento**.

Todos los métodos de integración numérica comparten la estructura en la que la cuadratura `In` se expresa como una suma:
`In = sum(wj * f(xj))`
Los **coeficientes `wj`** se determinan según cada regla. El **orden de la regla de cuadratura** se define como el máximo grado del polinomio que dicha regla integra de forma exacta, es decir, para el cual `En = 0`.

Existen dos tipos principales de cuadratura:

### 2.1 Cuadratura de Newton-Cotes

En esta cuadratura, los **valores `xj`** donde se conoce `f(xj)` son **predeterminados** (datos fijos para la regla de integración). Los coeficientes `wj` se determinan para estos `xj`. El **paso** (distancia entre abscisas dato) puede ser fijo o variable.

### 2.2 Cuadratura de Gauss-Legendre

En contraste con Newton-Cotes, tanto los **valores `xj` como los coeficientes `wj`** se determinan en cada regla de integración.

## 3 REGLAS DE INTEGRACIÓN DE NEWTON - COTES

Para una función `y = f(x): R -> R` dada en forma discreta mediante `n+1` puntos `(Xi ; Yi)`, `i = 0,...,n`, se utiliza un **polinomio de grado `n`** por el método de **polinomios de Lagrange**.
`Pn(x) = sum(Yi * li(x))`
Donde cada **polinomio base `li(x)`** es `product((x-xj)/(xi-xj))`.
El grado del polinomio `Pn` y la cantidad de polinomios base `li(x)` dependen del número de puntos datos `(n+1)`.

La integral se expresa como `I = In + En`, donde:
`In = Integral from X0 to Xn of Pn(x) dx = sum(Yi * Integral from X0 to Xn of li(x) dx)`
`En = Integral from X0 to Xn of En(x) dx = Integral from X0 to Xn of (x-x0)...(x-xn) * f^(n+1)(xi) / (n+1)! dx`
El **error `En`** es proporcional a la derivada de orden `(n+1)` de la función a integrar y al valor de la integral del primer polinomio (grado `n+1`) para el cual se comete error.

Los diferentes métodos surgen de interpolar mediante polinomios de distintos grados.

### 3.1 Regla de los Trapecios

La **regla de los trapecios** es una regla de integración de **orden 1**, lo que significa que es exacta para polinomios de grado 1. Permite aproximar la integral `I` mediante la fórmula:
`I = h/2 * (Yi + Yi+1) - h^3/12 * f''(xi)`
Donde `xi` es un valor entre `xi` y `xi+1`.

Se exploran cuatro formas de desarrollo y cálculo del error para esta regla:

#### 3.1.1 Desarrollo de la Regla de los Trapecios mediante Integración Del Polinomio Interpolante

Es una regla de Newton-Cotes que utiliza **2 puntos** `(xi;yi), (xi+1;yi+1)`. Se interpola la función `f(x)` mediante un polinomio de grado 1 (`P1(x)`).
La fórmula resultante para el intervalo `[xi, xi+1]` es:
`Ii = h/2 * (Yi + Yi+1)`
Donde `h` es el paso `(xi+1 - xi)`.

#### 3.1.2 Cálculo del Error en la Regla De Trapecios a partir del Error de Interpolación

El error `E1` al calcular la integral definida de `f(x)` entre `xa` y `xb` por el método de los trapecios se deriva de la integral del error de interpolación `E1(x)`.
Al realizar un cambio de variable al dominio `t` en ``, se obtiene la expresión del error:
`E1 = -h^3/12 * f''(xi)` para cierto punto `xi` en `(xa, xb)`.
Se dice que el **error en la regla de trapecios es del orden de `h^3`: O(h^3)**. Es importante no confundir el orden de la regla de integración (1) con el orden del error (O(h^3)).

#### 3.1.3 Cálculo Del Error De La Regla De Los Trapecios usando Serie De Taylor

Partiendo de la definición `E1 = I - I1` y desarrollando la función primitiva `G(x)` en serie de Taylor alrededor de `xi`, se confirma que el **error en la regla de trapecios es O(h^3)**.

#### 3.1.4 Regla De Los Trapecios Por El Método De Los Coeficientes Indeterminados

Este método busca determinar los coeficientes `a0` y `a1` de la expresión `Integral(G(t)dt) = a0*G(0) + a1*G(1) + R` (donde R es el error) de manera que la regla sea exacta para las funciones `{1, t}`.
Se obtiene `a0 = a1 = 1/2`.
El error de truncamiento `R` se determina aplicando la regla a polinomios de grado superior (cuadráticos, en este caso). Se llega a que `R = -h^2/12 * f''(xi)`.
La regla de los trapecios completa es:
`Integral from Xi to Xi+1 of f(x) dx = h/2 * (Yi + Yi+1) - h^3/12 * f''(xi)`.

**Ejemplo:** `f(x) = sen(x)`. Integrando de `0` a `pi/2` (exacto = 1) y de `0` a `pi` (exacto = 2).
Para `h = pi/2`: `I1 = pi/4 = 0.7854`.
Para `h = pi`: `I1 = 0`.

### 3.2 Regla De Los Trapecios Múltiple o Trapecios Compuesta

Para calcular `Integral from X0 to Xn of f(x) dx`, el intervalo `[x0; xn]` se divide en `n` subintervalos `[x0; x1], [x1; x2], ..., [xn-1; xn]`. Se aplica la regla de los trapecios simple en cada subintervalo y se suman los resultados.
Si todos los intervalos tienen la misma longitud `h`, la fórmula se simplifica a la **regla de trapecios múltiple**:
`I = h/2 * (Y0 + 2*sum(Yi for i=1 to n-1) + Yn) + E1M`
Donde `E1M` es el error total acumulado.

El **error `E1M`** se aproxima como:
`E1M = - (xn - x0) * h^2/12 * f''(xi)`
El **orden del error** para la regla de trapecios múltiple es `O(h^2)`. Al pasar de la regla simple (O(h^3)) a la compuesta (O(h^2)), la precisión disminuye.

### 3.3 Algoritmo De Trapecios Múltiples

Se presentan pseudo-códigos para la implementación de la regla de trapecios múltiples, tanto para funciones dadas en **forma discreta** (tabla de valores x, y) como para funciones dadas en **forma analítica**.

*   **Algoritmo trapecios-múltiples-discreta:** Lee valores X e Y, calcula la suma ponderada de Y, determina `h` y la integral final.
*   **Algoritmo Trapecios-múltiples-Equidistante-analítica:** Define la función `f(x)`, calcula `h`, y suma los valores de `f(x)` ponderados.

### 3.4 Regla de Simpson

La **regla de Simpson** es una regla de **orden 3**, lo que significa que integra de forma exacta polinomios de grado hasta 3. Permite aproximar la integral `I` mediante la fórmula:
`I = h/3 * (f(x0) + 4*f(x1) + f(x2)) - h^5/90 * f^(4)(xi)`
Donde `xi` es un valor entre `x0` y `x2`.

#### 3.4.1 Regla de Simpson mediante integración del polinomio interpolante

Es una cuadratura de Newton-Cotes con `n=2`, es decir, utiliza **tres puntos**. Se interpola la función con un polinomio de Lagrange de grado dos y se integra este polinomio de forma aproximada.
Si los intervalos son iguales (`h1 = h2 = h`), la fórmula de Simpson es:
`I = h/3 * (Y0 + 4*Y1 + Y2)`

#### 3.4.2 Regla De Simpson Por El Método De Los Coeficientes Indeterminados

Se busca normalizar la integral al dominio `t` en `[-1, 1]`. Se propone resolver la integral de `G(t)` con coeficientes indeterminados `C-1, C0, C1` de manera que la regla sea exacta para `{1, t, t^2}`.
Se obtienen los coeficientes: `C-1 = 1/3`, `C0 = 4/3`, `C1 = 1/3`.
Esto lleva a la misma fórmula: `I = h/3 * (Y0 + 4*Y1 + Y2)`.

#### 3.4.3 Regla de Simpson - error

El error de truncamiento `R` se determina aplicando la regla a polinomios de grado superior. Se encuentra que la regla es exacta incluso para polinomios de grado 3. Para polinomios de grado 4, se obtiene el error:
`R = -h^5/90 * f^(4)(xi)`
El **orden del error** para la regla de Simpson es **`O(h^5)`**.

### 3.5 Regla de Simpson Compuesta

La regla de Simpson compuesta se obtiene sumando aplicaciones sucesivas de la regla de Simpson simple. La fórmula es:
`I = h/3 * (f(x0) + 4*sum(f(xi) for odd i) + 2*sum(f(xi) for even i) + f(xn))`
Similar a la regla de los trapecios, al pasar de la regla de Simpson simple (O(h^5)) a la compuesta, el **orden del error disminuye** a **`O(h^4)`**.

## 4 CUADRATURA DE GAUSS

En la **cuadratura de Gauss**, el problema se plantea en el **dominio unitario `[-1, 1]`**. Este método busca determinar tanto los coeficientes como los puntos de evaluación de la función. La idea es hallar los valores de abscisas `t1, t2, ...` y coeficientes `w1, w2, ...` para aproximar la integral `Integral from -1 to 1 of G(t) dt`.

#### 4.1 Regla De Dos Puntos Usando el Método De Coeficientes Indeterminados

Para la regla de dos puntos, se proponen `w1*G(t1) + w2*G(t2)`. Los valores `w1, w2, t1, t2` se determinan de manera que el error de integración sea `R = 0` para polinomios de hasta 3er grado.
Las soluciones son: `t1 = -1/sqrt(3)`, `t2 = 1/sqrt(3)`, `w1 = 1`, `w2 = 1`.
La regla queda: `I = h * (f(c - h/sqrt(3)) + f(c + h/sqrt(3)))`.

#### 4.2 Generalización de la regla anterior

La regla de dos puntos se puede generalizar a más puntos. Se proporciona una tabla con las abscisas (`ti`) y coeficientes (`wi`) para 2, 3 y 4 puntos de Gauss, y el orden de la derivada del error de truncamiento.

*   **2 puntos:** Abscisas `+-0.577350269`, Coeficientes `1.0`, Orden de error `4`.
*   **3 puntos:** Abscisas `0`, `+-0.774596669`, Coeficientes `0.8888889`, `0.5555556`, Orden de error `6`.
*   **4 puntos:** Abscisas `+-0.339981044`, `+-0.861136312`, Coeficientes `0.6521452`, `0.3478548`, Orden de error `8`.

## 5 EXTRAPOLACIÓN DE RICHARDSON

La **extrapolación de Richardson** es una técnica para **mejorar la aproximación de una integral** (o derivada) cuando se tienen dos aproximaciones obtenidas con pasos diferentes (`h1` y `h2`).
Si una regla tiene un error del orden de `h^n`, y `h2 = h1 / R` (donde R es un factor), la mejorada integral `I_mejorado` se calcula como:
`I_mejorado = (R^n * I(h_small) - I(h_large)) / (R^n - 1)`
El error de la nueva aproximación es de un orden superior. Por ejemplo, para la regla de trapecios compuesta (error `O(h^2)`), la extrapolación de Richardson da un error `O(h^4)`. Para la regla de Simpson compuesta (error `O(h^4)`), el error resultante es `O(h^6)`.

## 6 INTEGRACIÓN DE ROMBERG

La **integración de Romberg** es un método que aplica **sucesivas extrapolaciones de Richardson** sobre una serie de aproximaciones obtenidas con la **regla de trapecios múltiples**, utilizando pasos que se reducen a la mitad.
La fórmula general para las mejoras es:
`Ij,k = (4^(k-1) * Ij+1,k-1 - Ij,k-1) / (4^(k-1) - 1)`
Donde `j` es el nivel de divisiones por la mitad del paso original y `k` indica el nivel de extrapolación.
El criterio de parada para las iteraciones es que la diferencia relativa entre aproximaciones consecutivas sea menor que una tolerancia `Epsilon` o que se alcance un número máximo de iteraciones.

### 6.1 Algoritmo de Romberg

Se presenta un pseudo-código para la integración de Romberg. Este algoritmo calcula las aproximaciones trapezoidales para diferentes pasos (`h`), y luego aplica las extrapolaciones de Richardson en cascada para obtener una solución mejorada.

**Ejemplo:** Integración de `sen(x)` de `0` a `pi`. Se muestra una tabla que ilustra cómo las aproximaciones mejoran con cada nivel de extrapolación, reduciendo el orden del error progresivamente de `O(h^2)` a `O(h^12)`.
