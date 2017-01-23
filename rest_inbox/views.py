from __future__ import unicode_literals, absolute_import

import requests
import datetime
import grequests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, status
from django.contrib import auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response


def home(request):
    return render(request, 'index.html')


@csrf_exempt
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((permissions.IsAuthenticated,))
def get_user(request):
	content = {
		'user': unicode(request.user),
	}
	return Response(content)


def get_email(response):
	r = response.json()
	if response.status_code != 200:
		return None
	result = {
		"Message": r.get("snippet")
	}
	for header in r.get("payload").get("headers"):
		if header.get("name") in ["Date", "Subject", "From"]:
			result[header.get("name")] = header.get("value")
	return result


@csrf_exempt
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((permissions.IsAuthenticated,))
def get_mails(request):
	user = User.objects.get(username=request.user)
	social = user.social_auth.get(provider='google-oauth2')
	r = requests.get(
	    "https://www.googleapis.com/gmail/v1/users/me/messages",
	    params={'access_token': social.extra_data['access_token'], 'maxResults': 100}
	)
	if r.status_code != 200:
		return Response({
			"message": "Error during request Gmail API"
		}, status=status.HTTP_400_BAD_REQUEST)
	response = r.json()
	rs = (
		grequests.get(
			"https://www.googleapis.com/gmail/v1/users/me/messages/%s" % (message.get("id")),
			params={'access_token': social.extra_data['access_token'], "format": "metadata"}
		) for message in response.get("messages"))
	responses = grequests.map(rs)
	results = []
	for response in responses:
		result = get_email(response)
		if result:
			results.append(result)
	return Response(results)


@csrf_exempt
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((permissions.IsAuthenticated,))
def logout(request):
	auth.logout(request)
	return Response({
		"message": "User is logged out"
	})
