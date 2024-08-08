Permite importar la lista de productos, precios, SKU, imágenes, del archivo CSV de wordpress y pegarlo en el archivo de carga masiva de fallabela.

Algunos datos de la tabla son constantes y se puede modificar posteriormente desde el seller center, o en el archivo de excel una vez se encuentre relleno con los datos importados al ejecutar el código.
 
Descargar archivo de productos CSV de wordpress.

    Productos --> exportar -->  generar CSV
    
![image](https://github.com/user-attachments/assets/b30e141d-3c12-4317-8f92-22160d90af7b)


Descargar una pantilla de una categoría genérica desde el seller center de Falabella, ejemplo: 

Productos --> Carga Masiva

Categoría genérica:
2779 - Electrónica / Computación / Componentes informáticos / Otros componentes informáticos


![image](https://github.com/user-attachments/assets/d0165b15-2936-4748-96d0-3cfc566666fd)


La plantilla viene como un archivo de EXCEL.

Ejecutar el código python:

  1. Escoger el archivo CSV descargado de wordpress con la lista de productos.
  2. Escoger el archivo de excel del Seller Center.

El los datos esenciales de la tabla EXCEL se rellenarán con la información proveniente de la tabla CSV.

El texto en la columna descripción aprece con el simbolo de salto de linea "\n", se puede eliminar desde excel con funcion buscar y reemplazar.

Se debe rellenar la columna de categoría del producto manualmente.



