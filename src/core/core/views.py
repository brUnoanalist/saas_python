from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view( request, *args, **kwargs):
    html_ =""
    html_file_path = this_dir /"home.html"
    html_ = html_file_path.read_text()
    html_template="home.html"
    return render(request, html_template)