from django.shortcuts import path
from writing_to_excel_and_loading_file.views import write_data_excel, read_data_from_excel_file

urlpatterns = [
    path('write_data_excel/', write_data_excel, name='write_data_excel'),
    path('read_data_from_excel_file/', read_data_from_excel_file, name='read_data_from_excel_file')
]
