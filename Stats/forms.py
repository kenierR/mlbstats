from django import forms
from Stats.models import Division

div = Division.objects.filter(sport=1)
choise = []
for x in div:
    #mituple = (x.id,x.name)
    choise.append((x.id,x.name))
DEMO_CHOICES = tuple(choise)


class TeamSelectForm(forms.Form):
    name = forms.MultipleChoiceField(choices = DEMO_CHOICES,label='prueba')

