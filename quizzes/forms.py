from django import forms

from .models import Answer, Question


class AdminQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


    def clean(self):

        
        return super().clean()


class AdminAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'

    
    def clean(self):

        return super().clean()


class AnswerInlineFormSet(forms.models.BaseInlineFormSet):

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
            raise forms.ValidationError('At least two answers variants required.')
        elif correct == 0:
            raise forms.ValidationError('At least 1 correct answer required.')
        elif correct == valid:
            raise forms.ValidationError('At least 1 wrong answer required')