import json
import requests
import base64
from io import BytesIO
from reportlab.platypus import Image


import qrcode
from qrcode.image import svg



def GenerateCertificatePDFintoSVGMovil(questions_mtto, question_views, questions_deterioration, tank_identification,
                       observations_and_results,  fecha_convertida, companieuser, companie, user, id, aprobado,JSONsignatures):
   # Crear un objeto BytesIO para guardar la imagen en memoria
   JSONquestions_mtto = json.loads(questions_mtto)
   JSONquestion_views = json.loads(question_views)
   JSONquestions_deterioration = json.loads(questions_deterioration)
   JSONtank_identification = json.loads(tank_identification)
   JSONobservations_and_results =    json.loads(observations_and_results)
   qr = qrcode.QRCode(
      version=1,  # Tamaño del código QR (1-40)
      error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H)
      box_size=2,  # Tamaño de los cuadros en el código QR
      border=2,  # Ancho del borde blanco alrededor del código QR
   )
   data = f"http://198.50.156.11:8000/api/pdfcreatecertificate/{id}/"  # Puedes cambiar esto por tu propio enlace o datos
   qr.add_data(data)   
   img = qr.make_image(fill_color="black", back_color="white")
   img.resize((20, 20))   
   # Guardar la imagen en un búfer de bytes
   buffer = BytesIO()
   img.save(buffer)

   # Obtener los datos binarios del código QR en formato SVG
   codigo_qr_svg = buffer.getvalue()
   #guarda la imagen
   imagen_base64 = base64.b64encode(codigo_qr_svg).decode("utf-8")
   
   
   

   def recorridoCumple(data,nombre):
      all_valid = all(value['cumple'] == True for key, value in data.items() if nombre in key)
      return all_valid


   def downloadImage(url):
      response = requests.get(url)
      if response.status_code == 200:
            # Obtener el contenido de la imagen
         image_data = response.content
         image_base64 = base64.b64encode(image_data).decode('utf-8')
         return image_base64
      else:
         print("Error al descargar la imagen:", response.status_code)
         return ("")



#instalar el libreoffice por comando en la maquina
import os

def editar_y_generar_pdf():
    # Leer el archivo Excel
    workbook = openpyxl.load_workbook('/content/certitrans.xlsx')
    print(workbook)
    # Obtener la hoja de trabajo (puedes ajustar esto según tu necesidad)
    hoja = workbook['Hoja1']

    #datos iniciales
    hoja['G10'] = fecha_convertida
    hoja['C11'] = companie
    hoja['f9'] = numerocerti
    hoja['C12'] = nit
    hoja['C13'] = ciudad
    hoja['C17'] = ciudad
    hoja['F12'] = direccion

    #datos vahiculo
    hoja['E16']=JSONquestions_mtto['capacidadNominal']
    hoja['G16']='X'
    hoja['H15']=JSONquestions_mtto['fabricante']
    hoja['F15']=JSONquestions_mtto['numeroSerie']
    hoja['C15']=JSONquestions_mtto['tipoTanque']
    hoja['E17'] = direccion
    hoja['C18'] = JSONquestions_mtto['placa']


    #hermeticidad
    if JSONquestions_mtto['hermeticidad']['cumple']== True:
     hoja['G24'] = 'CUMPLE'
    #soldadura
    if JSONobservations_and_results['soldadura']['cumple']== True:
     hoja['G25'] = 'CUMPLE'
    #abollladura
    if JSONquestions_mtto['abolladura']['cumple']== False:
     hoja['G26'] = 'CUMPLE'
    #hinchamiento
    if JSONquestions_mtto['hinchamiento']['cumple']== False:
     hoja['G27'] = 'CUMPLE'
    #hundimientos
    if JSONquestions_mtto['hendiduras']['cumple']== False:
     hoja['G28'] = 'CUMPLE'
    #corrosion
    if JSONquestions_mtto['corrosion']['cumple']== False:
     hoja['G29'] = 'CUMPLE'
    #tuberia
    if JSONobservations_and_results['corrosion']['cumple']== True & JSONobservations_and_results['fisurasoescape']['cumple']== True &  JSONobservations_and_results['roscas']['cumple']== True &  JSONobservations_and_results['aplastamiento']['cumple']== True:
     hoja['G30'] = 'CUMPLE'
    #valvulas de alivio
    if JSONquestions_mtto['valvulaAlivio']['cumple']== False:
     hoja['G31'] = 'CUMPLE'
    #conexiones
    if JSONtank_identification['EstadoConexionCorrosion']['cumple']== False & JSONtank_identification['EstadoConexionEvidenciaGolpes']['cumple']== False &  JSONtank_identification['EstadoConexionDesgaste']['cumple']== False &  JSONtank_identification['EstadoConexionOtros']['cumple']== False:
     hoja['G32'] = 'CUMPLE'
    else:
     hoja['G32'] = 'NOCUMPLE'


    #fajas
    if JSONquestion_views['fajasapoyo']['cumple']== True & JSONquestion_views['sobresanos']['cumple']== True &  JSONquestion_views['soportes']['cumple']== True:
     hoja['G33'] = 'CUMPLE'
    #tuberia
    if JSONobservations_and_results['soldadura']['cumple']== True & JSONobservations_and_results['corrosion']['cumple']== True &  JSONobservations_and_results['fisurasoescape']['cumple']== True &  JSONobservations_and_results['roscas']['cumple']== True & JSONobservations_and_results['aplastamiento']['cumple']== True:
     hoja['G34'] = 'CUMPLE'



    #firma
    routeLogo =JSONsignatures['logo']

    response = requests.get(routeLogo)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 3.5 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    print(img.width)
    print(img.height)
    hoja.add_image(img, 'D38')  # Agregar la imagen en la celda A1 o en la celda que desees

     #firma
    routeFirmaUsuario =JSONsignatures['firma']

    response = requests.get(routeFirmaUsuario)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 3.5 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    print(img.width)
    print(img.height)
    hoja.add_image(img, 'F38')  # Agregar la imagen en la celda A1 o en la celda que desees





    # Convertir la hoja de cálculo a un DataFrame de pandas
    df = pd.DataFrame(hoja.values, columns=[col[0].value for col in hoja.iter_cols()])

    # Crear un objeto BytesIO para almacenar la salida del archivo PDF
    pdf_output = BytesIO()

    # Crear un objeto PdfPages de matplotlib
    pdf_pages = matplotlib.backends.backend_pdf.PdfPages(pdf_output)

    # Tabular el DataFrame y agregarlo al PDF
    fig, ax = plt.subplots()
    ax.axis('off')  # Desactivar los ejes
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

    pdf_pages.savefig(fig, bbox_inches='tight', pad_inches=0.1)
    pdf_pages.close()

    # Hacer que BytesIO esté listo para ser leído
    pdf_output.seek(0)

    # Hacer algo con el PDF, por ejemplo, ofrecerlo para su descarga
    # En este ejemplo, simplemente imprimiré el contenido del PDF
    pdf_output


    # Guardar el archivo Excel editado en un nuevo archivo
    workbook.save('/content/nuevo_archivo_editado.xlsx')





    #borrar archivo.


# Llamar a la función para editar y generar el PDF en memoria
editar_y_generar_pdf()


# Ruta al archivo Excel de entrada
archivo_excel = '/content/nuevo_archivo_editado.xlsx'

# Ruta al archivo PDF de salida
archivo_pdf = '/content/nuevo_archivo_editado.pdf'


# Convertir el archivo Excel a PDF
#excel_to_pdf(archivo_excel, archivo_pdf)

#eliminarArchivos(archivo_excel, archivo_pdf)


