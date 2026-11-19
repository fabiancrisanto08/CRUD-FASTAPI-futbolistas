# API de futbolistas

API REST desarrollada con FastAPI para consultar y administrar una lista de futbolistas. Los datos se guardan en `futbolistas.json`; al crear un futbolista, la API asigna automáticamente un ID.

## Requisitos

- Python 3
- Dependencias del proyecto

## Cómo arrancar

Desde la carpeta del proyecto, instala las dependencias y ejecuta la aplicación:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

La API estará disponible en <http://127.0.0.1:8000>. La documentación interactiva de FastAPI está en <http://127.0.0.1:8000/docs>.

## Rutas

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Devuelve un mensaje de bienvenida. |
| `GET` | `/futbolistas` | Devuelve todos los futbolistas. |
| `GET` | `/futbolistas/{id}` | Busca un futbolista por su ID. |
| `POST` | `/futbolistas` | Añade un futbolista y le asigna el siguiente ID. |
| `PUT` | `/futbolistas/{id}` | Actualiza nombre, equipo y posición del futbolista indicado. |
| `DELETE` | `/futbolistas/{id}` | Elimina el futbolista indicado. |

Para crear o actualizar un futbolista, envía un cuerpo JSON con estos campos:

```json
{
  "nombre": "Nombre del futbolista",
  "equipo": "Nombre del equipo",
  "posicion": "Posición en el campo"
}
```

y para levantar el servidor necesitas estos comandos en la 
terminal de powershell, git bash o la que se te haga mas comoda

#ACTIVAR EL ENTORNO VIRTUAL : .\.venv\Scripts\Activate.ps1
#LEVANTAR EL SERVIDOR O FASTAPI (CONTROLADOR): fastapi dev main.py