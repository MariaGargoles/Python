#!/usr/bin/env python3
import subprocess
from datetime import datetime, timedelta

# Obtener la fecha actual
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Cabecera del fichero IPs_maliciosas.txt
with open('/home/auditoria/IPs_maliciosas.txt', 'w') as f:
    f.write("---------------------------------------------------------------------------------------------------------------------------\n")
    f.write("\n")
    f.write("-------------- IPs maliciosas desde las que se hacen ataques por fuerza bruta contra nuestro sistema tardis. --------------\n")
    f.write("\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------\n")

# Pasar por teclado el número de días atrás que queremos filtrar el journalctl
ndias = input(f"Hola {subprocess.getoutput('echo $USER')}, ¿de cuántos días quieres filtrar el journalctl? ")
ndias = int(ndias)

# Consultar el journalctl y filtrarlo por +invalid user+. El resultado se guarda en el fichero IPs_maliciosas.txt que está en /home/auditoria
journal_output = subprocess.getoutput(f"sudo journalctl -S -{ndias}d | grep 'invalid user'")
with open('/home/auditoria/IPs_maliciosas.txt', 'a') as f:
    for line in journal_output.splitlines():
        parts = line.split()
        if parts[11] != "port":
            f.write(f"Fecha: {parts[0]} {parts[1]}\tHora: {parts[2]}\tIP: {parts[11]}\tPort: {parts[13]}\tNombre: {parts[10]}\n")
        else:
            f.write(f"\tFecha: {parts[0]} {parts[1]}\tHora: {parts[2]}\tIP: {parts[10]}\tPort: {parts[12]}\tNombre: desconocido\n")

# Verificar si el comando se ha ejecutado correctamente
if subprocess.run(["echo", "$?"], capture_output=True).stdout.decode().strip() == "0":
    print("El fichero IPs_maliciosas ha sido creado correctamente")
    # Cambiar los permisos del fichero
    subprocess.run(["sudo", "chmod", "664", "/home/auditoria/IPs_maliciosas.txt"])
    # Cambiar el grupo y el propietario del fichero
    subprocess.run(["sudo", "chown", "seginf_director:auditoria", "/home/auditoria/IPs_maliciosas.txt"])

    # Pie del fichero
    with open('/home/auditoria/IPs_maliciosas.txt', 'a') as f:
        f.write("\n")
        f.write("---------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        f.write(f"Fichero actualizado: {fecha} ----------------------------------------------------------------------------------\n")
        f.write("---------------------------------------------------------------------------------------------------------------------------\n")
else:
    print("El fichero IPs_maliciosas no ha sido creado correctamente")

respuesta = input("¿Quieres mostrar por pantalla el resultado? 's' para aceptar: ")
if respuesta.lower() == "s":
    subprocess.run(["less", "/home/auditoria/IPs_maliciosas.txt"])
