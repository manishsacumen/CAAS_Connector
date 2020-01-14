from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests.auth import HTTPBasicAuth
import requests
import json
from .models import Jira
from Connector.models import SSCConnector



# Create your views here.


class Connector:
    
    __headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def __init__(self, url, username, api_token):
        self.__url = url
        self.__username = username
        self.__api_token = api_token
        self.__auth = HTTPBasicAuth(username, api_token)
        
    
    def get_issue_url(self):
        return self.__url + '/rest/api/3/issue'


    def get_issue_detail_url(self, issue_id):
        return "{}/{}".format(self.get_issue_url(), issue_id)


    # Get the details of an issue based on given issue_id
    def get_issue_details(self, issue_id):
        url = self.get_issue_detail_url(issue_id)

        request = requests.get(url, auth=self.__auth)

        if request.status_code == 200:
            return request.json() 

        raise ValueError("Received invalid response {} with status code {}".format(
            request.content, request.status_code))
            

    # Creating new issue
    def create_issue(self, **data):
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        payload = json.dumps(data)

        request = requests.post(self.get_issue_url(), payload, auth=self.__auth, headers=headers)

        if request.status_code == 201:
            return request.json()

        raise ValueError("Received invalid response {} with status code {}".format(
            request.content, request.status_code))




def jira_register(request):

    jira_config = request.POST.dict()
    current_user = request.user
    app_url = jira_config.get('app_url')
    email_id = jira_config.get('email_id')
    api_key = jira_config.get('api_key')
    test_api = "/rest/api/2/issue/createmeta"
    project_key = jira_config.get('project_key')
    test_api_url = "{}/{}".format(app_url, test_api)

    auth  = HTTPBasicAuth(email_id, api_key)
    res = requests.get(url=test_api_url, auth=auth)
    if res.status_code == 200:
        new_jira = Jira(user_id=current_user, app_url=app_url, email_id=email_id, api_key=api_key, project_key=project_key)
        new_jira.save()
        messages.success(request, f'Jira connected Successfully..!!')
        return redirect('/home/')
    else:
        messages.error(request, f'There is some problem in connection..!! Please Try Again')
        return redirect('/home/')

    return render(request, 'dashboard/home.html')
