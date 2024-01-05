from django import forms

from catalog.models import Product

BAD_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция']


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # use all fields
        # fields = ('name',)  # use only listed fiedls
        # exclude = ('date_last_change',)  # use all except these
        # write only one option

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for bad in BAD_WORDS:
            if bad in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с плохими словами в названии')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for bad in BAD_WORDS:
            if bad in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с плохими словами в названии')

        return cleaned_data

