import time
from flask import Flask, render_template, request
from requests import get

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=["GET"])
def index():

    request_limit=3
    count=0
    
    data = request.environ['REMOTE_ADDR']
    #data=request.environ['HTTP_X_FORWARDED_FOR']
    #data = get('https://api.ipify.org').text
    array=[]

    try:
        file = open('ip_list.txt','a')
    except:
        print("Can not open the file!")
    finally:
        check = open('ip_list.txt','r')
        for line in check:
            array.append(line)
            if data in line:
                count += 1

        if count<request_limit:
            file.write(data + " - Requested: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n")
            file.close()
        else:
            data=("Too many request from the same source IP!")

    
    req_time=time.strftime("%Y-%m-%d %H:%M:%S")+"\n"
    #ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    #print (ip+"\n")
    #print ("Received IP: "+data)
    return render_template('index.html',data=data,req_time=req_time,array=array)
  

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000,debug = True)