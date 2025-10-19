# crud-fastApi-mongodb-motor
 API de Gestión de Almacén


La API de Gestión de Almacén es un servicio RESTful desarrollado con FastAPI y MongoDB (Motor) que permite administrar los productos de un almacén de forma sencilla y eficiente.
Incluye operaciones como Crear, Leer y Eliminar con validaciones de datos y manejo de errores.

<img width=400px src="img/Captura de pantalla 2025-10-19 145937.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 145618.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 145633.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 150425.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 151032.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 145539.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 155600.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 155631.png">

<img width=400px src="img/Captura de pantalla 2025-10-19 155645.png">


# ⚙️ Características principales

* 🚀 Desarrollada con FastAPI (framework moderno, rápido y asíncrono).

* 🧩 Base de datos MongoDB, conectada mediante Motor (driver async).

* ✅ Validaciones automáticas con Pydantic.

* 🛠️ Endpoints RESTful bien estructurados:

  * GET /producto → listar todos los productos

  * GET /producto/{codigo} → obtener un producto por código

  * POST /producto → crear un nuevo producto


  * DELETE /producto/{codigo} → eliminar un producto

* 🚫 Validación de códigos duplicados.

* 📄 Documentación automática disponible en /docs (Swagger UI) y /redoc

# 🧰 Tecnologías utilizadas

* FastAPI:framework para construir APIs rápidas con Python.

* Motor: cliente asíncrono para MongoDB.

* MongoDB: Base de datos NoSQL orientada a documentos.

* Pydantic:validación de modelos y tipado.

* Docker:contenedores para despliegue simple y portable.
