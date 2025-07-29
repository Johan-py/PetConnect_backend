# 🐾 PetConnect Backend

![Django](https://img.shields.io/badge/Django-5.2-green?logo=django\&logoColor=white\&style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql\&logoColor=white\&style=flat)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render\&logoColor=white\&style=flat)

## 📖 Descripción

Este es el **backend de PetConnect**, desarrollado con **Django REST Framework** y desplegado en **Render**.
Se encarga de manejar la lógica de negocio, persistencia de datos y la API que consume el frontend.

Funcionalidades principales:

* 👤 **Gestión de usuarios**.
* 🐕 **Registro de mascotas**.
* 🗓️ **Manejo de citas veterinarias**.
* 📢 **Publicaciones globales** visibles en el chat.
* 🚨 **Alertas importantes** (ejemplo: mascotas perdidas), notificadas en tiempo real al frontend.

👉 El backend se conecta a una base de datos **PostgreSQL en la nube** y expone una API REST segura y escalable.

---

## 🚀 Tecnologías utilizadas

* 🐍 **Django 5.2** – Framework backend.
* ⚡ **Django REST Framework (DRF)** – Creación de APIs.
* 🐘 **PostgreSQL** – Base de datos en producción.
* 🔒 **CORS + Middleware de seguridad** – Para conexión con frontend.
* ☁️ **Render** – Despliegue del backend.

---

## 📂 Estructura principal

```bash
petconnect-backend/
│── alertas/           # App para alertas
│── citas/             # App para manejo de citas
│── mascotas/          # App para mascotas
│── publicaciones/     # App para publicaciones
│── usuarios/          # App para usuarios
│── petconnect/        # Configuración principal del proyecto
│
├── manage.py          # Comando principal de Django
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Este archivo 😃
```

---

## ⚙️ Instalación y ejecución local

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Johan-py/PetConnect_backend.git
   cd petconnect-backend
   ```

2. Crear entorno virtual e instalar dependencias:

   ```bash
   python -m venv env
   source env/bin/activate   # Linux/Mac
   env\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Configurar variables de entorno en `.env`:

   ```env
   DB_NAME=petconnect
   DB_USER=postgres
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=clave_secreta_django
   DEBUG=True
   ```

4. Migraciones y ejecución del servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

El backend estará disponible en 👉 `http://127.0.0.1:8000`

---

## 🌐 Endpoints principales

| Método     | Endpoint                          | Descripción          |
| ---------- | --------------------------------- | -------------------- |
| **GET**    | `/api/mascota/mascotas/`          | Listar mascotas      |
| **POST**   | `/api/mascota/crear/`             | Crear nueva mascota  |
| **GET**    | `/api/publicacion/publicaciones/` | Listar publicaciones |
| **POST**   | `/api/publicacion/crear/`         | Crear publicación    |
| **POST**   | `/api/alertas/crear/`             | Crear alerta         |
| **DELETE** | `/api/alertas/eliminar/{id}/`     | Eliminar alerta      |
| **POST**   | `/api/citas/crear/`               | Crear cita           |
| **POST**   | `/api/citas/cancelar/{id}/`       | Cancelar cita        |

---

## 🌍 Deploy

El backend está desplegado en **Render**:
👉 [PetConnect Backend](https://petconnect-backend-la15.onrender.com)

El frontend está desplegado en **Vercel**:
👉 [PetConnect Frontend](https://pet-connect-frontend-three.vercel.app)

---


### 📢 Crear alerta

**Request**

```json
POST /api/alertas/crear/
{
  "contexto": "Se perdió en el parque central",
  "tipo": "perdida"
}
```

**Response**

```json
{
  "id_alerta": "a62732e47490463b8bb55fcb617e6d89",
  "tipo": "perdida"
}
```

---

## 👨‍💻 Autor

**Johan Beltrán**
📌 Estudiante de Ingeniería Informatica | Enfocado en **Python, Java y Rust**
🌍 [LinkedIn](https://www.linkedin.com/in/johan-beltran-backend-dev) | [GitHub](https://github.com/Johan-py)
---

✨ *“Backend sólido para una comunidad que conecta personas y mascotas”*

---

👉 ¿Quieres que te arme un **README conjunto estilo fullstack** (frontend + backend en un solo repo con monorepo o documentación unificada) para que luzca como un proyecto completo?
