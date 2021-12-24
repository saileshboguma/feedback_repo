from django import forms
from django.core import validators
#recommended to use validators

# Create your forms here.
#I AM IMPLEMENTING MY OWN validators
# def starts_with_s(value):
#     if value[0].lower() !='s':
#         raise forms.ValidationError('Name should be starts with s')
#     #In the above written code..now you just specify the function name in the CharField
#
# def only_alphabets(value):
#     if value.isalpha() != True:
#         raise forms.ValidationError('Name should contains only alphabets symbols')
#
# def gmail_verification(value):
#     if value[len(value)-9:] != 'gmail.com':
#         raise forms.ValidationError('Must be gmail.com')


class FeedBackForm(forms.Form):
    # name=forms.CharField(validators=[starts_with_s,only_alphabets])
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Reenter Passwords', widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    
    #email=forms.EmailField(validators=[gmail_verification])

    #feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(20)])
    #Validation of Total Form directly by using a Single Clean Method:
    def clean(self):
        print('Total Form Validation...')
        print('BOT VALIDATION....')
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']

        inputname=cleaned_data['name']
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']

        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks BOT..!!!')

        if len(inputname) <10:
            raise forms.ValidationError('Name should compulsory contains minimum 10 character')

        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('Rollno should complusory contains 3 digits')

        if inputpwd != inputrpwd:
            raise forms.ValidationError('Passwords not matched')

    # I want to implement my own Validations:
    # Explicitly by the Programmer by using Clean Methods:
    # Form validation by using clean methods is not recommended.

    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     print('validating name field')
    #     if len(inputname)<4:
    #         raise forms.ValidationError('The minimum length of the name field should be >=4')
    #     return inputname
    #
    # def clean_rollno(self):
    #     inputrollno=self.cleaned_data['rollno']
    #     print('validating rollno field')
    #     return inputrollno
    #
    # def clean_email(self):
    #     inputemail=self.cleaned_data['email']
    #     print('validating email field')
    #     return inputemail
    #
    # def clean_feedback(self):
    #     inputfeedback=self.cleaned_data['feedback']
    #     print('validating feedback field')
    #     return inputfeedback
