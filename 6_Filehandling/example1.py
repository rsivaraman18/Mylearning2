print("Hello Python")

# import os
# print(os.getcwd())
# # print(dir(os))

# # os.mkdir('Dummycheck')
# print(os.listdir(r"D:\Siva\2.Mylearnings\07_Python"))
# os.rename('old','new')
# os.mkdir('test')
# os.rmdir('test')
# os.listdir(("path"))

# with open("filename","r") as file:
#     content = json.load(file)

# import csv
# import json
# with open("filename","r") as file:
#     content = csv.reader(file)
#     for line in content
import csv
with open('student.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "name", "Age"])
    writer.writerow([1, "Siva", 21])
    writer.writerow([2, "Harry", 23])

from django.shortcuts import render
from django.http import HttpResponse
def members(request):
    return HttpResponse("Hello world!")
def members(request):
    return render(request,"index.html")