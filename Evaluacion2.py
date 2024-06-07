import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sql
import pandas as pd


data = sql.connect('db_personas.db')
cursor = data.cursor()  
comandoon = '''
Select p.rut, p.nombre_completo, p.nacionalidad, s.Rol, s.Sueldo
FROM personas p
INNER JOIN Salarios s 
ON p.id_rol = s.id_salarios
'''
cursor.execute(comandoon)
data = cursor.fetchall()  
columnas = [i[0] for i in cursor.description]
df = pd.DataFrame(data, columns=columnas)

print (df)