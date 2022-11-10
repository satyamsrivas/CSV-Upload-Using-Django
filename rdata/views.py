
from django.shortcuts import render
from django.http import HttpResponse
from .models import Csv, TradingData
import pandas as pd
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import csv


fs = FileSystemStorage(location='media/')


# Create your views here.


def index(request):
    if request.method == "POST":
        file_input = request.FILES['document']  # takes the file input
        content = file_input.read()  # saves the content
        file_content = ContentFile(content)  # create a new file with content
        # saves the file in local storage
        file_name = fs.save(file_input.name, file_content)
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors='ignore')  # converts back to csv
        reader = csv.reader(csv_file)
        next(reader)
        trading_list = []
        for id, row in enumerate(reader):
            (
                Date,
                Open,
                Close,
                High,
                Low,
                Adj_Close,
                Volume,
            ) = row

            trading_list.append(
                TradingData(

                    Date=Date,
                    Open=Open,
                    Close=Close,
                    High=High,
                    Low=Low,
                    Adj_Close=Adj_Close,
                    Volume=Volume,
                )
            )
        TradingData.objects.bulk_create(trading_list)

    data = TradingData.objects.all()
    return render(request, 'index.html', {"key_data": data})
