# EDA — TDAH en Niños

Análisis exploratorio, modelamiento predictivo e informe técnico sobre una muestra clínica de niños de 6 a 12 años evaluados para TDAH.

## Datos

| | |
|---|---|
| **Fuente original** | `data/raw/datos_tdah.csv` |
| **Datos procesados** | `data/processed/processed_data.csv` |
| **Registros** | 875 |
| **Variables** | 18 (14 predictores + 1 objetivo + 3 índices excluidos por leakage) |
| **Variable objetivo** | `etiqueta` — 13 categorías diagnósticas |

**Grupos de variables:**

| Grupo | Variables |
|---|---|
| Demográficas | `edad`, `sexo`, `escolaridad`, `lateralidad` |
| Antecedentes clínicos | `antecedentes_familiares`, `antecedentes_obstetricos`, `retrasos_desarrollo` |
| Índices TDAH *(excluidos por leakage)* | `indice_tdah`, `indice_inatencion`, `indice_impuls_hiperac` |
| Cognitivo | `cit` (Coeficiente Intelectual Total) |
| Conductuales — BASC-3 (T-scores) | `agresividad_basc3`, `hiperactividad_basc3`, `problemas_conducta_basc3`, `problemas_atencion_basc3`, `atipicidad_basc3` |
| Función ejecutiva | `fluidez_fonologica` |

## Notebooks

Los notebooks siguen el flujo analítico del proyecto, de la limpieza de datos hasta el informe técnico.

| # | Notebook | Contenido |
|---|---|---|
| 1 | `preprocessing.ipynb` | Limpieza, codificación, control de consistencia y exportación de datos procesados |
| 2 | `eda_univariate.ipynb` | Distribución individual de cada variable: normalidad, outliers, asimetría (rúbrica: 94/100) |
| 3 | `eda_bivariate.ipynb` | Relaciones variable–`etiqueta`: Kruskal-Wallis, Dunn, Chi², perfiles z-score (rúbrica: 95/100) |
| 4 | `model_4clases.ipynb` | Clasificación en 4 tipos diagnósticos principales usando perfil BASC-3 |
| 5 | `model_13clases.ipynb` | Clasificación de las 13 categorías diagnósticas (RF, XGBoost, Regresión Logística) |
| 6 | `error_analysis.ipynb` | Análisis de errores: tipos, confianza del modelo y pares de confusión más frecuentes |
| 7 | `comorbidity_importance.ipynb` | Importancia de variables por comorbilidad (TND, TEAZ, TEA) mediante clasificadores binarios |
| 8 | `ablation_study.ipynb` | Estudio de ablación: impacto en rendimiento al retirar bloques de variables |
| 9 | `informe_tecnico_13clases.ipynb` | Notebook integrador: reproduce todos los resultados del informe técnico en un solo flujo |
| 10 | `figuras_parametrizables.ipynb` | Código parametrizable para regenerar las figuras 5, 6 y 9 del informe |

La calidad de los notebooks EDA se evalúa con `notebooks/rubrica_calidad_eda.md`.

## Informe técnico

El informe técnico completo se encuentra en `EDA-TDAH/`. Documenta el proceso analítico de principio a fin: preprocesamiento, EDA bivariado, comparación de modelos, importancia de variables, análisis de errores, estudio de ablación, conclusiones y limitaciones.

**Resultados principales:**

| Modelo | CV F1-macro | DE | Test F1-macro | Test Accuracy |
|---|:---:|:---:|:---:|:---:|
| Regresión logística | 0.841 | 0.024 | 0.851 | 0.874 |
| **Random Forest** | **0.953** | **0.018** | **0.942** | **0.954** |
| XGBoost | 0.934 | 0.022 | 0.941 | 0.949 |

El bloque BASC-3 concentra la mayor parte del poder discriminante: retirarlo reduce el F1-macro de 0.942 a 0.268. Los errores se concentran en la frontera entre subtipos con perfiles sintomáticos cercanos.

## Notas metodológicas

- Ninguna variable continua sigue distribución normal (Shapiro-Wilk / KS). Todos los tests bivariados son no paramétricos.
- Umbral diagnóstico para índices TDAH: **≥ 0.5** (equivale a 6/9 síntomas DSM-5).
- T-scores BASC-3: **T ≥ 60** = At-Risk · **T ≥ 70** = Clínicamente significativo (media = 50, SD = 10).
- Los índices `indice_tdah`, `indice_inatencion` e `indice_impuls_hiperac` se excluyeron del modelamiento por leakage (F1 individual > 0.70).
- El análisis bivariado agrupa las 13 etiquetas en 4 tipos principales para visualizaciones.
- Todos los resultados corresponden a validación interna; no deben interpretarse como evidencia de generalización externa.

## Estructura del proyecto

```
TDAH-data/
├── data/
│   ├── raw/                          # Datos originales (xlsx, csv, equivalencias)
│   └── processed/
│       └── processed_data.csv        # Dataset limpio listo para análisis
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── eda_univariate.ipynb
│   ├── eda_bivariate.ipynb
│   ├── model_4clases.ipynb
│   ├── model_13clases.ipynb
│   ├── error_analysis.ipynb
│   ├── comorbidity_importance.ipynb
│   ├── ablation_study.ipynb
│   ├── informe_tecnico_13clases.ipynb
│   ├── figuras_parametrizables.ipynb
│   └── rubrica_calidad_eda.md
├── EDA-TDAH/
│   └── Informe_TDAH-9.docx           # Informe técnico final
├── .gitignore
├── LICENCE
└── Readme.md
```
