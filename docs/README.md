# Sistema Web: Surtido-Pro

## Descripción
Es un sistema de gestión de stock mayorista y monorista con catálogo web para vender por redes sociales. 

---

## Estado de este commit (Diseño inicial)
Este commit tiene como objetivo dejar documentado el análisis y modelado del primer diseño del proyecto.

En su momento este estado del proyecto no fue versionado en Git. Sin embargo, se incorpora posteriormente para reflejar de manera más fiel la evolución real del sistema y conservar el punto de partida desde el cual se realizaron las mejoras posteriores.

El contenido incluido representa:
* Primer borrador del diagrama de clases.
* Primeras clases implementadas en Python.
* Implementación de atributos y métodos base.

---

## Tecnologías previstas

### Backend
* Python
* FastAPI

### Frontend
* Vue.js

---

# Requisitos

- Python 3.13
- MySQL / XAMPP

## Instalación
1. Clonar repositorio 
2. Crear el entorno virtual: 'python -m venv env'
3. Activarlo: 'env\Scripts\activate'
4. Instalar dependencias: 'pip install -r requirements.txt'
5. Copiar '.env.example' a '.env' y completar con tus credenciales. 

## Levantar servidor
uvicorn app.main:app --reload

## Verificar conexión
http://127.0.0.1:8000/db-test

## Swagger
http://127.0.0.1:8000/docs#/

---


