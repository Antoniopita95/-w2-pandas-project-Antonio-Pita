def coincidencia (patron, string):
    import re
    dni = re.search(patron, string)
    if dni is None:
        return 0
    return dni.group().lower()