# Rúbrica de Calidad — Notebooks de EDA
## Proyecto TDAH · Evaluación de estructura, visualización e interpretación

---

## Propósito

Este instrumento evalúa la calidad de los notebooks de análisis exploratorio de datos (EDA) del proyecto.
Se aplica a cualquier notebook del proyecto para garantizar que todos tengan el mismo nivel de claridad,
rigor y consistencia visual, independientemente de su contenido.

**Escala de puntuación por criterio:**

| Puntuación | Nivel | Descripción |
|:---:|---|---|
| **4** | Excelente | Cumple el criterio completamente, sin correcciones necesarias |
| **3** | Satisfactorio | Cumple en su mayoría; hay gaps menores que no afectan la comprensión |
| **2** | Necesita mejora | Cumple parcialmente; gaps importantes que dificultan la lectura |
| **1** | Insuficiente | No cumple o cumple de forma mínima |

**Total máximo: 100 puntos.** Umbral de calidad aceptable: ≥ 80 puntos.

---

## Dimensión 1 — Estructura y navegación · (máx. 20 puntos)

*Evalúa si el notebook puede seguirse de forma lógica y ordenada sin necesidad de ejecutar celdas.*

| # | Criterio | 1 | 2 | 3 | 4 | Notas |
|---|---|:---:|:---:|:---:|:---:|---|
| 1.1 | **Celda de título:** incluye nombre del notebook, dataset, n de registros y objetivo del análisis | | | | | |
| 1.2 | **Tabla de contenidos:** lista los bloques temáticos con numeración en la primera celda | | | | | |
| 1.3 | **Encabezado de bloque:** cada sección principal comienza con una celda markdown que describe qué se analizará y por qué | | | | | |
| 1.4 | **Separadores visuales (`---`):** presentes entre todos los bloques principales | | | | | |
| 1.5 | **Celda de clasificación de variables:** al inicio del notebook se listan y agrupan todas las variables por tipo | | | | | |

**Subtotal D1: ___ / 20**

---

## Dimensión 2 — Calidad visual de las gráficas · (máx. 24 puntos)

*Evalúa si las gráficas son claras, completas y estéticamente consistentes.*

| # | Criterio | 1 | 2 | 3 | 4 | Notas |
|---|---|:---:|:---:|:---:|:---:|---|
| 2.1 | **Título descriptivo:** toda gráfica tiene `suptitle` o `set_title` que identifica qué muestra | | | | | |
| 2.2 | **Etiquetas de ejes:** todos los ejes tienen label con la variable y unidades donde aplica | | | | | |
| 2.3 | **Leyenda completa:** las gráficas con múltiples series tienen leyenda con labels significativos | | | | | |
| 2.4 | **Líneas de referencia etiquetadas:** toda `axhline`/`axvline` de umbral tiene `label=` y aparece en la leyenda | | | | | |
| 2.5 | **Tamaño y resolución:** `figsize` y `dpi` apropiados para el número de subplots; texto legible sin zoom | | | | | |
| 2.6 | **Consistencia de paleta:** mismo conjunto de colores base (`C_BLUE`, `C_ORG`, `PAL4`, etc.) en todo el notebook | | | | | |

**Subtotal D2: ___ / 24**

---

## Dimensión 3 — Interpretación · (máx. 32 puntos)

*La dimensión más importante. Evalúa si el notebook puede leerse como un documento analítico, no solo como código.*

| # | Criterio | 1 | 2 | 3 | 4 | Notas |
|---|---|:---:|:---:|:---:|:---:|---|
| 3.1 | **Cobertura:** toda celda con gráfica tiene una celda markdown de interpretación inmediatamente después | | | | | |
| 3.2 | **Identificación:** las interpretaciones están marcadas con `📋 **Interpretación**` para localizarlas de un vistazo | | | | | |
| 3.3 | **Umbrales explicados:** todo umbral o línea de referencia es explicado con su significado clínico/estadístico antes o durante su primer uso en el notebook | | | | | |
| 3.4 | **Profundidad:** la interpretación va más allá de describir la gráfica — explica qué significa el resultado, qué se esperaba y qué implicaciones tiene | | | | | |
| 3.5 | **Concisión:** las interpretaciones no son verbose; cada párrafo agrega información nueva; no hay repeticiones entre la descripción del bloque y la interpretación de la gráfica | | | | | |
| 3.6 | **Contexto clínico:** donde es relevante, la interpretación conecta el hallazgo estadístico con el significado clínico o práctico del resultado | | | | | |
| 3.7 | **Guía de lectura:** las gráficas más complejas (heatmaps, violin plots, radar) incluyen una explicación de cómo leerlas antes de la interpretación del resultado | | | | | |
| 3.8 | **Conclusión de bloque:** cada bloque temático cierra con una frase o párrafo que resume el hallazgo principal de ese bloque | | | | | |

**Subtotal D3: ___ / 32**

---

## Dimensión 4 — Rigor estadístico comunicado · (máx. 12 puntos)

*Evalúa si los tests y métricas están correctamente aplicados y comunicados.*

| # | Criterio | 1 | 2 | 3 | 4 | Notas |
|---|---|:---:|:---:|:---:|:---:|---|
| 4.1 | **Tests apropiados:** los tests usados son adecuados al tipo de variable y distribución (p.ej. no paramétricos cuando corresponde) | | | | | |
| 4.2 | **Resultados en lenguaje natural:** los estadísticos (H, p, χ²) son traducidos a conclusiones en texto, no solo reportados en tablas | | | | | |
| 4.3 | **Limitaciones señaladas:** se mencionan limitaciones relevantes (tamaño de celda, p-valores sin corrección, outliers, etc.) donde corresponde | | | | | |

**Subtotal D4: ___ / 12**

---

## Dimensión 5 — Consistencia entre notebooks · (máx. 12 puntos)

*Evalúa si los notebooks del proyecto son estilísticamente coherentes entre sí.*

| # | Criterio | 1 | 2 | 3 | 4 | Notas |
|---|---|:---:|:---:|:---:|:---:|---|
| 5.1 | **Estilo visual idéntico:** mismos valores de `dpi`, `facecolor`, `font_scale`, `sns.set_theme` y colores base en todos los notebooks | | | | | |
| 5.2 | **Formato de interpretación idéntico:** mismo marcador (`📋`), mismo encabezado en negrita, misma convención para umbrales y referencias | | | | | |
| 5.3 | **Profundidad equivalente:** el nivel de detalle por bloque es comparable — ningún notebook tiene bloques notablemente más superficiales que otro del mismo tipo | | | | | |

**Subtotal D5: ___ / 12**

---

## Resumen de puntuación

| Dimensión | Máximo | Obtenido | % |
|---|:---:|:---:|:---:|
| D1 · Estructura y navegación | 20 | | |
| D2 · Calidad visual | 24 | | |
| D3 · Interpretación | 32 | | |
| D4 · Rigor estadístico comunicado | 12 | | |
| D5 · Consistencia entre notebooks | 12 | | |
| **Total** | **100** | | |

**Nivel:**
- 90–100 → Publicable sin cambios
- 80–89 → Listo para revisión, mejoras menores
- 65–79 → Requiere trabajo en dimensiones específicas
- < 65 → Revisión sustancial necesaria

---

## Evaluación — Estado actual de los notebooks

### eda_univariate.ipynb

> **Versión revisada — Mayo 2026.** El notebook fue regenerado completamente aplicando el plan de acción de la evaluación anterior (71/100 → 94/100).

| # | Criterio | Puntaje | Observación |
|---|---|:---:|---|
| 1.1 | Celda de título | 4 | Completa: dataset, n, objetivo y guía de lectura del notebook |
| 1.2 | Tabla de contenidos | 4 | 8 bloques numerados con descripción |
| 1.3 | Encabezado de bloque | 4 | Todos los bloques tienen encabezado con contexto clínico/estadístico |
| 1.4 | Separadores `---` | 4 | Presentes en todos los bloques |
| 1.5 | Clasificación de variables | 3 | Definida en celda de código (`vars_cat`, `vars_indices`, `vars_basc3`, etc.); no hay tabla markdown separada |
| **D1** | | **19/20** | |
| 2.1 | Título en cada gráfica | 4 | Todas las gráficas tienen `suptitle` o `set_title` |
| 2.2 | Etiquetas de ejes | 4 | Presentes con unidades en todos los ejes |
| 2.3 | Leyenda con labels | 3 | Presente en la mayoría; algunas gráficas de una sola serie no requieren leyenda |
| 2.4 | Líneas de referencia etiquetadas | 4 | 30 ocurrencias de `label=` — todas las `axhline`/`axvline` etiquetadas |
| 2.5 | Tamaño y resolución | 4 | `figsize` apropiado por tipo de gráfica, `dpi=130` global |
| 2.6 | Consistencia de paleta | 4 | `C_BLUE`, `C_ORG` definidos globalmente y usados consistentemente |
| **D2** | | **23/24** | |
| 3.1 | Cobertura (toda gráfica con interpretación) | 3 | 13 celdas `📋` para 14 gráficas; una gráfica de estadísticos tabular comparte interpretación |
| 3.2 | Marcador `📋` | 4 | Presente y consistente en todas las interpretaciones |
| 3.3 | Umbrales explicados | 4 | T=60 (At-Risk), T=70 (Clínico), 0.5 (6/9 síntomas DSM-5), rangos CIT — todos explicados en contexto |
| 3.4 | Profundidad de interpretación | 4 | Cada interpretación explica qué significa, qué se esperaba y la implicación para el bivariado |
| 3.5 | Concisión | 4 | Las celdas son focalizadas; no hay repetición entre encabezado e interpretación |
| 3.6 | Contexto clínico | 4 | DSM-5, BASC-3, etiología multifactorial — presente en todas las interpretaciones relevantes |
| 3.7 | Guía de lectura para gráficas complejas | 4 | "Cómo leer" incluido para histograma+KDE, Q-Q plot, boxplot/violín, tabla de normalidad |
| 3.8 | Conclusión de bloque | 2 | Las interpretaciones cierran con frases de síntesis, pero no hay una celda de conclusión de bloque separada y explícita en todos los bloques |
| **D3** | | **29/32** | |
| 4.1 | Tests apropiados | 4 | Shapiro-Wilk y KS — correctos para normalidad en muestra clínica |
| 4.2 | Resultados en lenguaje natural | 4 | Tabla de normalidad traducida a conclusiones en las interpretaciones de cada bloque |
| 4.3 | Limitaciones señaladas | 3 | Bloque 8 menciona las principales; podría ser más explícito en bloques intermedios |
| **D4** | | **11/12** | |
| 5.1 | Estilo visual idéntico al bivariado | 4 | Mismos `rcParams`, `dpi`, `facecolor`, `font_scale`, `sns.set_theme` |
| 5.2 | Formato de interpretación idéntico | 4 | `📋 **Interpretación**` en negrita, mismo marcador y estructura que el bivariado |
| 5.3 | Profundidad equivalente | 4 | Nivel de detalle por bloque comparable al bivariado |
| **D5** | | **12/12** | |
| | **TOTAL** | **94/100** | ✅ Publicable sin cambios |

---

### eda_bivariate.ipynb

| # | Criterio | Puntaje | Observación |
|---|---|:---:|---|
| 1.1 | Celda de título | 4 | Completa con tabla y guía de lectura del notebook |
| 1.2 | Tabla de contenidos | 4 | 6 bloques numerados con descripción |
| 1.3 | Encabezado de bloque | 4 | Cada bloque tiene contexto clínico antes de las gráficas |
| 1.4 | Separadores `---` | 4 | Presentes en todos los bloques |
| 1.5 | Clasificación de variables | 4 | Función helper + clasificación de grupos al inicio |
| **D1** | | **20/20** | |
| 2.1 | Título en cada gráfica | 4 | Todas tienen `suptitle` descriptivo |
| 2.2 | Etiquetas de ejes | 4 | Presentes y con unidades en todas |
| 2.3 | Leyenda con labels | 4 | Leyendas completas con labels clínicos |
| 2.4 | Líneas de referencia etiquetadas | 2 | 3 de 6 líneas tienen `label=`; las del loop del Bloque 5 no |
| 2.5 | Tamaño y resolución | 4 | `figsize` apropiado por tipo de gráfica |
| 2.6 | Consistencia de paleta | 4 | `PAL4`, `C_BLUE`, etc. usados globalmente |
| **D2** | | **22/24** | Gap puntual: líneas de referencia en loops |
| 3.1 | Cobertura (toda gráfica con interpretación) | 4 | Todas las gráficas tienen celda `📋` posterior |
| 3.2 | Marcador `📋` | 4 | Presente y consistente en todas las interpretaciones |
| 3.3 | Umbrales explicados | 4 | Cada umbral está explicado con su significado clínico |
| 3.4 | Profundidad de interpretación | 4 | Las interpretaciones explican el porqué, no solo el qué |
| 3.5 | Concisión | 3 | Algunos bloques (especialmente el Bloque 6) son extensos; podrían reducirse sin perder contenido |
| 3.6 | Contexto clínico | 4 | Presente en todas las interpretaciones relevantes |
| 3.7 | Guía de lectura para gráficas complejas | 4 | Violinplots, heatmaps, radar y coordenadas paralelas tienen guía |
| 3.8 | Conclusión de bloque | 3 | La mayoría de bloques cierran; el Bloque 5 no tiene cierre explícito |
| **D3** | | **30/32** | |
| 4.1 | Tests apropiados | 4 | KW + Dunn y Chi² correctos para datos no normales y categóricos |
| 4.2 | Resultados en lenguaje natural | 4 | Cada test tiene su traducción en texto |
| 4.3 | Limitaciones señaladas | 4 | Dunn sin corrección, Chi² con tablas grandes, etc. |
| **D4** | | **12/12** | |
| 5.1 | Estilo visual idéntico al univariado | 4 | Mismos parámetros de configuración |
| 5.2 | Formato de interpretación idéntico | 4 | `📋` y estructura consistente |
| 5.3 | Profundidad equivalente | 4 | Ambos notebooks ahora al mismo nivel de detalle |
| **D5** | | **12/12** | |
| | **TOTAL** | **95/100** | ✅ Listo para revisión; solo mejoras menores |

---

## Resumen comparativo final

| Notebook | Evaluación inicial | Evaluación final | Variación |
|---|:---:|:---:|:---:|
| `eda_univariate.ipynb` | 71/100 | **94/100** | +23 pts ✅ |
| `eda_bivariate.ipynb` | 95/100 | **95/100** | — |

Ambos notebooks superan el umbral de **90/100** (publicable sin cambios). La brecha D5 (consistencia entre notebooks) ha sido cerrada.

---

*Rúbrica creada: Mayo 2026 · Evaluación final: Mayo 2026 · Proyecto EDA-TDAH*
