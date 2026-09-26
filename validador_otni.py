import re

def validar_cliente(dni_cuit: str, nombre: str, email: str, telefono: str) -> tuple[bool, str]:
    """
    Valida los datos ingresados para un cliente de OTNI Textil.
    Retorna una tupla: (True, "Mensaje de éxito") o (False, "Mensaje de error").
    """
    # 1. Validación de DNI / CUIT
    dni_cuit_limpio = dni_cuit.strip()
    if not dni_cuit_limpio:
        return False, "El DNI/CUIT es un campo obligatorio."
    if not dni_cuit_limpio.isdigit():
        return False, "El DNI/CUIT debe contener únicamente números (sin puntos ni guiones)."
    if not (7 <= len(dni_cuit_limpio) <= 11):
        return False, "El DNI/CUIT debe tener entre 7 y 11 dígitos."

    # 2. Validación de Nombre / Razón Social
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return False, "El nombre o razón social es obligatorio."
    if len(nombre_limpio) < 2:
        return False, "El nombre debe tener al menos 2 caracteres."

    # 3. Validación de Email
    email_limpio = email.strip()
    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not email_limpio:
        return False, "El correo electrónico es obligatorio."
    if not re.match(patron_email, email_limpio):
        return False, "El formato del correo electrónico no es válido (ejemplo: cliente@mail.com)."

    # 4. Validación de Teléfono
    telefono_limpio = telefono.strip()
    if not telefono_limpio:
        return False, "El teléfono de contacto es obligatorio."
    if not re.match(r"^[0-9\+\-\s]+$", telefono_limpio):
        return False, "El teléfono contiene caracteres no válidos."

    return True, "Cliente validado correctamente."


def validar_producto(codigo: str, descripcion: str, precio: str, stock: str) -> tuple[bool, str]:
    """
    Valida los datos ingresados para un producto (indumentaria o accesorio de seguridad).
    Retorna una tupla: (True, "Mensaje de éxito") o (False, "Mensaje de error").
    """
    # 1. Validación del Código de Producto
    codigo_limpio = codigo.strip()
    if not codigo_limpio:
        return False, "El código del producto es obligatorio."

    # 2. Validación de Descripción
    descripcion_limpia = descripcion.strip()
    if not descripcion_limpia:
        return False, "La descripción del producto es obligatoria."
    if len(descripcion_limpia) < 3:
        return False, "La descripción debe tener al menos 3 caracteres."

    # 3. Validación de Precio
    precio_limpio = precio.strip().replace(",", ".")
    try:
        precio_val = float(precio_limpio)
        if precio_val <= 0:
            return False, "El precio debe ser un número mayor a 0."
    except ValueError:
        return False, "El precio ingresado no es válido. Debe ser un número."

    # 4. Validación de Stock
    stock_limpio = stock.strip()
    try:
        stock_val = int(stock_limpio)
        if stock_val < 0:
            return False, "El stock no puede ser un valor negativo."
    except ValueError:
        return False, "El stock debe ser un número entero válido."

    return True, "Producto validado correctamente."