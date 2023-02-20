#### Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Activity, ActivityTracker
from django.views import View
from .helpers import GetBody
from django.core.serializers import serialize

####  Activity Views
class ActivityView(View):
    ### Index - displaying all
    def get(self, request):
        activity = Activity.objects.all()
        serialized = serialize("json", activity)
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)
    #### Create
    def post(self, request):
        print('request', request)
        body = GetBody(request)  
        print("body", body) 
        activity = Activity.objects.create(activity=body["activity"],category=body["category"],description=body["description"])
        print("activity", activity)
        finalData = json.loads(serialize("json",[activity]))
        return JsonResponse(finalData, safe=False)
    
class ActivityViewID(View): 
    ### Show
    def get(self, request, id):
        activity = Activity.objects.get(act_id=id)
        finalData=json.loads(serialize("json", [activity]))
        return JsonResponse(finalData, safe=False)
    
    def put(self, request, id):
        body = GetBody(request)
        ## unpacking the dictionary and making them arguments
        Activity.objects.filter(act_id=id).update(**body)
        activity = Activity.objects.get(act_id=id)
        finalData = json.loads(serialize("json", [activity]))
        return JsonResponse(finalData, safe=False)
    
    def delete(self, request, id):
        activity = Activity.objects.get(act_id=id)
        activity.delete()
        finalData = json.loads(serialize("json", [activity]))
        return JsonResponse(finalData, safe=False)
        
        
####  Activity Tracker Views
class ActivityTrackerView(View):
    ### Index - displaying all
    def get(self, request):
        activity_tracker = ActivityTracker.objects.all()
        serialized = serialize("json", activity_tracker)
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)
    #### Create
    def post(self, request):
        body = GetBody(request)   
        activity_tracker = ActivityTracker.objects.create(act_main_id=body["act_main_id"],activity_date=body["activity_date"],activity_count=body["activity_count"])
        finalData = json.loads(serialize("json",[activity_tracker]))
        return JsonResponse(finalData, safe=False)
    
class ActivityTrackerViewID(View): 
    ### Show
    def get(self, request, id):
        # print ("request", id, request)
        body = GetBody(request)
        # print ("body - before", body)
        # ## unpacking the dictionary and making them arguments
        ActivityTracker.objects.filter(act_main_id=id).update(**body)
        # print ("body - after", body)
        # print ("ActivityTracker.objects.filter", ActivityTracker.objects.filter)
        
        activity_tracker = ActivityTracker.objects.get(act_main_id=id)
        finalData=json.loads(serialize("json", [activity_tracker]))
        return JsonResponse(finalData, safe=False)
    
    def put(self, request, id):
        body = GetBody(request)
        ## unpacking the dictionary and making them arguments
        ActivityTracker.objects.filter(act_trk_id=id).update(**body)
        activity_tracker = ActivityTracker.objects.get(act_trk_id=id)
        finalData = json.loads(serialize("json", [activity_tracker]))
        return JsonResponse(finalData, safe=False)
    
    def delete(self, request, id):
        activity_tracker = ActivityTracker.objects.get(act_trk_id=id)
        print ("activity_tracker", activity_tracker)
        activity_tracker.delete()
        finalData = json.loads(serialize("json", [activity_tracker]))
        return JsonResponse(finalData, safe=False)

