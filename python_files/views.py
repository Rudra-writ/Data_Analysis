from msilib.schema import Directory
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from .forms import OptionsForm
from django.http import HttpResponse


def first_page(request):
    context = {}
    form = OptionsForm(request.POST or None)
    context['form'] = form
    if( request.method == 'POST'):
        if ( 'plot'  in  request.POST):
        
                if(form.is_valid()):
                        parameter = form.cleaned_data.get("filters")
                        print(parameter)
                        if(len(parameter)<=7):
                            shutil.copy2("P:\\Test_Log.csv", "P:\\project\\newproject\\newproject\\static\\Test_Log.csv") 
                           
                            df = pd.read_csv('P:\SLM_Analyzer\slmAnalyst\static\Sensor.csv', sep = ",|;", engine = 'python')
                           
                            chunksize = 10 ** 6
                            for chunk in pd.read_csv("P:\\project\\newproject\\newproject\\static\\Test_Log.csv",delimiter=";",low_memory=True, index_col=False, dtype="unicode",chunksize=chunksize):
                                    df = pd.DataFrame(chunk)
                            columns = []
                            df.reset_index(drop = True, inplace =True)

                            df.dropna(axis='columns',how='all', inplace = True)
                            df.fillna('0', inplace =True)

                            df = df.loc[:, ~(df == '0').all()]
                            columns = list(df)
                            df = df.apply(pd.to_numeric, errors = 'coerce')
                        
                            fig,ax = plt.subplots()
                            colors = ['b', 'y', 'g', 'r', 'm', 'c', 'k']
                            for params, index in zip(parameter, range(len(parameter))):
                                    ax.plot( df['Time[s]'], df[params], color = colors[index] , label = params)
                            plt.xlabel("Time in seconds")
                            plt.ylabel(',  '.join(str(params) for params in parameter) )
                            plt.title(',  '.join(str(params) for params in parameter)  + " Vs Time[s]")
                            ax.legend()
                            plt.show()
                            print(df.head(50))
                            
                            return render(request,'first_page.html',context)
                                    
                        else:
                            return render(request,'first_page.html',context)
        else:
            return render(request,'first_page.html',context)

    else:
        return render(request,'first_page.html',context)