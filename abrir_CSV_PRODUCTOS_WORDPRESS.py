import pandas as pd
import tkinter as tk
from tkinter import filedialog

def cargar_csv():
    # Crear una ventana oculta de Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abre un cuadro de diálogo para seleccionar el archivo CSV
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if file_path:
        # Cargar el archivo CSV en un DataFrame de pandas
        df = pd.read_csv(file_path)
        print("Archivo CSV cargado correctamente\n")
        print("Los encabezados detectados son los siguientes:\n")
        print(df.columns)
        print("\nVoy a imprimir la tabla:\n")
        print(df)
        print("\nEl tamaño del dataframe es: " + str(len(df))+" filas")
        return df
    else:
        print("No se seleccionó ningún archivo\n")
        return None

def cargar_excel(skip_rows=3,sheet_name="Subir plantilla"):
    # Crear una ventana oculta de Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abre un cuadro de diálogo para seleccionar el archivo Excel
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    
    if file_path:
        # Cargar el archivo Excel en un DataFrame de pandas, saltando las primeras filas
        df = pd.read_excel(file_path, skiprows=skip_rows,sheet_name=sheet_name)
        print("Archivo Excel cargado correctamente\n")
        print("Los encabezados detectados son los siguientes:\n")
        print(df.columns)
        print("\nVoy a imprimir la tabla:\n")
        print(df)
        return df, file_path
    else:
        print("No se seleccionó ningún archivo\n")
        return None, None
    
def ajustar_tamano_dataframe(df_origen, df_destino):
    # Verificar si el DataFrame de destino necesita más filas
    if len(df_destino) < len(df_origen):
        # Añadir filas vacías al DataFrame de destino
        num_filas_a_anadir = len(df_origen) - len(df_destino)
        filas_vacias = pd.DataFrame(index=range(num_filas_a_anadir), columns=df_destino.columns)
        df_destino = pd.concat([df_destino, filas_vacias], ignore_index=True)
    return df_destino

def crear_dataframe_imagenes(df_csv):
    print("Voy a crear un dataframe con las direcciones de las imágenes:\n")
    df_separado = df_csv['Imágenes'].str.split(', ', expand=True)
    df_separado.columns = ['Imagen1','Imagen2','Imagen3','Imagen4','Imagen5','Imagen6','Imagen7','Imagen8','Imagen9','Imagen10','Imagen11','Imagen12','imagen13']
    print (df_separado)
    return df_separado   

    
# Cargar el archivo CSV
df_csv = cargar_csv()

# Cargar el dataframe de imágenes
df_imagenes = crear_dataframe_imagenes(df_csv)

# Cargar el archivo Excel
df_excel, excel_path = cargar_excel(skip_rows=3)


if df_excel is not None:
    df_excel=ajustar_tamano_dataframe(df_csv, df_excel)
    # Rellenar toda la columna 'columna2' con el texto 'valor_fijo'
    df_excel['Nombre #39'] = df_csv['Nombre']
    df_excel['Marca #26'] = "GENERICO"
    df_excel['Descripción #53'] = df_csv['Descripción']
    #df_excel['Categoría primaria #1'] =
    #df_excel[ 'Código de barras #56'] = 
    df_excel['Variación #1700'] = '...'
    df_excel['TaxPercentage #2725'] = 0

    df_excel['Ancho del paquete #60']=10
    df_excel['Largo del paquete #33']=10
    df_excel['Alto del paquete #47']=10
    df_excel['Peso del paquete #8']=1

    df_excel['PriceFalabella #52']=df_csv['Precio normal']
    df_excel['SalePriceFalabella #18']=""

    df_excel['QuantityFalabella #25']= 1

    df_excel['Dimensiones #1619']= "10 cm x 10 cm x 10 cm"
    df_excel['Condición del Producto #22']= "Nuevo"

    df_excel['Imagen principal #IM1']= df_imagenes['Imagen1']
    df_excel['Imagen2 #IM2']= df_imagenes['Imagen2']
    df_excel['Imagen3 #IM3']= df_imagenes['Imagen3']
    df_excel['Imagen4 #IM4']= df_imagenes['Imagen4']
    df_excel['Imagen5 #IM5']= df_imagenes['Imagen5']
    df_excel['Imagen6 #IM6']= df_imagenes['Imagen6']
    df_excel['Imagen7 #IM7']= df_imagenes['Imagen7']
    df_excel['Imagen8 #IM8']= df_imagenes['Imagen8']
    

with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
        df_excel.to_excel(writer, index=False, startrow=5, sheet_name="Subir plantilla",header=False)
print("Archivo Excel modificado y guardado correctamente.")

    

   