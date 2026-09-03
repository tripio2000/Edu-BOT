# Solución Numérica de Ecuaciones Diferenciales Ordinarias con Valores Iniciales

## 1. Introducción

Las ecuaciones diferenciales son expresiones matemáticas que involucran funciones, sus derivadas, y una o más variables independientes y dependientes. Se clasifican en dos grandes grupos:
*   **Ecuaciones Diferenciales Ordinarias (EDO)**: Aquellas que contienen **solo una variable independiente**. Por ejemplo, `y´´(x)=f(x)` o `y´(x)=-K y(x)`.
*   **Ecuaciones Diferenciales Parciales (EDP)**: Aquellas con **más de una variable independiente**.
En este curso, nos centramos en las EDO de **primer orden** con una condición inicial, de la forma: `y´=f(x,y)` y `y(x0)=y0`.

**¿Por qué surgen los métodos numéricos para resolver EDO?**
Aunque existen soluciones analíticas para casos específicos de EDO (variables separables, exactas, etc.), **muchos problemas prácticos no tienen solución analítica o es demasiado compleja de obtener/evaluar**. Frecuentemente, los coeficientes o funciones en una EDO son fuertemente no lineales, o están definidos por **datos experimentales tabulados**, haciendo inviables los métodos clásicos.

La **solución numérica** de una EDO implica discretizar la variable `x` en una sucesión de puntos `xm = x0 + m·h` (con `m = 0, 1, ..., n`) y aproximar la función `Y(x)` en estos puntos discretos. La idea es avanzar paso a paso, usando la pendiente conocida `f(x,y)` para estimar el siguiente punto.

## 2. Clasificación de los Métodos
Los métodos numéricos para EDO de primer orden se dividen en dos categorías principales:
### I. Métodos de un Paso
*   Para aproximar la solución en `xm`, **utilizan datos solo del punto anterior** (`xm-1, Ym-1`).
*   Son **métodos directos**, es decir, la solución en un punto no se itera.
*   Su principal desventaja es que **es difícil estimar el error**.
*   Ejemplos incluyen el **Desarrollo en Serie de Taylor** y los **Métodos de Runge-Kutta**.
*   Su forma general es: `Ym+1 = Ym + h Φ(xm ,Ym, h, f)`. La función `Φ` es crucial para la convergencia y estabilidad.

### II. Métodos Multipaso
*   Para aproximar `Ym+1`, **utilizan información de varios puntos anteriores**.
*   **Requieren iteración** de la solución para alcanzar la precisión deseada.
*   Permiten una **estimación del error**.
*   Generalmente requieren **menos evaluaciones de la función `f`** por paso que los métodos de un paso para un mismo orden.
*   La mayoría se conocen como **Predictor-Corrector**.
*   Se clasifican en:
    *   **Explícitos**: Si `b_p+1 = 0` (la incógnita `Ym+1` solo aparece en el primer miembro).
    *   **Implícitos**: Si `b_p+1 ≠ 0` (la incógnita `Ym+1` también aparece en el segundo miembro, requiriendo un proceso iterativo para su cálculo).

## 3. Tipos de Errores en los Métodos Numéricos para la Solución de EDO
Comprender los errores es vital para garantizar la **fiabilidad y la robustez** de nuestros modelos numéricos. Un DevOps o AI Engineer debe ser consciente de cómo estos errores pueden afectar el rendimiento y la precisión de un sistema en producción:

1.  **Error de Redondeo Local**: Causado por la **precisión finita de los números** en la computadora. Es independiente del tamaño de paso `h`.
2.  **Error por Truncado Local**: Inherente al método numérico y **depende directamente del tamaño de paso `h`**. Generalmente es mayor que el error de redondeo local.
3.  **Error por Propagación**: El **error de un paso se transmite y puede amplificarse en los pasos siguientes**. Si el método es inestable, este error puede crecer de forma descontrolada, llevando a soluciones sin sentido.

## 4. Solución en Serie de Taylor

Aunque tiene **escaso valor computacional práctico**, este método es una **base teórica fundamental** para evaluar y comparar otros métodos.

La idea es desarrollar `y(x)` en una Serie de Taylor alrededor de `x0` y luego evaluar la serie en `x1` para obtener `y(x1) = y1`, repitiendo el proceso.

La expansión de `Y(x)` con centro en `xm` para el siguiente punto `Ym+1 = Y(xm + h)` es:
`Ym+1 = Ym + h Ym´ + (h²/2) Ym´´ + (h³/6) Ym´´´ + ...`.

Las derivadas `Ym´, Ym´´, Ym´´´`, etc., se obtienen derivando sucesivamente la EDO original `y´=f(x,y)`. Por ejemplo:
*   `Ym´ = f (xm , Ym)`.
*   `Ym´´ = ∂f/∂x + (∂f/∂y)·Ym´ = f_x + f_y · f`.
*   Las derivadas de orden superior se complican rápidamente.

El **error de truncamiento local** (de un paso) se obtiene al evaluar el primer término omitido en la Serie de Taylor, siendo proporcional a `h^(n+1)` para un método de orden `n`.

La **dificultad práctica** radica en la **evaluación compleja y laboriosa de las derivadas de `f(x,y)`** de orden superior, lo que lo hace impráctico para la implementación computacional directa en la mayoría de los casos.

## 5. Métodos de Runge-Kutta

Los métodos de Runge-Kutta (RK) son la **piedra angular** en la resolución numérica de EDO en la práctica de la ingeniería y el desarrollo de software.

Sus **características generales** son:
*   Son **métodos de un paso**.
*   **Coinciden con la Serie de Taylor hasta un cierto orden `p`**, que define el orden del método.
*   **No requieren la evaluación explícita de las derivadas de `f`**, sino únicamente evaluaciones de la función `f` misma en diferentes puntos. Esta última es su mayor ventaja práctica.

### 5.1. Método de Euler

Es el **más antiguo y simple**. Es fácil de entender, pero **no es muy preciso y a menudo es inestable**, amplificando errores pequeños conforme `x` aumenta.

La fórmula del Método de Euler es una simple extrapolación lineal usando la pendiente inicial:
`Ym+1 = Ym + h * f(xm, Ym)`.

*   Su **error de truncamiento local es de orden O(h²)**.
*   Es un **método de Runge-Kutta de primer orden**.

Gráficamente, la derivada es la pendiente de la secante que pasa por `(xs, fs)` y `(xs+1, fs+1)`. Es una aproximación hacia adelante.

### 5.2. Método de Euler Mejorado

Este método **mejora la precisión promediando pendientes**.
1.  Se estima un punto `E` (predicción) usando Euler simple: `Y_E = Ym + h * f(xm, Ym)`.
2.  Se calcula la pendiente en `E`: `f(xm+h, Y_E)`.
3.  Se promedian la pendiente inicial `f(xm, Ym)` y la pendiente en `E`:
    `Pendiente_promedio = (f(xm, Ym) + f(xm+h, Ym + h*f(xm,Ym))) / 2`.
4.  La nueva aproximación `Ym+1` se calcula usando esta pendiente promedio:
    `Ym+1 = Ym + h * Pendiente_promedio`.

*   Este método es un **Método de Runge-Kutta de segundo orden**, ya que su expresión coincide con la Serie de Taylor hasta los términos de `O(h²)`.
*   Requiere **dos evaluaciones de la función `f`** por paso.

### 5.3. Método de Euler Modificado

En lugar de promediar pendientes, este método **"promedia puntos"**.
1.  Se calcula la pendiente inicial `f(xm, Ym)`.
2.  Se determina el **punto medio** del intervalo `[xm, xm+h]` usando esta pendiente:
    `Y_C = Ym + (h/2) * f(xm, Ym)`.
    `X_C = xm + h/2`.
3.  Se calcula la pendiente de la recta tangente a la curva en este punto medio `C`:
    `Pendiente_C = f(xm + h/2, Ym + (h/2)*f(xm, Ym))`.
4.  La aproximación `Ym+1` se obtiene usando esta pendiente en el intervalo completo:
    `Ym+1 = Ym + h * Pendiente_C`.

*   También es un **Método de Runge-Kutta de segundo orden**.

### 5.4. Generalización de los Métodos de Runge-Kutta de Segundo Orden

Los métodos de RK de segundo orden se pueden expresar de forma general como:
`Ym+1 = Ym + h * (a1*k1 + a2*k2)`
donde:
*   `k1 = f(xm, Ym)`.
*   `k2 = f(xm + b1*h, Ym + b2*h*k1)`.

Las condiciones para que este método sea de segundo orden (es decir, que su expansión en serie de Taylor coincida con la de la solución exacta hasta `O(h²)` son:
1.  `a1 + a2 = 1`
2.  `a2 * b1 = 1/2`
3.  `a2 * b2 = 1/2`

Como hay **tres ecuaciones y cuatro parámetros** (`a1, a2, b1, b2`), existe **un grado de libertad**, lo que permite derivar muchas fórmulas diferentes de segundo orden. Por ejemplo:
*   **Método de Euler Mejorado**: `a1=1/2, a2=1/2, b1=1, b2=1`.
*   **Método de Euler Modificado**: `a1=0, a2=1, b1=1/2, b2=1/2`.
*   **Método de Heun (sin corrección)**: `a1=1/2, a2=1/2, b1=1, b2=1` (es el mismo que el mejorado, pero Heun es más conocido como predictor-corrector).

### 5.5. Método de Runge-Kutta de Cuarto Orden (RK4 Clásico)

El **RK4 clásico es el método de Runge-Kutta más popular y utilizado** debido a su excelente equilibrio entre precisión y costo computacional.
Requiere **cuatro evaluaciones de la función `f`** por paso:
`Ym+1 = Ym + (h/6) * (k1 + 2*k2 + 2*k3 + k4)`
donde:
*   `k1 = f(xm, Ym)`.
*   `k2 = f(xm + h/2, Ym + (h/2)*k1)`.
*   `k3 = f(xm + h/2, Ym + (h/2)*k2)`.
*   `k4 = f(xm + h, Ym + h*k3)`.

*   Su **error de truncamiento local es de orden O(h⁵)**.
*   El **error global del método es de orden O(h⁴)**.
*   Se puede demostrar que es una **generalización del método de Simpson** para integrar funciones que dependen de `x` e `y`.

## 6. Métodos Predictor-Corrector

Estos métodos son una alternativa a los Runge-Kutta, especialmente útiles cuando se requiere **alta precisión y control del error**.

### 6.1. Métodos Multipaso

Para evaluar `Ym+1`, utilizan información de **varios puntos anteriores**. Esto significa que, a diferencia de los métodos de un paso, **requieren un "Método Inicializador"** (como un RK de alto orden) para calcular los primeros `p` puntos antes de que el método multipaso pueda comenzar.

La forma general de estos métodos es:
`Σ(aj * Y(m+j)) = h * Σ(bj * f(X(m+j), Y(m+j)))`

*   **Métodos Explícitos**: `b_final = 0`. `Ym+1` se calcula directamente.
    *   **Método del Punto Medio**: `Ym+1 = Ym-1 + 2h * f(xm, Ym)`.
        *   Es un **método de dos pasos** (necesita `Ym` y `Ym-1`).
        *   Es de **segundo orden** con error `O(h³)`.
        *   Es **explícito**.

*   **Métodos Implícitos**: `b_final ≠ 0`. `Ym+1` aparece en ambos lados de la ecuación, requiriendo un proceso iterativo (ej. punto fijo) para su solución.
    *   **Método del Trapecio**: `Ym+1 = Ym + (h/2) * (f(xm, Ym) + f(xm+1, Ym+1))`.
        *   Es un **método de un paso** (solo necesita `Ym` y `Ym+1` que se itera).
        *   Es de **segundo orden** con error `O(h³)`.
        *   Es **implícito**.

### 6.2. Métodos Predictor-Corrector (P-C)

Combinan un método **predictor** (generalmente explícito y de menor complejidad) para obtener una primera estimación de `Ym+1`, y luego un método **corrector** (generalmente implícito y de mayor precisión) que refina esa estimación mediante iteración. El ciclo predictor-corrector se repite hasta alcanzar una tolerancia deseada.

#### 6.2.1. Método Predictor-Corrector de Segundo Orden

*   **Predictor (Método del Punto Medio)**: `Ym+1^(0) = Ym-1 + 2h * f(xm, Ym)`.
    *   Explícito, 2 pasos, 2º orden. Necesita un método inicializador (ej. RK4) para `Y1`.
*   **Corrector (Método del Trapecio)**: `Ym+1^(i) = Ym + (h/2) * (f(xm, Ym) + f(xm+1, Ym+1^(i-1)))`.
    *   Implícito, 1 paso, 2º orden. Se itera hasta convergencia.

#### 6.2.2. Método de Heun

*   **Predictor (Método de Euler)**: `Ym+1^(0) = Ym + h * f(xm, Ym)`.
    *   Explícito, 1º orden, 1 paso. No requiere inicializador.
*   **Corrector (Método del Trapecio)**: `Ym+1^(i) = Ym + (h/2) * (f(xm, Ym) + f(xm+1, Ym+1^(i-1)))`.
    *   Implícito, 2º orden.

*   El error de truncamiento de este método es `O(h³)`.

#### 6.2.3. Método de Milne

Un ejemplo de un método predictor-corrector de **mayor orden**:
*   **Predictor**: `Ym+1^(0) = Ym-3 + (4h/3) * (2*fm-2 - fm-1 + 2*fm)`.
    *   Explícito, **4 pasos**, 4º orden. Requiere un inicializador para los primeros 3 pasos.
*   **Corrector**: `Ym+1^(i) = Ym-1 + (h/3) * (fm-1 + 4*fm + f(m+1)`).
    *   Implícito, **2 pasos**, 4º orden.

A pesar de su alto orden, el método de Milne puede presentar **problemas de estabilidad** para ciertos valores de `h`.
