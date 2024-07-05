# admin_dashboard.py

import streamlit as st
from crud import create_user, read_users, update_user, delete_user
from crud import create_role, read_roles, update_role, delete_role

def admin_dashboard():
    st.sidebar.title("Panel de Administrador")

    st.sidebar.header("Manejo de usuarios")
    user_task = st.sidebar.selectbox("Seleccione tarea de usuario", ["Crear usuario", "Lista de usuarios", "Editar usuario", "Borrar usuario"])

    st.sidebar.header("Manejo Roles")
    role_task = st.sidebar.selectbox("Seleccione tarea de rol", ["Crear Rol", "Lista de roles", "Editar rol", "Borrar rol"])

    st.sidebar.write("---")

    if user_task == "Crear usuario":
        create_user_page()
    elif user_task == "Lista de usuarios":
        read_users_page()
    elif user_task == "Editar usuario":
        update_user_page()
    elif user_task == "Borrar usuario":
        delete_user_page()

    if role_task == "Crear Rol":
        create_role_page()
    elif role_task == "Lista de roles":
        read_roles_page()
    elif role_task == "Editar rol":
        update_role_page()
    elif role_task == "Borrar rol":
        delete_role_page()

def create_user_page():
    st.title("Crear Usuario")
    dni = st.text_input("DNI", key="create_user_dni")
    username = st.text_input("Nombre de usuario", key="create_user_username")
    password = st.text_input("Contraseña", type="password", key="create_user_password")
    roles = read_roles()  # Obtener la lista de roles actualizados
    role_names = [role[1] for role in roles]  # Obtener nombres de roles (suponiendo que el nombre está en la posición 1)
    role = st.selectbox("Rol", role_names, key="create_user_role")  # Mostrar nombres de roles en el selector
    selected_role_id = roles[role_names.index(role)][0]  # Obtener ID del rol seleccionado por su nombre
    if st.button("Crear", key="create_user_button"):
        if create_user(dni, username, password, selected_role_id):  # Pasar el ID del rol seleccionado
            st.success("Usuario creado exitosamente")
        else:
            st.error("Usuario ya existe")

def read_users_page():
    st.title("Usuarios")
    users = read_users()

    # Mostrar usuarios en forma de tabla
    if users:
        st.table(users)
    else:
        st.warning("No se encontraron usuarios.")

def update_user_page():
    st.title("Editar usuario")
    user_id = st.text_input("ID usuario", key="update_user_id")
    dni = st.text_input("DNI", key="update_user_dni")
    username = st.text_input("Nombre de usuario", key="update_user_username")
    password = st.text_input("Contraseña", type="password", key="update_user_password")
    roles = read_roles()
    role_names = [role[1] for role in roles]
    role = st.selectbox("Rol", role_names, key="update_user_role")
    selected_role_id = roles[role_names.index(role)][0]
    if st.button("Editar", key="update_user_button"):
        update_user(user_id, dni, username, password, selected_role_id)
        st.success("Usuario editado exitosamente")

def delete_user_page():
    st.title("Borrar usuario")
    user_id = st.text_input("ID usuario", key="delete_user_id")
    if st.button("Borrar", key="delete_user_button"):
        delete_user(user_id)
        st.success("Usuario borrado exitosamente")

def create_role_page():
    st.title("Crear Rol")
    role_name = st.text_input("Nombre rol", key="create_role_name")
    permissions = st.text_area("Permisos (separados por coma)", key="create_role_permissions")
    if st.button("Crear", key="create_role_button"):
        if create_role(role_name, permissions):
            st.success("Rol creado exitosamente")
        else:
            st.error("El rol ya existe")

def read_roles_page():
    st.title("Lista de roles")
    roles = read_roles()

    # Mostrar roles en forma de tabla
    if roles:
        st.table(roles)
    else:
        st.warning("No se encontraron roles disponibles.")

def update_role_page():
    st.title("Editar Rol")
    role_id = st.text_input("ID de Rol", key="update_role_id")
    role_name = st.text_input("Nombre de rol", key="update_role_name")
    permissions = st.text_area("Permisos (separados por coma)", key="update_role_permissions")
    if st.button("Editar", key="update_role_button"):
        update_role(role_id, role_name, permissions)
        st.success("Rol editado exitosamente")

def delete_role_page():
    st.title("Borrar Rol")
    role_id = st.text_input("ID de rol", key="delete_role_id")
    if st.button("Borrar", key="delete_role_button"):
        delete_role(role_id)
        st.success("Rol borrado exitosamente")
