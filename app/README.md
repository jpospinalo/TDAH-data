# Interfaz "Perfil TDAH" (prototipo)

Interfaz web de apoyo a la decisión clínica construida sobre el modelo Random Forest de `notebooks/model_13clases.ipynb`. Se publica con GitHub Pages desde `docs/index.html`.

- **Para qué sirve:** sugiere el perfil más probable entre las 13 categorías diagnósticas a partir de 14 variables (demografía, antecedentes, BASC-3, CIT y fluidez fonológica). Indica si la sugerencia está bien diferenciada, no es concluyente o requiere revisión por datos fuera de rango.
- **Cómo funciona:** los 300 árboles del modelo van dentro de la página y se evalúan en el navegador. No hay servidor y los datos ingresados no salen del equipo de quien la usa.
- **Estado:** prototipo de investigación con validación interna (875 casos, un centro). **No es una herramienta diagnóstica.**

## Regenerar la página

Desde la raíz del repositorio:

```bash
pip install -r app/requirements.txt
python app/construir_modelo_y_app.py
```

El script:

1. entrena el Random Forest (300 árboles, `min_samples_leaf=2`, `class_weight="balanced"`, `random_state=42`) con los 875 casos de `data/processed/processed_data.csv`;
2. imprime las métricas de validación cruzada de 10 particiones que muestra la interfaz;
3. exporta los árboles y verifica que la inferencia en JavaScript da las mismas probabilidades que scikit-learn;
4. genera los casos ilustrativos y los datos auxiliares;
5. escribe `docs/index.html`.

El modelo entrenado (`modelo_rf_tdah.joblib`) y los datos de la página (`payload.json`) quedan en `app/salida/`, que no se versiona.

## Archivos

| Archivo | Contenido |
|---|---|
| `construir_modelo_y_app.py` | Entrenamiento, verificación y construcción de la página |
| `template.html` | Interfaz (HTML, CSS y JavaScript); el script inserta el modelo en ella |
| `requirements.txt` | Versiones usadas (scikit-learn 1.9.1, numpy 2.5.3, pandas 3.0.5, joblib 1.6.0) |

Con otras versiones de scikit-learn, el Random Forest puede variar levemente.

## Pendientes antes de un uso más amplio

- Confirmar con el equipo clínico qué significa **TEAZ** (hoy figura como "trastorno específico del aprendizaje, por confirmar") y la escala de **escolaridad** (1–7, asumida como grado escolar).
- Calibrar los puntajes y el umbral preliminar de 60.
- Validación externa con datos de otra institución.
