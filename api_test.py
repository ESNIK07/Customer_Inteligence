import requests

def obtener_lista_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Manejar errores HTTP
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return None

def obtener_info_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Manejar errores HTTP
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información del usuario {user_id}: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    lista_usuarios = obtener_lista_usuarios()

    if lista_usuarios:
        print("Lista de usuarios:")
        for usuario in lista_usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['name']}")

        # Obtener información detallada del primer usuario en la lista
        user_id = lista_usuarios[0]['id']
        info_usuario = obtener_info_usuario(user_id)

        if info_usuario:
            print("\nInformación detallada del usuario:")
            print(f"ID: {info_usuario['id']}")
            print(f"Nombre: {info_usuario['name']}")
            print(f"Email: {info_usuario['email']}")
    else:
        print("No se pudo obtener la lista de usuarios.")
