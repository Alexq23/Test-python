from django import forms
from .models import Quote, Source

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'source', 'weight']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите цитату...'}),
        }

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if Quote.objects.filter(text__iexact=text).exists():
            raise forms.ValidationError("Цитата уже существует!")
        return text

    def clean_source(self):
        source = self.cleaned_data['source']
        if source.quotes.count() >= 3:
            raise forms.ValidationError(f"У источника '{source.name}' уже 3 цитаты. Нельзя добавить больше.")
        return source