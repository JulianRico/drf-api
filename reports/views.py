import io
import json
import os
from django.http import FileResponse, HttpResponse
from django.views import View
from reports.report_pdf_movil import GeneratePDFintoSVGMovil
from .report_pdf_estacionario import GeneratePDFintoSVG
from .certificado_pdf import GenerateCertificatePDFintoSVG
from .certificado_pdfMovil import GenerateCertificatePDFintoSVGMovil
from .models import Report
from datetime import datetime
from users.models import User
from companies.models import Companie, UserCompany

import yagmail

from .cumple import Cumple, CumpleDeterioration

import threading


class SVGtoPDFView(View):
    def get(self, request, *args, **kwargs):
        id_from_url = kwargs.get('id_report')

        print(id_from_url)

        try:
            # Consulta el modelo Report usando el ID
            report = Report.objects.get(id=id_from_url)
        except Report.DoesNotExist:
            return HttpResponse("El reporte no existe.")

        # Aquí puedes acceder a los campos del reporte
        # Convierte la cadena de fecha a un objeto datetime
        fecha = report.created_at
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        fechafull = fecha_str.split(" ")
        fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
        fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

        questions_mtto = report.questionsmtto
        question_views = report.questionviews
        questions_deterioration = report.questionsdeterioration
        tank_identification = report.tankidentification
        observations_and_results = report.observationsandresults
        signatures = report.signatures
        photos = report.photos

        try:
            # Consulta el modelo Report usando el ID
            user = User.objects.get(name=report.user)
        except User.DoesNotExist:
            return HttpResponse("El usuario no existe.")
        print(user.email)

        try:
            # Consulta el modelo Report usando el ID
            companie = Companie.objects.get(name=report.companie)
        except Companie.DoesNotExist:
            return HttpResponse("la compañia no existe.")
        print(companie.email)

        try:
            # Consulta el modelo Report usando el ID
            companieuser = UserCompany.objects.get(usuario=report.userCompany)
        except UserCompany.DoesNotExist:
            return HttpResponse("El usuario de compañia no existe.")
        print(companieuser)


        # revisa si cumple en todo
        cumple_instance_identification = Cumple(tank_identification)
        
        cumple_instance_identification.buscar_cumple_principal()        
        cumple_instance_identification.buscar_cumple(cumple_instance_identification.datos)        
        cumpleidentification = cumple_instance_identification.BuscarFalse()

        

        cumple_objDeterioration = CumpleDeterioration()
        resultadoDetarioration = cumple_objDeterioration.buscar_cumple_principal(questions_deterioration)
        


        cumple_objViews = CumpleDeterioration()
        resultadoViews = cumple_objViews.buscar_cumple_principal(question_views)
        
    
        cumple_objObservations = CumpleDeterioration()
        resultadoObservations = cumple_objObservations.buscar_cumple_principal(observations_and_results)
        

        CumpleCertificado: bool; 
        if resultadoObservations and resultadoViews and resultadoDetarioration and cumpleidentification:
            print("todos cumple")
            CumpleCertificado = True;
        else:
            print("no cumple")  
            CumpleCertificado = False;
        print(CumpleCertificado);

        # Pasa los campos a la función GeneratePDFintoSVG
        svg_code = GeneratePDFintoSVG(
            questions_mtto, question_views, questions_deterioration, tank_identification,
            observations_and_results, signatures, photos, fecha_convertida, companieuser, companie, user, id_from_url,CumpleCertificado
        )

        pdf_buffer = self.convert_svg_to_pdf(svg_code)

        # Envía el PDF por correo electrónico
        # self.send_email_with_attachment(id_from_url, companie.name,
        #           companie.email, companieuser.emailContact, user.email, fecha_convertida)
        response = HttpResponse(
            pdf_buffer["bufer"], content_type='application/pdf')
        # response = FileResponse(open(pdf_buffer, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="ReporteQ-Checker_{id_from_url}.pdf"'

        os.remove(pdf_buffer["path"])
        return response
   
# Create your views here.
class SetSatus(View):
    def get(self, request, *args, **kwargs):
        try:
            report_id = kwargs.get('report_id')
            print(report_id)
            new_status = 3
            report = Report.objects.get(pk=report_id)
            print(report.status)
            report.status = new_status
            report.save()

            fecha = report.created_at
            fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
            fechafull = fecha_str.split(" ")
            fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
            fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

            try:
                # Consulta el modelo Report usando el ID
                user = User.objects.get(name=report.user)
            except User.DoesNotExist:
                return HttpResponse("El usuario no existe.")
            print(user.email)

            try:
                # Consulta el modelo Report usando el ID
                companie = Companie.objects.get(name=report.companie)
            except Companie.DoesNotExist:
                return HttpResponse("la compañia no existe.")
            print(companie.email)

            try:
                # Consulta el modelo Report usando el ID
                companieuser = UserCompany.objects.get(
                    usuario=report.userCompany)
            except UserCompany.DoesNotExist:
                return HttpResponse("El usuario de compañia no existe.")
            print(companieuser)

            self.send_email_with_attachment(
                report_id, fecha_convertida, companie.email, user.email, companieuser.emailContact, companie.name)
            return HttpResponse(f"Reporte aprobado {report_id}.")
        except Report.DoesNotExist:
            return HttpResponse(f"El reporte {report_id} no Existe.")

    def send_email_with_attachment(self, id, fecha, correoempresa, correousuario, correousuarioempresa, namecompanie):

        # Reemplaza con la URL real
        
        url_descargarCertificado = f'https://api-qc-drf.onrender.com/api/pdfcreatecertificate/{id}'

        url_descargarReporte = f'https://api-qc-drf.onrender.com/api/pdfcreateimages/{id}'

        user = "testqchecker@gmail.com"
        codeApp = "rflahrjtjqzbdumr"
        subject = 'Entrega de Reporte Q-Checker S.A.S [Aprobado]'        
        to = [correoempresa, correousuario, correousuarioempresa]
        # Genera el contenido HTML directamente en el código
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte Q-Checker S.A.S</title>
    </head>
    <body>
        <p>Estimado(a) {namecompanie},</p>        
        <p>Por favor, descarga el Reporte y certificado {id} : {fecha}</p>

        <div style="margin-top: 20px;">            
            <a href="{url_descargarCertificado}" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Descargar Certificado</a> <br/>
             <a href="{url_descargarReporte}" style="background-color: #9404db; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Descargar Reporte</a>
        </div>

        <p>Mensaje enviado por el sistema de reportes.</p>
        <p>No contestar este mensaje,</p>
        <p>Estamos comprometidos con el medio Ambiente, por favor no imprimir este documento si no es necesario, Politica de Cero Papel - Q-Checker S.A.S</p>        
    </body>
    </html>
    """

        # Elimina las etiquetas HTML para el contenido de texto
        # text_content = strip_tags(html_content)

        with yagmail.SMTP(user, codeApp) as yag:
            yag.send(to, subject, html_content)

        # se borrar el archivo pdf

class SetStatusReject(View):
    def get(self, request, *args, **kwargs):
        try:   
           
            report_id = kwargs.get('id_report')
            print(report_id)
            new_status = 2
            report = Report.objects.get(pk=report_id)
           
            report.status = new_status
            report.save()

            fecha = report.created_at
            fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
            fechafull = fecha_str.split(" ")
            fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
            fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

            try:
                # Consulta el modelo Report usando el ID
                user = User.objects.get(name=report.user)
            except User.DoesNotExist:
                return HttpResponse("El usuario no existe.")
            print(user.email)

            try:
                # Consulta el modelo Report usando el ID
                companie = Companie.objects.get(name=report.companie)
            except Companie.DoesNotExist:
                return HttpResponse("la compañia no existe.")
            print(companie.email)

            try:
                # Consulta el modelo Report usando el ID
                companieuser = UserCompany.objects.get(
                    usuario=report.userCompany)
            except UserCompany.DoesNotExist:
                return HttpResponse("El usuario de compañia no existe.")
            print(companieuser)

            self.send_email_with_attachment(
                report_id, fecha_convertida, companie.email, user.email, companieuser.emailContact, companie.name)
            return HttpResponse(f"Reporte rechazado {report_id}.")
        except Report.DoesNotExist:
            return HttpResponse(f"El reporte {report_id} no Existe.")

    def send_email_with_attachment(self, id, fecha, correoempresa, correousuario, correousuarioempresa, namecompanie):

        # Reemplaza con la URL real       

        url_descargarReporte = f'https://api-qc-drf.onrender.com/api/pdfcreateimages/{id}'

        user = "testqchecker@gmail.com"
        codeApp = "rflahrjtjqzbdumr"
        subject = 'Entrega de Reporte Q-Checker S.A.S [Rechazado]'        
        to = [correoempresa, correousuario, correousuarioempresa]
        # Genera el contenido HTML directamente en el código
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte Q-Checker S.A.S</title>
    </head>
    <body>
        <p>Estimado(a) {namecompanie},</p>        
        <p>Por favor, descarga el Reporte {id} : {fecha}</p>

        <div style="margin-top: 20px;">            
            <a href="{ url_descargarReporte}" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Descargar</a>
        </div>

        <p>Mensaje enviado por el sistema de reportes.</p>
        <p>No contestar este mensaje,</p>
        <p>Estamos comprometidos con el medio Ambiente, por favor no imprimir este documento si no es necesario, Politica de Cero Papel - Q-Checker S.A.S</p>        
    </body>
    </html>
    """

        # Elimina las etiquetas HTML para el contenido de texto
        # text_content = strip_tags(html_content)

        with yagmail.SMTP(user, codeApp) as yag:
            yag.send(to, subject, html_content)

        # se borrar el archivo pdf


class  SVGtoPdfImagesView(View):
    def get(self, request, *args, **kwargs):
        id_from_url = kwargs.get('id_report')
        
        try:
            # Consulta el modelo Report usando el ID
            report = Report.objects.get(id=id_from_url)
        except Report.DoesNotExist:
            return HttpResponse("El reporte no existe.")

        # Aquí puedes acceder a los campos del reporte
        # Convierte la cadena de fecha a un objeto datetime
        fecha = report.created_at
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        fechafull = fecha_str.split(" ")
        fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
        fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

        questions_mtto = report.questionsmtto
        question_views = report.questionviews
        questions_deterioration = report.questionsdeterioration
        tank_identification = report.tankidentification
        observations_and_results = report.observationsandresults
        signatures = report.signatures
        photos = report.photos
        
        
        company = []

        try:
            # Consulta el modelo Report usando el ID
            user = User.objects.get(name=report.user)
           
            company.append(user.name)
        except User.DoesNotExist:
            return HttpResponse("El usuario no existe.")
        

        try:
            # Consulta el modelo Report usando el ID
            companies = Companie.objects.get(name=report.companie)            
            company.append(companies.name)
            company.append(companies.nit)
        except Companie.DoesNotExist:
            return HttpResponse("la compañia no existe.")
        

        try:
            # Consulta el modelo Report usando el ID
            companieuser = UserCompany.objects.get(usuario=report.userCompany)
            company.append(companieuser.phone)
            company.append(companieuser.address)
            company.append(companieuser.usuario)
            company.append(companieuser.contact)
        except UserCompany.DoesNotExist:
            return HttpResponse("El usuario de compañia no existe.")
       

        # revisa si cumple en todo    

        # revisa si cumple en todo
        cumple_instance_identification = Cumple(tank_identification)
        cumple_instance_identification.buscar_cumple_principal()        
        cumple_instance_identification.buscar_cumple(cumple_instance_identification.datos)
        cumpleidentification = cumple_instance_identification.BuscarFalse()

        cumple_objDeterioration = CumpleDeterioration()
        resultadoDetarioration = cumple_objDeterioration.buscar_cumple_principal(questions_deterioration) 

        cumple_objViews = CumpleDeterioration()
        resultadoViews = cumple_objViews.buscar_cumple_principal(question_views)

        cumple_objObservations = CumpleDeterioration()
        resultadoObservations = cumple_objObservations.buscar_cumple_principal(observations_and_results)        

        CumpleCertificado: bool;



        if resultadoObservations and resultadoViews and resultadoDetarioration and cumpleidentification:
            print("todos cumple")
            CumpleCertificado = True;
        else:
            print("no cumple")  
            CumpleCertificado = False;
        print(CumpleCertificado);

        
        print(companieuser)

        tank_format = json.loads(tank_identification)
            

        if 'formato' in tank_format and tank_format['formato'] == "Movil":
                print('ingreso movil')
                
                print(' ')
                
                pdf_movil = GeneratePDFintoSVGMovil(
                questions_mtto, question_views, questions_deterioration, tank_identification,
                observations_and_results, signatures, photos, fecha_convertida,company, id_from_url,CumpleCertificado)

                def eliminar_archivo(ruta):
                    os.remove(ruta)   

                if pdf_movil['path']:
                    temporizador = threading.Timer(5, eliminar_archivo, args=[pdf_movil['path']])
                    temporizador.start()
                # Crear una respuesta de descarga con el archivo PDF
                
                return  pdf_movil['response']
               
        else:
            print('ingreso fijo')   

            
        # Pasa los campos a la función GeneratePDFintoSVG
            pdf_output = GeneratePDFintoSVG(
                questions_mtto, question_views, questions_deterioration, tank_identification,
                observations_and_results, signatures, photos, fecha_convertida,company, id_from_url,CumpleCertificado)

           
        # Envía el PDF por correo electrónico
        # self.send_email_with_attachment(id_from_url, companie.name,
        #           companie.email, companieuser.emailContact, user.email, fecha_convertida)
            def eliminar_archivo(ruta):
                os.remove(ruta)                
            if pdf_output['path']:
                temporizador = threading.Timer(5, eliminar_archivo, args=[pdf_output['path']])
                temporizador.start()
            # Crear una respuesta de descarga con el archivo PDF
            
            return  pdf_output['response']      
        

  
class CertificatePDFView(View):
    def get(self, request, *args, **kwargs):
        id_from_url = kwargs.get('id_report')       

        try:
            # Consulta el modelo Report usando el ID
            report = Report.objects.get(id=id_from_url)
        except Report.DoesNotExist:
            return HttpResponse("El reporte no existe.")

        # Aquí puedes acceder a los campos del reporte
        # Convierte la cadena de fecha a un objeto datetime
        fecha = report.created_at
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        fechafull = fecha_str.split(" ")
        fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
        fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

        questions_mtto = report.questionsmtto
        question_views = report.questionviews
        questions_deterioration = report.questionsdeterioration
        tank_identification = report.tankidentification
        observations_and_results = report.observationsandresults
        

        company = []

        try:
            # Consulta el modelo Report usando el ID
            user = User.objects.get(name=report.user)
           
            company.append(user.name)
        except User.DoesNotExist:
            return HttpResponse("El usuario no existe.")
        

        try:
            # Consulta el modelo Report usando el ID
            companies = Companie.objects.get(name=report.companie)            
            company.append(companies.name)
            company.append(companies.nit)
            company.append(companies.city)
            company.append(companies.address)
        except Companie.DoesNotExist:
            return HttpResponse("la compañia no existe.")
        

        try:
            # Consulta el modelo Report usando el ID
            companieuser = UserCompany.objects.get(usuario=report.userCompany)
            company.append(companieuser.phone)
            company.append(companieuser.address)
            company.append(companieuser.usuario)
            company.append(companieuser.contact)
        except UserCompany.DoesNotExist:
            return HttpResponse("El usuario de compañia no existe.")   

        #agrgar la validaciones
        # revisa si cumple en todo
        cumple_instance_identification = Cumple(tank_identification)
        cumple_instance_identification.buscar_cumple_principal()        
        cumple_instance_identification.buscar_cumple(cumple_instance_identification.datos)
        cumpleidentification = cumple_instance_identification.BuscarFalse()
        print("cumple identificacion")
        print(cumpleidentification)

        
        cumple_objDeterioration = CumpleDeterioration()
        resultadoDetarioration = cumple_objDeterioration.buscar_cumple_principal(questions_deterioration)
        print("cumple deterioration")
        print(resultadoDetarioration)


        cumple_objViews = CumpleDeterioration()
        resultadoViews = cumple_objViews.buscar_cumple_principal(question_views)
        print("cumple views")
        print(resultadoViews)
    
        cumple_objObservations = CumpleDeterioration()
        resultadoObservations = cumple_objObservations.buscar_cumple_principal(observations_and_results)
        print("cumple Observationsandresults")
        print(resultadoObservations)

        CumpleCertificado: bool; 
        if resultadoObservations and resultadoViews and resultadoDetarioration and cumpleidentification:
            print("todos cumple")
            CumpleCertificado = True;
        else:
            print("no cumple")  
            CumpleCertificado = False; 
           
            #return HttpResponse(error_message)             
        
        tank_format = json.loads(tank_identification)
            

        if 'formato' in tank_format and tank_format['formato'] == "Movil":

            certificado = GenerateCertificatePDFintoSVGMovil(
                questions_mtto, question_views, questions_deterioration, tank_identification,
                observations_and_results, fecha_convertida,  company,  id_from_url, CumpleCertificado)
            
            def eliminar_archivo(ruta):
                os.remove(ruta)   

            if certificado['path']:
                temporizador = threading.Timer(5, eliminar_archivo, args=[certificado['path']])
                temporizador.start()
                    # Crear una respuesta de descarga con el archivo PDF
                    
            return  certificado['response']
            
        else:
            certificado = GenerateCertificatePDFintoSVG(
                questions_mtto, question_views, questions_deterioration, tank_identification,
                observations_and_results, fecha_convertida,  company,  id_from_url, CumpleCertificado)

            def eliminar_archivo(ruta):
                os.remove(ruta)   

            if certificado['path']:
                temporizador = threading.Timer(5, eliminar_archivo, args=[certificado['path']])
                temporizador.start()
                    # Crear una respuesta de descarga con el archivo PDF
                    
            return  certificado['response']  

    

