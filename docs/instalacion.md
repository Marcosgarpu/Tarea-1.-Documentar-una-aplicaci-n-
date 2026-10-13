# Instalación

## Requisitos

Antes de empezar, necesitas tener instalado:

- **Python 3.8 o superior**
- **pip** (el gestor de paquetes de Python, incluido con Python)
- **Git**

Puedes comprobarlo con:

```bash
python --version
pip --version
git --version
```

## Obtener el proyecto

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/Marcosgarpu/Tarea-1.-Documentar-una-aplicaci-n-.git
cd conversor
```

## Crear y activar el entorno virtual

Un entorno virtual mantiene las dependencias del proyecto aisladas del resto del sistema.

```bash
python -m venv .venv
```

Para activarlo:

- **Windows (PowerShell):**

```powershell
    .venv\Scripts\Activate.ps1
```

- **Linux / macOS:**

```bash
    source .venv/bin/activate
```

Cuando esté activo verás `(.venv)` al principio de la línea de la terminal.

## Instalar las librerias

```bash
pip install -r requirements.txt
```

## Ver la documentación en local

Para previsualizar esta documentación en el navegador:

```bash
mkdocs serve
```

Después abre `http://127.0.0.1:8000`.

Para generar el sitio web final en la carpeta `site/`:

```bash
mkdocs build
```