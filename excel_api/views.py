from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse


import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def read_excel(request):
    file_name = request.data.get('file_name')
    sheet_name = request.data.get('sheet_name', 'Sheet1')  # Use 'Sheet1' as the default sheet name

    file_path = f'{settings.EXCEL_FILES_FOLDER}/{file_name}'
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
        return Response(data.to_dict(orient='records'))
    except Exception as e:
        return Response({'error': f'Error reading the file: {str(e)}'}, status=400)