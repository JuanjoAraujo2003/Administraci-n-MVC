# Proyecto Admin-MVC

# Nombre del Proyecto: Task Management
Proyecto el cual se basa en poder crear diferentes proyectos por los administradores del sistema, en donde dentro de ellos se podran crear lo que son tareas con orden de prioridad y estatus
las cuales podran ser asignadas a los distintos empleados que se tengan creados en el momento para que las puedan realizar

Estos son los pasos para iniciar el entorno virtual, instalar Django y ejecutar el servidor con la ayuda de Django.

## Requisitos Previos
Asegúrate de tener Python 3 y pip instalados en nuestra máquina. 

## Pasos de Instalación

### 1. Clonar el Repositorio
Clona este repositorio en tu máquina local.

```bash
git clone <URL_del_repositorio>
cd <nombre_del_proyecto>
```

### 2. Iniciar un entorno virtual en Windows
Se recomienda el iniciar un entorno virtual de python con la finalidad de aislar las dependencias del proyecto

```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalar django en el entorno virtual del proyecto
Para poder utilizar el proyecto deberemos de instalar django

```bash
pip install -r requirements.txt
```

### 4. Ejecutar archivo requeriments.txt
Se debera de ejecutar el archivo requirements con la finalidad de descargar todas las dependencias necesarias del proyecto

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el proyecto
Una vez instalado todas las dependencias necesarias para el proyecto, podremos ejecutarlo con el siguiente comando

```bash
python manage.py runserver
```

