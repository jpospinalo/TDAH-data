# EDA — TDAH en Niños

Análisis exploratorio de datos de una muestra clínica de niños de 6 a 12 años evaluados para TDAH.

## Datos

| | |
|---|---|
| **Fuente original** | `data/raw/datos_tdah.csv` |
| **Datos procesados** | `data/processed/processed_data.csv` |
| **Registros** | 875 |
| **Variables** | 18 |
| **Variable objetivo** | `etiqueta` — 13 categorías diagnósticas |

**Variables disponibles:**

- *Demográficas:* `edad`, `sexo`, `escolaridad`, `lateralidad`
- *Antecedentes clínicos:* `antecedentes_familiares`, `antecedentes_obstetricos`, `retrasos_desarrollo`
- *Índices TDAH (0–1):* `indice_tdah`, `indice_inatencion`, `indice_impuls_hiperac`
- *Cognitivo:* `cit` (Coeficiente Intelectual Total)
- *Conductuales — BASC-3 (T-scores):* `agresividad_basc3`, `hiperactividad_basc3`, `problemas_conducta_basc3`, `problemas_atencion_basc3`, `atipicidad_basc3`
- *Función ejecutiva:* `fluidez_fonologica`

## Notebooks

| Notebook | Contenido | Puntaje rúbrica |
|---|---|:---:|
| `preprocessing.ipynb` | Limpieza, codificación y exportación de datos procesados | — |
| `eda_univariate.ipynb` | Distribución individual de cada variable — normalidad, outliers, asimetría | 94/100 |
| `eda_bivariate.ipynb` | Relaciones variable–`etiqueta` — Kruskal-Wallis, Dunn, Chi², perfiles z-score | 95/100 |

La calidad de los notebooks se evalúa con `rubrica_calidad_eda.md` (estructura, visualización, interpretación, rigor estadístico, consistencia).

## Notas metodológicas

- Ninguna variable continua sigue distribución normal (Shapiro-Wilk / KS). Todos los tests bivariados son no paramétricos.
- Umbral diagnóstico para índices TDAH: **≥ 0.5** (equivale a 6/9 síntomas DSM-5).
- T-scores BASC-3: **T ≥ 60** = At-Risk · **T ≥ 70** = Clínicamente significativo (media poblacional = 50, SD = 10).
- El análisis bivariado agrupa las 13 etiquetas en 4 tipos principales para visualizaciones (desarrollo típico, inatento, hiperactivo/impulsivo, combinado).

## Estructura del proyecto

```
TDAH-data/
├── data/
│   ├── raw/                  # Datos originales
│   └── processed/            # Datos limpios listos para análisis
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── eda_univariate.ipynb
│   ├── eda_bivariate.ipynb
│   └── rubrica_calidad_eda.md
└── Readme.md
```
