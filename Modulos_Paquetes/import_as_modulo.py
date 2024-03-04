#Podemos importar usan un alias, que es darle otro nombre al modulo
#si decidimos usar el as, es de obligado cunplimiento
# import MODULO as ALIAS
import mi_modulo as modulillo

#una vez lo tenemos se accede igual que con el modulo pero con el alias
modulillo.saludar()

#Y si intentamos acceder por el nombre del modulo tendremos un error
mi_modulo.saludar()