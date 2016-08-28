from django import forms

class FunctionForm(forms.Form):
    language_id = forms.DecimalField(label = 'Language')
    function_title = forms.CharField(label = 'Function', max_length = 50)
    function_body = forms.CharField(widget = forms.Textarea, label = 'Body', max_length = 200)