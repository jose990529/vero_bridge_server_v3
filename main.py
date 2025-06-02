import os

ruta = "D:/proyecto/Vero2.0/core/TEST_DE_VERDAD.txt"

try:
    with open(ruta, "w") as f:
        f.write("✅ Conexión real comprobada. Archivo generado automáticamente desde el servidor.")
    print("✔ Archivo creado correctamente:", ruta)
except Exception as e:
    print("❌ Error creando el archivo:", e)