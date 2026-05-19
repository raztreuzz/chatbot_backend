# Zara Chatbot Backend

Zara es un bot academico construido con FastAPI y Dialogflow. Su webhook responde consultas sobre cursos, horarios, fechas de parciales e informacion general de materias registradas.

El proyecto expone un endpoint compatible con fulfillment de Dialogflow:

- `GET /`: estado basico del servicio.
- `GET /health`: verificacion de salud para Docker, Ansible y Jenkins.
- `POST /webhook`: endpoint principal usado por Dialogflow.

## Funcionalidades

- Consulta de horarios por curso.
- Consulta de fechas de parciales.
- Consulta de temas e informacion del curso.
- Actualizacion de fecha de parcial desde una intencion de Dialogflow.
- Normalizacion de nombres de cursos y alias como `ia`, `a2`, `redes 1`.

## Stack

- Python
- FastAPI
- Uvicorn
- Dialogflow
- Docker Compose
- Jenkins + Ansible para despliegue

## Documentacion

La documentacion tecnica, flujo de codigo y capturas de Dialogflow estan en:

[Ver documentacion del proyecto](docs/documentacion.md)

## Ejecucion local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Levantar el webhook:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Probar salud:

```bash
curl http://localhost:8000/health
```

## Despliegue

El despliegue esta preparado para Jenkins y Ansible. El pipeline usa credenciales de Jenkins para recibir el archivo `.env` y el `docker-compose.yml` de despliegue, sincroniza el proyecto al servidor y levanta el contenedor.
