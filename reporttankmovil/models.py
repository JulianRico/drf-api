from django.db import models
from users.models import User
from companies.models import Companie, UserCompany

# Create your models here.


class ReportTankMovil(models.Model):
    questionsmtto = models.JSONField()
    questionviews = models.JSONField()
    questionsdeterioration = models.JSONField()
    tankidentification = models.JSONField()
    observationsandresults = models.JSONField()
    signatures = models.JSONField()
    photos = models.JSONField(null=True)
    idcerticate = models.CharField(max_length=30, null=True, blank=True)

    SelfStatus = ((1, "Espera"), (2, "Rechazado"), (3, "Aprobado"))
    status = models.IntegerField(choices=SelfStatus, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='reporttankmovil',
                             on_delete=models.CASCADE, blank=True, null=True)
    companie = models.ForeignKey(
        Companie, related_name='reporttankmovil', on_delete=models.CASCADE, blank=True, null=True)

    userCompany = models.ForeignKey(
        UserCompany, related_name='reporttankmovil', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)
