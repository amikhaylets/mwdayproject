from django.db import models

# Create your models here.
class Join(models.Model):
	"""run models app"""
	email = models.EmailField()
	ref_id = models.CharField(max_length=120, default='Default_value', unique=True)
	ip_address = models.CharField(max_length=120, default='Default_value')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return str(self.email)

	class Meta:
		unique_together = ("email", "ref_id",)