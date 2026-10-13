# Uso

## Ejecutar la aplicación

Con el entorno virtual activado, desde la carpeta del proyecto:

```bash
python conversor.py
```

## Funcionamiento

1. El programa muestra un menú con las conversiones disponibles.
2. Eliges una opción.
3. Introduces el valor a convertir.
4. El programa muestra el resultado.

## Ejemplo de ejecución

> Sustituye este bloque por la salida **real** de tu programa (copia y pega desde la terminal).

```text
=== CONVERSOR DE TEMPERATURAS ===
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Celsius a Kelvin
Elige una opción: 1
Introduce la temperatura en °C: 25
25.0 °C equivalen a 77.0 °F
```

## Fórmulas utilizadas

| Conversión | Fórmula |
|---|---|
| Celsius a Fahrenheit | `F = C × 9/5 + 32` |
| Fahrenheit a Celsius | `C = (F − 32) × 5/9` |
| Celsius a Kelvin | `K = C + 273.15` |

## Posibles errores

- **`python` no se reconoce como comando:** prueba con `python3` o revisa que Python esté en el PATH.
- **El entorno virtual no se activa en PowerShell:** puede que necesites permitir la ejecución de scripts con `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.