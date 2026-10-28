# TDAH en niñas y niños · análisis, modelos e interfaz

Análisis exploratorio, modelamiento predictivo, informe técnico e interfaz de apoyo a la decisión clínica sobre una muestra clínica de niñas y niños de 6 a 12 años evaluados por TDAH.

**Interfaz (prototipo):** <https://jpospinalo.github.io/TDAH-data/> · apoyo a la decisión clínica construido sobre el modelo Random Forest. Ver [Interfaz](#interfaz).

## Datos

| | |
|---|---|
| **Fuente original** | `data/raw/datos_tdah.csv` |
| **Datos procesados** | `data/processed/processed_data.csv` |
| **Registros** | 875 |
| **Variables** | 18 (14 predictores + 1 objetivo + 3 índices excluidos por circularidad) |
| **Variable objetivo** | `etiqueta` — 13 categorías diagnósticas |

**Grupos de variables:**

| Grupo | Variables |
|---|---|
| Demográficas | `edad`, `sexo`, `escolaridad`, `lateralidad` |
| Antecedentes clínicos | `antecedentes_familiares`, `antecedentes_obstetricos`, `retrasos_desarrollo` |
| Índices TDAH *(excluidos del modelamiento)* | `indice_tdah`, `indice_inatencion`, `indice_impuls_hiperac` |
| Cognitivo | `cit` (cociente intelectual total) |
| Conductuales — BASC-3 (puntuaciones T) | `agresividad_basc3`, `hiperactividad_basc3`, `problemas_conducta_basc3`, `problemas_atencion_basc3`, `atipicidad_basc3` |
| Función ejecutiva | `fluidez_fonologica` |

**Categorías diagnósticas:** desarrollo típico y los tres subtipos de TDAH (inatento, hiperactivo/impulsivo y combinado), solos o con una condición asociada:

| Sigla | Significado |
|---|---|
| TND | Trastorno negativista desafiante |
| TEA | Trastorno del espectro autista |
| TEAZ | Trastorno específico del aprendizaje *(definición por confirmar con el equipo clínico)* |

<!-- TODO (equipo): sección "Origen de los datos y consideraciones éticas": institución, periodo de recolección, aval ético o consentimiento y proceso de anonimización. -->

## Notebooks

Los notebooks siguen el flujo analítico del proyecto, de la limpieza de datos hasta el informe técnico.

| # | Notebook | Contenido |
|---|---|---|
| 1 | `preprocessing.ipynb` | Limpieza, codificación, control de consistencia y exportación de datos procesados |
| 2 | `eda_univariate.ipynb` | Distribución individual de cada variable: normalidad, valores atípicos, asimetría (rúbrica: 94/100) |
| 3 | `eda_bivariate.ipynb` | Relaciones variable–`etiqueta`: Kruskal-Wallis, Dunn, Chi², perfiles z (rúbrica: 95/100) |
| 4 | `model_4clases.ipynb` | Clasificación en 4 tipos diagnósticos principales usando el perfil BASC-3 |
| 5 | `model_13clases.ipynb` | Clasificación de las 13 categorías diagnósticas (Random Forest, XGBoost, regresión logística) |
| 6 | `error_analysis.ipynb` | Análisis de errores: tipos, confianza del modelo y pares de confusión más frecuentes |
| 7 | `comorbidity_importance.ipynb` | Importancia de variables por condición asociada (TND, TEAZ, TEA) mediante clasificadores binarios |
| 8 | `ablation_study.ipynb` | Estudio de ablación: impacto en el rendimiento al retirar bloques de variables |
| 9 | `informe_tecnico_13clases.ipynb` | Notebook integrador: reproduce los resultados del informe técnico en un solo flujo |
| 10 | `figuras_parametrizables.ipynb` | Código parametrizable para regenerar las figuras 5, 6 y 9 del informe |

La calidad de los notebooks de EDA se evalúa con `notebooks/rubrica_calidad_eda.md`.

## Informe técnico

El informe técnico completo se encuentra en `EDA-TDAH/`. Documenta el proceso analítico de principio a fin: preprocesamiento, EDA bivariado, comparación de modelos, importancia de variables, análisis de errores, estudio de ablación, conclusiones y limitaciones.

**Resultados principales** (según el informe técnico):

| Modelo | CV F1-macro | DE | Test F1-macro | Test Accuracy |
|---|:---:|:---:|:---:|:---:|
| Regresión logística | 0.841 | 0.024 | 0.851 | 0.874 |
| **Random Forest** | **0.953** | **0.018** | **0.942** | **0.954** |
| XGBoost | 0.934 | 0.022 | 0.941 | 0.949 |

Random Forest se eligió por su mayor F1-macro en validación cruzada (0.953 frente a 0.934 de XGBoost). En el conjunto de prueba ambos quedan prácticamente empatados. Entre las ejecuciones de los distintos notebooks, el F1-macro de prueba de Random Forest varía entre 0.942 y 0.952.

El bloque BASC-3 concentra la mayor parte del poder discriminante: retirarlo reduce el F1-macro de prueba de 0.942 a 0.258 (`ablation_study.ipynb`). Los errores se concentran en la frontera entre subtipos con perfiles sintomáticos cercanos.

## Interfaz

Prototipo web que usa el modelo Random Forest para sugerir el perfil de un caso entre las 13 categorías. Muestra si la sugerencia está bien diferenciada, no es concluyente o requiere revisión, junto con las variables que más influyeron y comparaciones con la muestra. Corre completamente en el navegador, sin servidor, y se publica con GitHub Pages desde `docs/`.

- **Enlace:** <https://jpospinalo.github.io/TDAH-data/> · modo presentación: <https://jpospinalo.github.io/TDAH-data/#presentar>
- **Código y cómo regenerarla:** [`app/README.md`](app/README.md)
- Es un prototipo de investigación con validación interna; **no es una herramienta diagnóstica**.

## Notas metodológicas

- Ninguna variable continua sigue una distribución normal (Shapiro-Wilk / KS). Todas las pruebas bivariadas son no paramétricas.
- Umbral diagnóstico para los índices TDAH: **≥ 0.5** (equivale a 6 de 9 síntomas DSM-5).
- Puntuaciones T del BASC-3: **T ≥ 60** = en riesgo · **T ≥ 70** = clínicamente significativo (media = 50, DE = 10).
- Los índices `indice_tdah`, `indice_inatencion` e `indice_impuls_hiperac` se excluyeron del modelamiento por circularidad (fuga de información o *leakage*): codifican directamente los criterios DSM-5 con los que se asigna el subtipo de TDAH. Como control adicional, ninguna variable conservada alcanza por sí sola un F1-macro ≥ 0.70 en el problema de 13 clases.
- El análisis bivariado agrupa las 13 etiquetas en 4 tipos principales para las visualizaciones.
- Todos los resultados corresponden a validación interna; no deben interpretarse como evidencia de generalización externa.

## Cómo reproducir

```bash
pip install -r requirements.txt          # dependencias de los notebooks
jupyter lab notebooks/                   # ejecutar en el orden de la tabla de notebooks

pip install -r app/requirements.txt      # versiones exactas usadas por la interfaz
python app/construir_modelo_y_app.py     # reentrena el modelo y regenera docs/index.html
```

## Estructura del proyecto

```
TDAH-data/
├── data/
│   ├── raw/                          # Datos originales (xlsx, csv, equivalencias)
│   └── processed/
│       └── processed_data.csv        # Dataset limpio listo para análisis
├── app/                              # Interfaz: script de construcción y plantilla
├── docs/
│   └── index.html                    # Interfaz publicada con GitHub Pages
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
├── requirements.txt                  # Dependencias de los notebooks
├── .gitignore
├── LICENCE
└── Readme.md
```

## Licencia y cita

Código y documentación bajo licencia [Apache 2.0](LICENCE).

Si usas este material, cita el repositorio: *jpospinalo (2026). TDAH-data: análisis, modelos e interfaz de apoyo a la decisión clínica para TDAH infantil. GitHub. <https://github.com/jpospinalo/TDAH-data>*
