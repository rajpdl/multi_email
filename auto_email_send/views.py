from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
import io
import xlrd
from django.contrib import messages

def compose(request):
    if(request.method == 'POST'):
        subject = request.POST['subject']
        body = request.POST['body']
        xls = request.FILES['xls']
        xls = xls.read()

        workbook = xlrd.open_workbook(file_contents=xls)

        worksheet = workbook.sheet_by_index(0)

        emailList = []

        #loop through the list of sheet

        for i in range(worksheet.nrows):
            for j in range(worksheet.ncols):
                if worksheet.cell_value(i, j) == 'Email':
                    i = 1
                    while i < worksheet.nrows:
                        emailList.append(worksheet.cell_value(i, j))
                        i += 1
                    

        print(emailList)
        
        #send the email

        send_mail(
        subject,
        body,
        'rajamucsmdy@gmail.com',
        emailList,
        fail_silently=False,
        )

        messages.info(request, 'Email is sent...')

        return redirect('compose')
    
    return render(request, 'compose.html')

@csrf_exempt

def ajax(request):
    name = request.POST['name']
    gender = request.POST['gender']
    
    person = {
        'name': name,
        'gender': gender
    }  

    return HttpResponse(json.dumps(person), content_type='application/json')


