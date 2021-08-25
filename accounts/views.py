from django.shortcuts import render
from .models import Kineto_Kisom
from .resource import Kineto_Kisom_Resource
from django.http import HttpResponse

from tablib import Dataset
# Create your views here.
def upload_file(request):
    if(request.method == 'POST'):
        # if form is submitted then POST request will be there then request will be handled here
        
        # used to IMPORT the uploaded file in the model
        trade_res = Kineto_Kisom_Resource()
        
        # used to LOAD and READ the uploaded file 
        dataset = Dataset()
        
        # get the FILE which was uploaded in the form
        uploaded_file = request.FILES['temp_file']
        
        # to read the uploaded file
        imported_data = dataset.load(uploaded_file.read())
        # print(imported_data)
        
        # dry_run is a Boolean which determines if changes to the database are made or if the import is only simulated. It defaults to False.

        # raise_errors is a Boolean. If True, import should raise errors. The default is False, which means that eventual errors and traceback will be saved in Result instance.
        
        result_temp = trade_res.import_data(dataset, dry_run=True) 
        # test the Data  Import here and check that if it raises an ERROR or not if it doesn't raises an ERROR then we will Perform Actual IMPORT 
        
        if (not result_temp.has_errors()):
            trade_res.import_data(dataset, dry_run=False) 
            # no ERROR actual Data Import
            
        return HttpResponse('Data Imported Successfully')
             
    else:
        return render(request, 'main_page.html')
        # default GET request will be there so we will display simple MAIN_PAGE
        
def export_CSV(request):
    res_download = Kineto_Kisom_Resource()
    
    dataset_download = res_download.export() 
    
    response = HttpResponse(dataset_download.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Trade Data.csv"'
    
    return response

def export_JSON(request):
    res_download = Kineto_Kisom_Resource()
    
    dataset_download = res_download.export() 
    
    response = HttpResponse(dataset_download.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="Trade Data.json"'
    
    return response

def export_XLS(request):
    res_download = Kineto_Kisom_Resource()
    
    dataset_download = res_download.export() 
    
    response = HttpResponse(dataset_download.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Trade Data.xls"'
    
    return response