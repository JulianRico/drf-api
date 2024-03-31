from rest_framework import serializers
from .models import ReportTankMovil
from users.models import User
from companies.models import Companie, UserCompany
import yagmail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)


class CompanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companie
        fields = ('name',)


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('usuario',)


class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    companie = CompanieSerializer()
    status_display = serializers.SerializerMethodField()
    userCompany = UserCompanySerializer()

    class Meta:
        model = ReportTankMovil
        fields = ('id', 'status_display', 'status', 'questionsmtto', 'questionviews', 'tankidentification', 'observationsandresults', 'signatures',
                  'questionsdeterioration', 'photos', 'user', 'companie', 'userCompany', 'created_at')
        read_only_fields = ( 'id', 'created_at',)

    def get_status_display(self, obj):
        return dict(ReportTankMovil.SelfStatus).get(obj.status)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        companie_data = validated_data.pop('companie')
        user_company_data = validated_data.pop('userCompany')

        user, _ = User.objects.get_or_create(**user_data)
        companie, _ = Companie.objects.get_or_create(**companie_data)
        user_company, _ = UserCompany.objects.get_or_create(
            **user_company_data)

        report = ReportTankMovil.objects.create(
            user=user,
            companie=companie,
            userCompany=user_company,
            **validated_data
        )

        self.send_email(report.id, user.email)
        return report

    def send_email(self, id, userEmail):
        user = "testqchecker@gmail.com"
        codeApp = "rflahrjtjqzbdumr"
        # Reemplaza con la URL real
        url_revisar = f'http://198.50.156.11:8000/api/pdfcreatereportemovil/{id}'
        # Reemplaza con la URL real
        url_aprobar = f'http://198.50.156.11:8000/api/reportmovilaprobe/{id}'

        url_rechazar = f'http://198.50.156.11:8000/api/reportmovilreject/{id}'

        subject = f'Informe para su revisión y aprobación [Quality Control - No.{id} ]'
        to = ['juliquinterorico@hotmail.com',
               "jhonfredyquintero@gmail.com", userEmail]
        # Genera el contenido HTML directamente en el código
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Informe para Revisión y Aprobación [Quality Control -  Generado]</title>
    </head>
    <body>
        <p>Estimado(a) destinatario,</p>
        <p>Adjunto encontrarás un informe que requiere tu revisión y aprobación.</p>
        <p>Por favor, toma un momento para revisar el informe {id} y realizar la acción correspondiente:</p>

        <div style="margin-top: 20px;">
            <a href="{url_revisar}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;">Revisar</a>
            <a href="{url_aprobar}" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Aprobar</a>
            <a href="{url_rechazar}" style="background-color: #d10d2d; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Rechazar</a>
           
        </div>

        <p>Mensaje enviado por el sistema de reportes.</p>
        <p>No contestar este mensaje,</p>        
    </body>
    </html>
    """

        with yagmail.SMTP(user, codeApp) as yag:
            yag.send(to, subject, html_content)