from django.urls import path
from rest_framework import routers
from .api import ReportViewSet
from .views import SetSatus, SVGtoPdfImagesView,  CertificatePDFView, SetStatusReject

router = routers.DefaultRouter()

router.register(r'api/reporttankmovil', ReportViewSet, 'reporttankmovil')

urlpatterns = [
     path(r'api/reportmovilreject/<int:id_report>/',
         SetStatusReject.as_view(), name='SetStatusReject'),
     path(r'api/pdfcreatereportemovil/<int:id_report>/',
         SVGtoPdfImagesView.as_view(), name='ReporteImagenesPDF'),
     path(r'api/pdfcreatecertificatemovil/<int:id_report>/',
         CertificatePDFView.as_view(), name='CertificadosPDF'),
     path(r'api/reportmovilaprobe/<int:report_id>/',
         SetSatus.as_view(), name='AprobarReporte'),
    *router.urls
]