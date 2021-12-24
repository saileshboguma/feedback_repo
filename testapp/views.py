from django.shortcuts import render
from  . import forms

# Create your views here.
def thankyouview(request):
    return render(request,'testapphtml/thankyou.html')

def feedbackview(request):
    if request.method=='GET':
        form=forms.FeedBackForm()


    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and displaying feedback Information:')
            print('Student Name:',form.cleaned_data['name'])
            print('Student RollNo:',form.cleaned_data['rollno'])
            print('Student Mail Id:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
    return render(request,'testapphtml/feedback.html',{'form':form})

            # return render(request,'testapphtml/thankyou.html',{'name':form.cleaned_data['name']})
