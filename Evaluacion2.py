import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sql
import pandas as pd
from word_gen import example_contract
from unidecode import unidecode

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

def contrato(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['fecha_ingreso']
    rol = sub_df['id_rol']
    address = sub_df['residencia']
    rut = sub_df['rut']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha_de_nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
    return sub_df

#Definicion del la funcion filtro
def filtro(df: pd.DataFrame):
    click = input("¿Como desea buscar a la persona?: ").strip().lower()
    
    if click == "nombre":
        nombreFiltro = input("Ingrese el nombre de la persona: ").strip().lower()
        nombreSNtilde = unidecode(nombreFiltro)
        df['nombre_completo'] = df['nombre_completo'].apply(lambda x: unidecode(x).lower())
        filtrodf = df[df['nombre_completo'].str.contains(nombreSNtilde, case=False)]
        
        if not filtrodf.empty:
            print(f"Se han encontrado a las siguientes personas con el nombre {nombreFiltro}:")
            print(filtrodf)
            if len(filtrodf) > 1:
                fila_idc = int(input("Ingrese el indice de la fila que desea seleccionar: "))
            else:
                fila_idc = filtrodf.index[0]
            persona_selc = filtrodf.iloc[filtrodf.index.get_loc(fila_idc)]
            print("Datos de la persona seleccionada: ")
            print(persona_selc)
        else:
            print(f"No se han encontrado personas con el nombre {nombreFiltro}")
    
    elif click == "rut":
        rutfiltro = input("Ingrese el rut de la persona: ").strip()
        filtrodf = df[df['rut'] == rutfiltro]
        
        if not filtrodf.empty:
            print(f"Se ha encontrado a la persona con el rut {rutfiltro}:")
            print(filtrodf)
            fila_idc = filtrodf.index[0]
            rut_selc = filtrodf.iloc[filtrodf.index.get_loc(fila_idc)]
            print("Datos de la persona seleccionada: ")
            print(rut_selc)
        else:
            print(f"No se han encontrado personas con el rut {rutfiltro}")
    
    elif click == "nacionalidad":
        nacionalidadFiltro = input("Ingrese la nacionalidad de la persona: ").strip().lower()
        df['nacionalidad'] = df['nacionalidad'].apply(lambda x: unidecode(x).lower())
        filtrodf = df[df['nacionalidad'] == nacionalidadFiltro]
        
        if not filtrodf.empty:
            print(f"Se han encontrado a las personas con la nacionalidad {nacionalidadFiltro}:")
            print(filtrodf)
            if len(filtrodf) > 1:
                fila_idc = int(input("Ingrese el indice de la fila que desea seleccionar: "))
            else:
                fila_idc = filtrodf.index[0]
            nacionalida_selc = filtrodf.iloc[filtrodf.index.get_loc(fila_idc)]
            print("Datos de la persona seleccionada: ")
            print(nacionalida_selc)
        else:
            print(f"No se han encontrado personas con la nacionalidad {nacionalidadFiltro}")
    
    elif click == "rol":
        rolFiltro = input("Ingrese el rol de la persona: ").strip().lower()
        df['Rol'] = df['Rol'].apply(lambda x: unidecode(x).lower())
        filtrodf = df[df['Rol'] == rolFiltro]
        
        if not filtrodf.empty:
            print(f"Se han encontrado a las personas con el rol {rolFiltro}:")
            print(filtrodf)
            if len(filtrodf) > 1:
                fila_idc = int(input("Ingrese el indice de la fila que desea seleccionar: "))
            else:
                fila_idc = filtrodf.index[0]
            rol_selc = filtrodf.iloc[filtrodf.index.get_loc(fila_idc)]
            print("Datos de la persona seleccionada: ")
            print(rol_selc)
        else:
            print(f"No se han encontrado personas con el rol {rolFiltro}")
    
    elif click == "sueldo":
        sueldoFiltro = int(input("Ingrese el sueldo de la persona: "))
        filtrodf = df[df['Sueldo'] == sueldoFiltro]
        
        if not filtrodf.empty:
            print(f"Se ha encontrado a la persona con el sueldo {sueldoFiltro}:")
            print(filtrodf)
            if len(filtrodf) > 1:
                fila_idc = int(input("Ingrese el indice de la fila que desea seleccionar: "))
            else:
                fila_idc = filtrodf.index[0]

            sueldo_selc = filtrodf.iloc[filtrodf.index.get_loc(fila_idc)]
            print("Datos de la persona seleccionada: ")
            print(sueldo_selc)
        else:
            print(f"No se han encontrado personas con el sueldo {sueldoFiltro}")
    else:
        print("Opción no válida")
        filtro(df)

print(filtro(df))