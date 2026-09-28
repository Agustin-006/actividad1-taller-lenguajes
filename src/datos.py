
# ---------------------------------------------------------------------------
# 1) COLUMNAS: diccionario de diccionarios.
#    Clave externa: nombre de la columna.
#    Valor: otro diccionario con "tipo" y "completitud".
# ---------------------------------------------------------------------------
COLUMNAS = {
    "PONDERA":    {"tipo": "int",    "completitud": 100},
    "ESTADO":     {"tipo": "int",    "completitud": 98},
    "CAT_OCUP":   {"tipo": "int",    "completitud": 85},
    "EDAD":       {"tipo": "int",    "completitud": 100},
    "REGION":     {"tipo": "int",    "completitud": 100},
    "AGLOMERADO": {"tipo": "int",    "completitud": 100},
    "MAS_500":    {"tipo": "string", "completitud": 100},
    "ANO4":       {"tipo": "int",    "completitud": 100},
    "TRIMESTRE":  {"tipo": "int",    "completitud": 100},
    "ITF":        {"tipo": "int",    "completitud": 72},
    "GDECCFR":    {"tipo": "int",    "completitud": 68},
}

# ---------------------------------------------------------------------------
# 2) ROLES: qué columnas ve cada rol, cómo se ordenan, y si hay un mínimo
#    de completitud exigido.
#
#    "orden_por"  -> "nombre" (alfabético) o "completitud"
#    "direccion"  -> "A" (ascendente) o "B" (descendente)
#    "minimo"     -> número (0-100) o None si el rol no filtra por completitud
# ---------------------------------------------------------------------------
ROLES = {
    "docente": {
        "columnas": ["EDAD", "REGION", "ESTADO", "CAT_OCUP"],
        "orden_por": "nombre",
        "direccion": "A",
        "minimo": None,
    },
    "investigador": {
        "columnas": ["ITF", "GDECCFR", "CAT_OCUP", "ESTADO", "EDAD"],
        "orden_por": "completitud",
        "direccion": "B",
        "minimo": 70,
    },
    "analista": {
        "columnas": list(COLUMNAS.keys()),  # le interesan TODAS las columnas
        "orden_por": "completitud",
        "direccion": "B",
        "minimo": 90,
    },
}
