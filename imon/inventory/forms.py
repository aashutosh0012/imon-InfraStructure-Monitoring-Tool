from django import forms
from .models import Server


class AddServerForm(forms.ModelForm):
	class Meta:
		model = Server
		# fields = "__all__"
		# fields = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','slug')) ]
		# fields = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','slug','servermetrics','diskvolumes','cpuusagehistory','cpumemoryusagehistory','database','host_ip')) ]
		fields = [ field.name for field in Server._meta.fields if (field.name not in ('id','slug')) ]
		# exclude
		def __init__(self, *args, **kwargs):
			super(UserColorsForm, self).__init__(*args, **kwargs)
			for field in self.fields: 
				self.fields[field].widget.attrs.update({'class': 'form-control'})
