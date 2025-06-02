
import os

def handle_request():
    ruta = "D:/proyecto/Vero2.0/core/TEST_DE_VERDAD.txt"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("✅ Esto fue creado automáticamente desde el servidor Vero-Bridge con conexión 100% REAL.
")
    print("Archivo creado en:", ruta)
