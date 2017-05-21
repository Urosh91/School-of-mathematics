from django import forms


def must_be_empty(value):
    if value:
        raise forms.ValidationError('should be left empty!')


class SuggestionForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify your email')
    suggestion = forms.CharField(widget=forms.Textarea)
    validate = forms.CharField(required=False, widget=forms.HiddenInput,
                               label='Leave empty', validators=[must_be_empty])

    def clean(self):
        cleaned_date = super().clean()
        email = cleaned_date['email']
        verify_email = cleaned_date['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Your emails did not match')