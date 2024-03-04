#PAra usar un paquete debemos importarlo
#para ello tenemos la sentencia import NOMBRE_PAQUETE
#El nombre del paquete es igual al nombre del fichero
import mi_paquete

#Puedo acceder a los elementos que estan dentro
# NOMBRE_PAQUETE.FUNCiON/OBJETO/VARIABLE
mi_paquete.saludar()

print(mi_paquete.variable)

#La docstring
print(mi_paquete.__doc__)