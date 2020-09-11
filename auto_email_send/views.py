from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
import io
import xlrd

def compose(request):
    if(request.method == 'POST'):
        subject = request.POST['subject']
        body = request.POST['body']
        xls = request.FILES['xls']
        xls = xls.read()

        workbook = xlrd.open_workbook(file_contents=xls)

        worksheet = workbook.sheet_by_index(0)

        emailList = []

        for i in range(worksheet.nrows):
            emailList.append(worksheet.cell_value(i, 0))
        
        send_mail(
        subject,
        body,
        'rajamucsmdy@gmail.com',
        emailList,
        fail_silently=False,
        )


        return redirect('compose')
    
    # recepantList = []
    # f = open('demofile.txt', 'rt')
    # for x in f:
    #     recepantList.append(x)
    #     # print(x)
    
    # print(recepantList)
    
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


