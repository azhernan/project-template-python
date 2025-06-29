import os
from pathlib import Path
import subprocess

project_name = input("Nombre del proyecto: ").strip()
base_path = Path.cwd() / project_name

# Crear estructura
(base_path / "src").mkdir(parents=True, exist_ok=True)
(base_path / "notebooks").mkdir(parents=True, exist_ok=True)
(base_path / ".vscode").mkdir(parents=True, exist_ok=True)
(base_path / "data").mkdir(parents=True, exist_ok=True)

# Crear archivos básicos
(base_path / "README.md").write_text(f"# {project_name}\n\nProyecto generado automáticamente.")
(base_path / ".gitignore").write_text(".venv/\n__pycache__/\n*.pyc\n.ipynb_checkpoints/\n")
(base_path / "requirements.txt").write_text("# Dependencias adicionales opcionales\n")
(base_path / ".vscode/settings.json").write_text(
    '{\n  "python.defaultInterpreterPath": ".venv/Scripts/python.exe",\n  "python.terminal.activateEnvironment": true\n}'
)

# Archivos dentro de src/
(base_path / "src/__init__.py").write_text("# Paquete inicializado\n")
(base_path / "src/main.py").write_text(
    "def main():\n    print('Proyecto ejecutado correctamente.')\n\n\nif __name__ == '__main__':\n    main()\n"
)

# Iniciar proyecto con Poetry
subprocess.run(["poetry", "init", "--name", project_name, "--no-interaction"], cwd=base_path)

print(f"Proyecto '{project_name}' creado con éxito en {base_path}")
