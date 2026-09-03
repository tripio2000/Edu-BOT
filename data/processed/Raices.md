# Solución Numérica de Raíces de Ecuaciones No Lineales

## 1 Introducción

En diversas aplicaciones de la ingeniería, es **frecuente la necesidad de encontrar los valores de variables que anulan una función conocida**. Esto ocurre, por ejemplo, al buscar los valores que anulan el polinomio característico de una matriz para determinar sus autovalores, o al buscar los valores que anulan funciones trascendentes en la determinación de estados inestables de sistemas conservativos o frecuencias naturales de sistemas dinámicos.

El problema matemático se formula como: dada una función continua y=f(x) de R → R, se busca x=r tal que **f(r)=0**. Geométricamente, esto significa encontrar el punto de abscisa `r` y ordenada `0` que verifica la relación funcional `0=f(r)`. Este punto solución se denomina **raíz de la ecuación no lineal**, y la función `f(x)` igualada a cero es la ecuación no lineal.

Mientras que para ecuaciones polinómicas de grado 2 o 3 existen fórmulas explícitas para calcular las raíces, esto no es común para polinomios de grado superior a 3 o para ecuaciones trascendentes (que incluyen expresiones trigonométricas). Por ello, se utilizan **métodos iterativos** para resolver este tipo de problemas.

Para un análisis detallado de los métodos, se recomienda consultar el texto "Métodos Numéricos para Ingenieros" de S. Chapra y R. Canale.

## 2 Procedimiento General

Para encontrar las raíces de una ecuación no lineal, se sugieren los siguientes pasos:

*   **Paso Inicial: Análisis de la función**.
    *   Se busca determinar singularidades, posibles discontinuidades, asíntotas y toda la información relevante para una elección adecuada de las variables iniciales de los procesos iterativos.
*   **Paso de Acercamiento: Encontrar un intervalo**.
    *   Se trata de localizar un intervalo en el eje X donde exista al menos una raíz de la ecuación no lineal.
    *   Para funciones continuas en un intervalo `[ak; bk]`, una condición necesaria es que la función **cambie de signo al menos una vez** dentro del intervalo.
    *   Si `f(ak) * f(bk) < 0`, entonces existe al menos una raíz `X = r` en el intervalo `[ak; bk]`.

*   **Paso de Aproximación: Métodos Iterativos**.
    *   Estos métodos generan una sucesión de soluciones aproximadas que, bajo ciertos requisitos, se acercan cada vez más a la solución exacta, reduciendo el error en cada iteración.
    *   Los métodos más difundidos se clasifican en:
        *   **Métodos de Intervalos**:
            *   Método de Bisección.
            *   Método de Regula Falsi.
        *   **Métodos Abiertos**:
            *   Método de la Secante o de Newton Lagrange.
            *   Método de Newton.
            *   Métodos de Puntos Fijos.

## 3 Métodos Iterativos en General

Los métodos iterativos poseen las siguientes características fundamentales:

*   **Condición de Inicialización**: Requisitos que deben cumplirse para que la sucesión de soluciones aproximadas converja a la solución exacta. Por ejemplo, la función debe ser continua en el entorno de trabajo, y en los métodos de intervalos, debe conocerse un intervalo donde la función sea continua y cambie de signo en sus extremos.
*   **Fórmula de Recurrencia**: Son las fórmulas que se utilizan para generar los elementos de la sucesión de soluciones aproximadas.
*   **Controles de Detención**: Condiciones que permiten detener el procedimiento. Generalmente se expresan como medidas del error (absolutas o relativas) o del proceso de convergencia, comparando con valores admisibles de error. Esto permite que el proceso iterativo sea tan preciso como se desee.
*   **Actualización de Variables**: Reasignación de las variables de trabajo para cumplir las condiciones de inicialización y permitir un nuevo ciclo o iteración.

**Síntesis Algorítmica General**:
*   **INICIALIZACIÓN**: Definir contenidos de variables para cumplir condiciones de inicialización del método.
*   **HACER MIENTRAS (No Hay Solución es Verdadero)**:
    *   **RECURRENCIA**: Evaluar la nueva solución aproximada (rk+1).
    *   **CONTROL DE DETENCIÓN**: Si una medida de error es adecuada, se ha encontrado la solución buscada (NHS = FALSO).
        *   `SI (Valor Absoluto de f(rk+1) < Tolerancia) ENTONCES NHS es FALSO FINSI`.
    *   **ACTUALIZACIÓN DE VARIABLES**: Reasignar variables para cumplir condiciones de inicialización.
*   **FIN DEL HACER MIENTRAS**.

## 4 Síntesis de los Distintos Métodos

### 4.1 Método de Bisección

*   **Inicialización**: Se requieren dos abscisas `x=ak` y `x=bk` que definan un intervalo `[ak; bk]` donde la función no lineal `f(x)` tenga al menos una raíz, es decir, `f(ak) * f(bk) < 0`.
*   **Recurrencia**: La aproximación de la raíz `rk+1` se calcula como la **abscisa media** de dicho intervalo: `rk+1 = (ak + bk) / 2`.
*   **Control de Detención**: Se verifica si `|f(rk+1)| < ε`, donde `ε` es una magnitud pequeña. Alternativamente, se controla si `|rk+1 - ak| < ε` o `| (rk+1 - rk) / rk+1 | < ε`. También es útil fijar un número máximo de iteraciones (`MaxIter`).
*   **Actualización de Variables**: Se definen dos nuevos subintervalos `[ak; rk+1]` y `[rk+1; bk]`. Se selecciona el intervalo que cumple la condición de inicialización (`f(ak) * f(rk+1) < 0` o `f(bk) * f(rk+1) < 0`) para la siguiente iteración.

### 4.2 Método de Regula Falsi

*   **Inicialización**: Idéntica al método de Bisección (`f(ak) * f(bk) < 0`).
*   **Recurrencia**: La aproximación de la raíz `rk+1` se obtiene donde la recta que une los puntos `[ak; f(ak)]` y `[bk; f(bk)]` intersecta el eje X.
    *   `rk+1 = ak - f(ak) * (bk - ak) / (f(bk) - f(ak))`.
    *   La pendiente `m = (f(bk) - f(ak)) / (bk - ak)` es independiente del punto de referencia.
*   **Control de Detención**: Igual que en el método de Bisección.
*   **Actualización de Variables**: Igual que en el método de Bisección.

### 4.3 Método de la Secante

*   **Inicialización**: Se requieren **dos aproximaciones anteriores** de la raíz (`rk-1, rk`).
*   **Recurrencia**: La aproximación de la raíz `rk+1` se obtiene donde la recta que une los puntos `[rk-1; f(rk-1)]` y `[rk; f(rk)]` intersecta el eje X.
    *   `rk+1 = rk - f(rk) * (rk - rk-1) / (f(rk) - f(rk-1))`.
    *   Los puntos `[rk-1; f(rk-1)]` y `[rk; f(rk)]` son equivalentes a `[ak; f(ak)]` y `[bk; f(bk)]` del método de Regula Falsi para la fórmula de recurrencia.
*   **Control de Detención**: Igual que en el método de Bisección.
*   **Actualización de Variables**: Se retienen las **dos últimas aproximaciones**, lo que es una ventaja al no requerir el análisis de datos de intervalo.

### 4.4 Método de Newton Raphson

*   **Inicialización**: Se requiere **una aproximación inicial** de la raíz (`rk`).
*   **Recurrencia**: La aproximación de la raíz `rk+1` se obtiene donde la **recta tangente** a `f(x)` en el punto `[rk; f(rk)]` intersecta el eje X.
    *   `rk+1 = rk - f(rk) / f'(rk)`.
    *   La pendiente `m = f'(rk)` es la derivada de la función evaluada en `rk`.
    *   Este método es conocido por su **mayor velocidad de acercamiento a la raíz**, ya que la tangente indica la dirección de máximo cambio.
*   **Control de Detención**: Igual que en el método de Bisección.
*   **Actualización de Variables**: Se retiene la **última aproximación** obtenida.

### 4.5 Planteo Alternativo para el Método de Newton Raphson

*   Dado `y = F(x)` y buscando `xr` tal que `F(xr) = C` (constante). Esto se puede reescribir como `f(x) = C - F(x) = 0`.
*   Se considera una expansión en Serie de Taylor de `f(x)` alrededor de `xk`. Truncando los términos de orden superior, se puede plantear `f(xk) + f'(xk) * (xk+1 - xk) = 0`.
*   De donde se obtiene: `xk+1 = xk - r(xk) / T(xk)`.
    *   `r(xk) = C - F(xk)` (residuo en la iteración k).
    *   `T(xk) = f'(xk)` (tangente en la iteración k).
*   **Inicialización**: Una aproximación de la raíz.
*   **Recurrencia**: `xk+1 = xk - r(xk) / T(xk)`.
*   **Control de Detención**: Igual que en el método de Bisección.
*   **Actualización de Variables**: Retener la última aproximación.

### 4.6 Método de Punto Fijo

*   Dado `y = F(x)` y buscando `xr` tal que `F(xr) = C`. Se puede reescribir `C - F(x) = 0`.
*   Multiplicando por un número no nulo y sumando `x` en ambos miembros, se llega a `x = g(x)`, donde `g(x) = x + α(C - F(x))`.
*   La igualdad `x = g(x)` se interpreta como la intersección de `y = x` (bisectriz del primer cuadrante) con `y = g(x)`. El punto solución es el **Punto Fijo** de la curva `g(x)`.
*   **Inicialización**: Una aproximación de la raíz.
*   **Recurrencia**: `xk+1 = g(xk)`.
*   **Control de Detención**: Igual que en el método de Bisección. Alternativamente, se controla `|xk+1 - g(xk+1)| < ε`.
*   **Relación con Newton Raphson**: El método de Newton Raphson puede interpretarse como un método de Punto Fijo donde el coeficiente `α` es variable en cada iteración.

### 4.7 Condición de Convergencia del Método de Punto Fijo

*   Sea `xs` el punto fijo de `g(x)`, es decir, `xs = g(xs)`.
*   Restando `xs = g(xs)` de `xk+1 = g(xk)`, y aplicando el Teorema del Valor Medio, se obtiene `xk+1 - xs = g'(ξ) * (xk - xs)`.
*   Esto significa que el error de la iteración `k+1` (`Ek+1`) es igual a `g'(ξ)` veces el error de la iteración `k` (`Ek`).
*   Para que el proceso iterativo **converja**, el error de una iteración debe ser menor que el error de la anterior.
*   La condición de convergencia es: **`|g'(x)| < 1`**.

