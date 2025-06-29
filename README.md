# 🧱 Project Template (Python + Poetry + VS Code)

Plantilla base para iniciar proyectos en Python de forma organizada y reproducible. Incluye integración con Poetry, estructura modular y configuración automática para Visual Studio Code.

---

## 📁 Estructura del proyecto

```
project-name/
│
├── .vscode/
│   └── settings.json           ← VS Code detecta el entorno automáticamente
│
├── data/                       ← Datos de entrada / salida
├── notebooks/                  ← Jupyter Notebooks
├── src/                        ← Código fuente Python
│   └── main.py
│
├── README.md
├── .gitignore
└── pyproject.toml              ← Se genera con `poetry init`
```

---

## 🚀 Cómo usar esta plantilla

### Opción 1: Clonar desde GitHub

```bash
git clone https://github.com/azhernan/project-template-python.git nuevo-proyecto
cd nuevo-proyecto
rmdir /s /q .git           # Elimina el historial del repo plantilla
poetry init --name nuevo-proyecto
poetry config virtualenvs.in-project true
```

Opcional: abrir con Visual Studio Code

```bash
code .
```

---

### Opción 2: Usar con script automatizado

```bat
REM Script .bat recomendado:
git clone https://github.com/azhernan/project-template-python.git %name%
cd %name%
rmdir /s /q .git
poetry init --name %name% --no-interaction
poetry config virtualenvs.in-project true
code .
```

---

## ⚙️ Requisitos

- [Python 3.12+](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/)
- [Visual Studio Code](https://code.visualstudio.com/)
- Git (para clonar el repo)

---

## 🧠 Consejos

- Mantené tus proyectos separados por entorno con Poetry (`.venv` en cada uno)
- Usá `poetry add` para instalar paquetes de forma controlada
- Ejecutá scripts con `poetry run python src/main.py`
- Organizá bien tus datos y notebooks desde el inicio

---

## ✍️ Autor

Plantilla creada por **Hernán Velázquez**  
[GitHub](https://github.com/hernanvelazquez)

---

## 🪪 Licencia

MIT License
