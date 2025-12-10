# 📰 **Sistema de Análisis de Noticias con APIs Múltiples**  
### **PEP 8 · Ruff · Arquitectura Modular · Escalable**

> Un sistema diseñado para recopilar, limpiar, validar y procesar noticias desde múltiples APIs utilizando buenas prácticas de ingeniería, arquitectura clara y herramientas de calidad.

---

## 🎯 **Tabla de Contenidos**
- [🌐 Descripción General](#-descripción-general)
- [✨ Características Principales](#-características-principales)
- [🏗️ Arquitectura del Proyecto](#️-arquitectura-del-proyecto)
- [⚙️ Instalación y Configuración](#️-instalación-y-configuración)
- [🚀 Ejemplo de Uso](#-ejemplo-de-uso)
- [📏 Estándares y Buenas Prácticas](#-estándares-y-buenas-prácticas)
- [🛠️ Ruff y Automatización](#️-ruff-y-automatización)
- [📦 Requisitos](#-requisitos)
- [🤝 Contribuciones](#-contribuciones)
- [📄 Licencia](#-licencia)

---

# 🌐 **Descripción General**

Este proyecto implementa un sistema modular para realizar análisis de noticias provenientes de múltiples fuentes externas.  
Incluye:

- Arquitectura escalable basada en módulos.  
- Procesos de normalización y limpieza de texto.  
- Validación de credenciales y parámetros.  
- Estandarización estricta bajo PEP 8 + Ruff.

---

# ✨ **Características Principales**

| ⭐ Característica | 📘 Descripción |
|------------------|----------------|
| **Modularidad** | Separación clara en `utils`, `services` y `config`. |
| **Estándares PEP 8** | Código limpio, ordenado y con estilo uniforme. |
| **Linting con Ruff** | Corrección automática y verificación continua. |
| **Escalable** | Permite agregar nuevos proveedores de noticias. |
| **Docstrings profesionales** | Documentación en español en todo el proyecto. |

---

# 🏗️ **Arquitectura del Proyecto**

```plaintext
📦 news-multiapi-system
│
├── README.md
├── main.py
│
├── utils/
│   ├── cleaner.py            # Limpieza y normalización de texto
│   ├── validator.py          # Validación de parámetros y API keys
│   └── __init__.py
│
├── services/
│   ├── news_api.py           # Cliente para NewsAPI
│   ├── gnews_api.py          # Cliente para GNews
│   ├── aggregator.py         # Unificación y normalización de datos
│   └── __init__.py
│
├── config/
│   ├── ruff.toml             # Reglas de linting y formateo
│   ├── settings.json         # Configuración de editor
│   └── credentials_example.json
│
└── requirements.txt


