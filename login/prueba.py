import bcrypt

password = "mi-contraseña"
stored_hash = "$2b$12$8t4a9541512353257891234567890123456789012345678901234567890123456"

if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")