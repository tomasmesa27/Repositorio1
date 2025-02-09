nombres = ['Ana','Luis','Carlos','María']
edades = (25,30,22,28)
ciudades = {'Madrid','Barcelona','Sevilla'}
calificaciones = {'Ana':8.5,'Luis':7.0,'Carlos':9.0,'María':6.5}

print(nombres[2])
print(edades[2])

nom_edad1 = nombres[0],edades[0]
nom_edad2 = nombres[1],edades[1]
nom_edad3 = nombres[2],edades[2]
nom_edad4 = nombres[3],edades[3]

consolidado_nom_edad = [nom_edad1,nom_edad2,nom_edad3,nom_edad4]
print(consolidado_nom_edad)

ciudades.add('Valencia')
print(ciudades)

calificacionesnum = list(calificaciones.values())
print(calificacionesnum)

nom_cal1 = nombres[0],calificacionesnum[0]
nom_cal2 = nombres[1],calificacionesnum[1]
nom_cal3 = nombres[2],calificacionesnum[2]

consolidado_nom_cal = [nom_cal1,nom_cal2,nom_cal3]
print(consolidado_nom_cal)