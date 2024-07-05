### README.md

# MHC_Streamlit_Software

## Descripción

MHC_Streamlit_Software es una aplicación desarrollada para el Manta Hospital Center. Esta aplicación facilita la gestión de usuarios, roles y diferentes módulos específicos del hospital, permitiendo a los administradores y otros roles del hospital interactuar de manera eficiente con el sistema. La aplicación está desarrollada utilizando Streamlit como frontend y SQLite como base de datos, implementando autenticación y autorización mediante JWT.

## Características

- **Autenticación y Autorización**: Gestión de acceso mediante JWT.
- **Roles y Permisos**: Gestión de usuarios y roles con diferentes permisos.
- **Interfaz Amigable**: Interfaz de usuario intuitiva y fácil de usar con Streamlit.
- **Base de Datos**: Uso de SQLite para la gestión de datos.
- **Panel de Administración**: Herramientas y paneles para la gestión de usuarios y roles.
- **Funciones Especializadas por Rol**: Acceso a diferentes módulos y paneles según el rol del usuario.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/MHC_Streamlit_Software.git
    cd MHC_Streamlit_Software
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # En Windows
    source venv/bin/activate  # En MacOS/Linux
    ```

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicializa la base de datos:
    ```bash
    python database/db_setup.py
    ```

## Uso

1. Inicia la aplicación Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Abre tu navegador web y ve a `http://localhost:8501`.

3. Inicia sesión con las credenciales del administrador por defecto:
    - **Usuario**: `admin`
    - **Contraseña**: `Ilargietaeguzki1`

4. Desde el panel de administrador, puedes gestionar usuarios, roles y otros módulos específicos del hospital.

## Funcionalidades del Proyecto

### Panel de Administración

- **Crear Usuario**: Formulario para agregar nuevos usuarios al sistema.
- **Lista de Usuarios**: Visualización de usuarios existentes en formato de tabla.
- **Editar Usuario**: Formulario para editar información de usuarios existentes.
- **Borrar Usuario**: Opción para eliminar usuarios del sistema.

### Manejo de Roles

- **Crear Rol**: Formulario para agregar nuevos roles al sistema.
- **Lista de Roles**: Visualización de roles existentes en formato de tabla.
- **Editar Rol**: Formulario para editar información de roles existentes.
- **Borrar Rol**: Opción para eliminar roles del sistema.

### Funciones Específicas por Rol

#### Administrador
- Gestión completa de usuarios y roles.
- Acceso a todos los módulos del sistema.

#### Responsable de TIC
- Gestión y supervisión de tecnología e información hospitalaria.
- Paneles de monitoreo y estadísticas de sistemas informáticos.
- Herramientas de seguridad informática y gestión de acceso.

#### Otros Roles
- Acceso a módulos específicos según el rol asignado.

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin nueva-funcionalidad`).
5. Abre un Pull Request.

## Soporte

Si tienes alguna pregunta o necesitas ayuda, por favor, abre un issue en el repositorio o contacta con el soporte a través de [aquí](https://wa.me/5930993513082?text=Solicito%20ayuda%20con%20la%20app%20MHC).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

¡Gracias por usar MHC_Streamlit_Software!