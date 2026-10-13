# Conversor de temperaturas

Programa en Python, ejecutable desde la terminal, que convierte temperaturas entre **Celsius**, **Fahrenheit** y **Kelvin**. El proyecto incluye su documentación, generada con [MkDocs](https://www.mkdocs.org/).

## Funcionalidades

- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Celsius → Kelvin
- Kelvin → Celsius
- Menú interactivo con control de errores (opciones o valores no válidos)

## Requisitos

- Python 3.8 o superior
- Git
- MkDocs (solo para ver o generar la documentación)

## Instalación

1. Clona el repositorio:

```bash
   git clone https://github.com/Marcosgarpu/Tarea-1.-Documentar-una-aplicaci-n-.git
   cd conversor
```

2. Crea y activa un entorno virtual:

```bash
   python -m venv .venv

   # Windows (PowerShell)
   .venv\Scripts\activate

   # Linux / macOS
   source .venv/bin/activate
```

3. Instala las dependencias:

```bash
   pip install -r requirements.txt
```

## Uso

Ejecuta el programa:

```bash
python conversor.py
```

Ejemplo de ejecución:

```
=== CONVERSOR DE TEMPERATURAS ===
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Celsius a Kelvin
4. Kelvin a Celsius
5. Salir
Elige una opción (1-5): 1
Introduce la temperatura: 100
100.0 °C = 212.00 °F
```

## Documentación

La documentación está hecha con MkDocs.

Para verla en local (con recarga automática):

```bash
mkdocs serve
```

Después abre <http://127.0.0.1:8000> en el navegador.

Para generar el sitio final (se crea la carpeta `site/`):

```bash
mkdocs build
```

## Estructura del proyecto

```
conversor/
├── conversor.py
├── README.md
├── .gitignore
├── mkdocs.yml
├── requirements.txt
└── docs/
    ├── index.md
    ├── instalacion.md
    └── uso.md
```

## Control de versiones

El proyecto usa Git con ramas `feature/*` para cada cambio, que se fusionan en `develop` y posteriormente en `main` cuando están probados.

## Autor

Marcos García Puche