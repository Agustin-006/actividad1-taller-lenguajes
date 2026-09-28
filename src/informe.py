"""
Lógica para generar el informe de columnas según el rol solicitado.

Se separa de datos.py a propósito: acá vive el "cómo se procesa",
en datos.py vive el "qué datos hay". Así, agregar una columna o un rol
nuevo no obliga a tocar ni una línea de esta función.
"""

from datos import COLUMNAS, ROLES


def generar_informe(rol=None, columnas=COLUMNAS, roles=ROLES):
    """
    Genera el informe de columnas correspondiente a un rol.

    Parámetros
    ----------
    rol : str, opcional
        Nombre del rol a informar ('docente', 'investigador', 'analista').
        Si no se especifica (o es None), se informan TODAS las columnas,
        ordenadas por completitud de forma descendente (comportamiento
        por defecto pedido en la consigna).
    columnas : dict, opcional
        Diccionario con la info de cada columna (nombre -> tipo, completitud).
        Tiene un valor por defecto (COLUMNAS) para no tener que pasarlo
        siempre a mano.
    roles : dict, opcional
        Diccionario con la configuración de cada rol. También tiene un
        valor por defecto (ROLES).

    Devuelve
    -------
    list[tuple]
        Lista de tuplas (nombre_columna, tipo, completitud), ya filtradas
        por el mínimo de completitud (si corresponde) y ordenadas según
        el criterio y la dirección configurados para el rol.

    Lanza
    -----
    ValueError
        Si el rol pide un criterio de orden ("orden_por") que no es
        "nombre" ni "completitud". Esto evita que el programa falle de
        forma confusa (por ejemplo, con un KeyError sin explicación) ante
        un dato de configuración mal cargado.
    """
    if rol is None:
        # Comportamiento por defecto exigido por la consigna:
        # todas las columnas, ordenadas por completitud, descendente.
        nombres = list(columnas.keys())
        orden_por = "completitud"
        direccion = "B"
        minimo = None
    else:
        config = roles[rol]  # si el rol no existe, se busca a propósito que rompa acá
        nombres = config["columnas"]
        orden_por = config["orden_por"]
        direccion = config["direccion"]
        minimo = config.get("minimo")  # get(): si no está la clave, da None en vez de error

    # --- filter(): descarta las columnas por debajo del mínimo, si hay uno ---
    if minimo is not None:
        nombres = list(
            filter(lambda nombre: columnas[nombre]["completitud"] >= minimo, nombres)
        )

    # --- map(): arma una lista de tuplas (nombre, tipo, completitud) ---
    filas = list(
        map(lambda nombre: (nombre, columnas[nombre]["tipo"], columnas[nombre]["completitud"]),
            nombres)
    )

    # --- sorted(): ordena según el criterio pedido ---
    if orden_por == "nombre":
        clave = lambda fila: fila[0]
    elif orden_por == "completitud":
        clave = lambda fila: fila[2]
    else:
        raise ValueError(
            f"Criterio de orden desconocido: {orden_por!r}. "
            "Los valores válidos son 'nombre' o 'completitud'."
        )

    es_descendente = (direccion == "B")
    return sorted(filas, key=clave, reverse=es_descendente)


def mostrar_informe(filas):
    """
    Imprime en pantalla una lista de filas (nombre, tipo, completitud)
    con un formato prolijo, alineado en columnas.
    """
    print(f"{'COLUMNA':<15}{'TIPO':<10}{'COMPLETITUD':>12}")
    print("-" * 37)
    for nombre, tipo, completitud in filas:
        print(f"{nombre:<15}{tipo:<10}{completitud:>11}%")
  