print('Bienvenido, este es un cuestionario para conocer si su VLAN corresponde a una VLAN de rango extendido o normal')
try:
    vlan = int((input('Ingrese el numero de la VLAN que desea consultar: ')))
    if 1 <= vlan <= 1005:
        print('La VLAN '+str(vlan)+' pertenece al rango NORMAL (1-1005)')
    elif 1006 <= vlan <= 4094:
        print('La VLAN '+str(vlan)+' pertenece al rango EXTENDIDO (1006-4094)')
    else:
            print('La VLAN '+str(vlan)+' está fuera de los rangos estándar')
except ValueError:
   print('Error: Debe ingresar un número entero válido')