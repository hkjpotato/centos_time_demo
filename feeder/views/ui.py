from django.shortcuts import render, render_to_response
# from feeder.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json

templatePrefix = 'feeder'

# Create your views here.
def test(request):
    return HttpResponse('hello')

def testui(request):
    return render_to_response(templatePrefix + '/' + 'testui.html', locals())

def saveData(request):
    if request.method == 'GET':
        # do_something()
        print 'get request'
    elif request.method == 'POST':
        with open("data/cases/" + "newLoc" + ".json", "w") as outFile:
            data = json.loads(request.body)
            json.dump(data, outFile, indent=4)
    return HttpResponse(status=204)


def distributionOutputData(request):
    if 'caseName' in request.GET:
        caseName = request.GET['caseName']
    if 'feederName' in request.GET:
        feederName = request.GET['feederName'] 
    with open("data/cases/" \
        + caseName \
        + "/jsondata/distribution/output/" \
        + feederName \
        +"_output.json", "r") as t_data:
        data = json.load(t_data)
    return JsonResponse(data, safe=False)

def distributionData(request):
    if 'caseName' in request.GET:
        caseName = request.GET['caseName']
    if 'feederName' in request.GET:
        feederName = request.GET['feederName'] 
    with open("data/cases/" \
        + caseName \
        + "/jsondata/distribution/input/" \
        + feederName \
        +".json", "r") as t_data:
        data = json.load(t_data)
    return JsonResponse(data, safe=False)


def transmissionData(request):
    if 'caseName' in request.GET:
        caseName = request.GET['caseName']
    if 'transmissionName' in request.GET:
        transmissionName = request.GET['transmissionName']
    with open("data/cases/" \
        + caseName \
        + "/jsondata/transmission/input/" \
        + transmissionName \
        +".json", "r") as t_data:
    # with open("data/cases/newyork/jsondata/transmission/transmission.json", "r") as t_data:
        data = json.load(t_data)
    return JsonResponse(data, safe=False)


def feederDataTest(request):
    if 'zoomLevel' in request.GET:
        zoomLevel = request.GET['zoomLevel']
        print 'zoomLevel', zoomLevel
    zoomLevel = int(request.GET.get('zoomLevel', 12))
    pgObj = {}
    with open("data/" + "omf_data.json", "r") as all:
        pgObj = json.load(all)
    data = pgObj
    # if (zoomLevel <= 13):
    #     print 'smaller than 13'
    #     with open("data/" + "nyc_transmission.json", "r") as transmission:
    #         transdata = json.load(transmission)
    #     pgObj.update(transdata)
    # else:
    #     print 'larger than 13'
    #     # feederData = makeFeeder("Circuit01")
    #     # pgObj.update(feederData)
    #     # print 'we really try'
    #     with open("data/" + "all.json", "r") as all:
    #         transdata = json.load(all)
    #     pgObj.update(transdata)
    #     # with open("data/" + "all" + ".json", "w") as outFile:
    #     #     json.dump(pgObj, outFile, indent=4)
    # data = pgObj
    return JsonResponse(data, safe=False)

