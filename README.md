fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
alembic
python-jose
passlib[bcrypt]
python-dotenv
pydantic


🚀 Logika – Backend Technical Test (FastAPI)

API REST desarrollada como parte de la prueba técnica para el cargo Developer Junior – Backend (Python/FastAPI).
El proyecto implementa autenticación JWT, persistencia en PostgreSQL y un CRUD completo de tareas, siguiendo buenas prácticas de arquitectura, seguridad y mantenibilidad.

Arquitectura y enfoque
app/
├── api/        # Routers (endpoints)
├── core/       # Configuración, seguridad y autenticación
├── db/         # Conexión y sesión de base de datos
├── models/     # Modelos SQLAlchemy
├── schemas/    # Esquemas Pydantic
├── services/   # Lógica de negocio
└── main.py     # Punto de entrada

🛠️ Stack tecnológico

Python 3.11+

FastAPI

SQLAlchemy

Alembic (migraciones)

PostgreSQL (Docker)

JWT (OAuth2 Password Flow)

Autenticación

La API utiliza JWT (JSON Web Tokens) mediante el flujo estándar OAuth2 Password.

El token se genera al autenticarse.

Los endpoints protegidos requieren el header: Authorization: Bearer <token>


Usuario inicial

El sistema crea automáticamente un usuario inicial mediante una migración Alembic, evitando pasos manuales.
username: admin
password: admin123


Funcionalidades implementadas

Autenticación:

Login con usuario y contraseña
Generación de JWT con expiración configurable
Protección de endpoints mediante dependencias de FastAPI

Gestión de tareas (Task)

-Crear tarea
-Listar tareas con paginación real
-Obtener tarea por ID
-Actualizar tarea
-Eliminar tarea
-Cada tarea incluye:
-title (obligatorio)
-description (opcional)
-status (pending, in_progress, done)
-created_at


Persistencia y migraciones

PostgreSQL corre exclusivamente en entorno local mediante Docker.
Las tablas y datos iniciales se gestionan con Alembic.
El esquema de la base de datos se crea automáticamente ejecutando las migraciones.
Se definieron índices en campos relevantes (status, created_at) para optimizar consultas frecuentes.

Ejecución del proyecto:

git clone <https://github.com/String1s/logika-backend-test.git>
cd logika-backend-test

2. Variables de entorno

Crear un archivo .env basado en .env.example.   (No es del todo obligatorio, es por buenas practicas)

Levantar PostgreSQL
docker-compose up -d

pip install -r requirements.txt

python -m alembic upgrade head

uvicorn app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs






Uso desde Swagger

Acceder a /docs

Click en Authorize

Ingresar credenciales del usuario inicial

Probar los endpoints protegidos (/tasks)

Swagger maneja automáticamente el token JWT tras la autenticación.



Detalles tecnicos:

Argon2 fue elegido para el hashing de contraseñas por su mayor robustez y compatibilidad con versiones recientes de Python.

Se utilizó OAuth2 Password Flow para alinearse con el estándar recomendado por FastAPI.

PostgreSQL se ejecuta únicamente en Docker para asegurar reproducibilidad del entorno.

La lógica de negocio se desacopló de los endpoints para facilitar pruebas y escalabilidad.