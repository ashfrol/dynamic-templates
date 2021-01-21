import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', encoding='utf-8') as fo:
        read_csv = list(csv.reader(fo))
    array = [element.split(';') for l in read_csv for element in l]

    for li in array:
        for num, element in enumerate(li):
            if not element:
                li[num] = '-'

    context = {
        'table': array
    }

    return render(request, template_name,
                  context)