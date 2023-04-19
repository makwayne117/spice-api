from flask import Flask, request
from flask import jsonify
import spiceypy
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
import subprocess
import numpy as np
import datetime
from urllib.request import urlopen
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

# loads in all the kernels of a specific mission  
def load_kernels(mission):
    # read missions dictionary from the file
    with open('missions.json', 'r') as f:
        missions = json.load(f)

    kernel_urls = missions[mission]

    for url in kernel_urls:
        # Download the kernel file and load it into SPICE
        with urlopen(url) as f:
            kernel_data = f.read()
            spiceypy.furnsh_c(kernel_data)
        
        # Use the kernel data
        # ...


@app.after_request
def after_request(response):
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  print("CORS")
  return response


@app.route('/pos', methods=['GET'])
def return_body_position():
    #METAKR = 'getsa.tm'
    METAKR = 'ss_kernel.mk'
    target = request.args.get('planet')
    utctim = request.args.get('utc')
    obs = 'SUN'
    if(utctim == None):
        utctim = "2004 jun 11 19:32:00"
    #utctim = "2004 jun 11 19:32:00"
    print(target)
    spiceypy.furnsh(METAKR)

    et = spiceypy.str2et(utctim)

    [return_pos, ltime] = spiceypy.spkpos(target, et, 'J2000',
                                          'LT+S', obs, )
    
    if ('BARYCENTER' in target):
        target = target.replace(' BARYCENTER', '')
    [dim,radii] = spiceypy.bodvrd(target,"RADII",3)

    spiceypy.unload(METAKR)
    print("radius",radii)
    print(jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2]}))
    
    return jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2], "r": radii[0]})

@app.route('/mission', methods=['GET'])
def return_spacecraft_position():
   # read missions dictionary from the file

    with open('missions.json', 'r') as f:
        missions = json.load(f)
        print("in missions")
    mission = request.args.get('mission')
    kernel_urls = missions[mission]
    kernel_urls = ["kernels/"+mission +"/"+ x for x in kernel_urls]
    print(kernel_urls)

    #Lets add the leapsecond file to the kernel pool
    kernel_urls.append("kernels/leap.tls")
    #Add all kernels to spice and compute data for VOYAGER 1 1
    spiceypy.furnsh(kernel_urls)
    target = request.args.get('mission')
    utctime = request.args.get('utc')
    obs = "SUN"
    et = spiceypy.str2et(utctime)
    [return_pos, ltime] = spiceypy.spkezr(target, et, 'J2000', 'LT+S', obs)
    spiceypy.unload(kernel_urls)
    print(jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2], "vx": return_pos[3], "vy": return_pos[4], "vz": return_pos[5]}))
    return jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2], "vx": return_pos[3], "vy": return_pos[4], "vz": return_pos[5]})


@app.route('/orbits', methods=['GET'])
def return_position():
    #METAKR = 'getsa.tm'
    METAKR = 'ss_kernel.mk'
    target = request.args.get('planet')
    utctim = request.args.get('utc')
    length = request.args.get('length')
    obs = 'SUN'
    if(utctim == None):
        utctim = "2004 jun 11 19:32:00"
    utctim = utctim[:-1]
    utctim = datetime.datetime.fromisoformat(utctim)
    print(target)
    spiceypy.furnsh(METAKR)

    #testUtc = datetime.datetime.now()
    temp = np.array(utctim.isoformat(),dtype=object)
    for i in range(int(length)):
        temp = np.append(temp,(utctim-datetime.timedelta(i)).isoformat())
    #print("Temp Times:",temp)
    et = np.empty(0)
    for i in range(0,len(temp)):
        et = np.append(et,spiceypy.str2et(temp[i]))
    #print("TestEt:", testEt)
    #print("Shapes",len(temp),len(testEt))

    [return_pos, ltime] = spiceypy.spkezr(target, et, 'J2000',
                                          'LT+S', obs, )

    spiceypy.unload(METAKR)
    #print("Spice:", return_pos)
    data = [l.tolist() for l in return_pos]
    #print("List",data)
    #return (return_pos.tolist())
    return(data)
    #return (return_pos.tolist())

@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
     print("Got request in static files")
     print(request.files)
     f = request.files['static_file']
     f.save(f.filename)
     spiceypy.furnsh(f)
     resp = {"success": True, "response": "file saved!"}
     return jsonify(resp), 200

#Endpoint: form_data.
#Description: a function that processes the requested object and time with spkpos through the form
@app.route('/form_data', methods=['GET'])
def return_position_form():
    METAKR = 'getsa.tm' #Kernel name. getsa.tm is a metakernel that processes the data for the CASSINI misison. Eventually this will work with all missions
    target = request.args.get('Planet') #planet: self explanatory
    obs = 'SUN' #for now, all missions will be observed from the reference frame of the sun.
    utctim = request.args.get('Time') #time: the requested time
    print(target)

    spiceypy.furnsh(METAKR) #load the kernel.
    et = spiceypy.str2et(utctim) #CONVERT TIME TO UTC
    [return_pos, ltime] = spiceypy.spkpos(target, et, 'J2000',
                                          'LT+S', obs, )

    spiceypy.unload(METAKR)


    print(jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2]}))

    return jsonify({"x": return_pos[0], "y": return_pos[1], "z": return_pos[2]}) #RETURN COORDINATES IN JSON.

@app.route('/get_body', methods=['GET'])
def getBody():
    kernel = request.args.get('kernels')  # planet: self explanatory
    ids = []
    idso = []
    bodylist = []
    # for x in Kernels:
    #     ids = spiceypy.spkobj(Kernels, idso)
    #     for i in range(len(ids)):
    #         body = spiceypy.bodc2n(ids[i])
    #         bodylist.append(body)
    ids = spiceypy.spkobj(kernel, idso)
    for i in range(len(ids)):
        body = spiceypy.bodc2n(ids[i])
        bodylist.append(body)
    return bodylist


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to spice-api!</h1>"

#api.add_resource(SpiceCalc, '/orbits')

if __name__ == "__main__":
    app.run(threaded=True, port=5000)




