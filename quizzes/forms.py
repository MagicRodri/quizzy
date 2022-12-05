from django import forms

from .models import Answer, Option, Question


class AdminQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


    def clean(self):

        
        return super().clean()


class AdminOptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = '__all__'

    
    def clean(self):

        return super().clean()


class OptionInlineFormSet(forms.models.BaseInlineFormSet):

    def clean(self) -> None:
        super().clean()

        valid = 0
        correct = 0
        for cleaned_data in self.cleaned_data:
            # Use only valid form not being deleted
            if cleaned_data and not cleaned_data.get('DELETE',False):
                valid += 1
                if cleaned_data.get('correct'):
                    correct += 1
        if valid < 2:
            raise forms.ValidationError('At least two Options variants required.')
        elif correct == 0:
            raise forms.ValidationError('At least 1 correct Option required.')
        elif correct == valid:
            raise forms.ValidationError('At least 1 wrong Option required')


class AnswerForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        print(kwargs)

        # grab initial question in order to limit options choices, initial set before first form rendering
        question = kwargs.get('initial').get('question')
        if question:
            self.fields['options'].queryset = Option.objects.filter(question=question)

    class Meta:
        model = Answer
        fields = ['options']
        widgets = {
            'options':forms.CheckboxSelectMultiple()
        }