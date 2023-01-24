from django.shortcuts import render
from django.http import HttpResponse
from . models import alert

def home (request):
    allResult = alert.objects.filter(Type='result').values()
    sortedResult = allResult.order_by('-date_of_issue')
    Result = sortedResult[0:16]
    
    allVacancy = alert.objects.filter(Type='vacancy').values()
    sortedVacancy = allVacancy.order_by('-date_of_issue')
    Vacancy = sortedVacancy[0:16]

    allAdmits = alert.objects.filter(Type='admitcard').values()
    sortedAdmits = allAdmits.order_by('-date_of_issue')
    Admits = sortedAdmits[0:16]

    para = {'result':Result, 'vacancy':Vacancy, 'admitcard':Admits} 
    return render(request, 'base.html', para)

def job (request, slug):
    allLink = alert.objects.filter(Title=slug)
    para = {'Link': allLink[0]}
    return render(request, 'jobbase.html', para)

def types (request, mytype):
    if (mytype == 'vacancy' or 'result' or 'admit'):
        allLinks = alert.objects.filter(Type=mytype).values()
        sortedLink = allLinks.order_by('-last_date')
        para = {'Link': sortedLink, 'type':mytype}
     
    return render(request, 'linkbase.html', para)