from analyze import *

dir = "../templogs0/pack/temp"
print(os.path.exists("{}/log000.txt".format(dir)))
# all available - indexed from 0
#print(len(os.listdir("out")))

#initialize into all.json
print(os.getcwd())
c = 0
while(c < 5):#len(os.listdir("temp"))):
    if(os.path.exists("{}/log{}.txt".format(dir,lformat(c)))): 
        f = open("{}/log{}.txt".format(dir,lformat(c)))
        for i in f:
            time_ms = json.loads(i)["time_ms"]
            time = json.loads(i)["time"]
            message = json.loads(i)["message"]
            data1 = pd.DataFrame({
                "time_ms":[time_ms],
                "time":[time],
                "message":[message]
            })
            data = data.append(data1,ignore_index=True)
    c+=1

    print("{}:{}".format(c,len(os.listdir("../templogs0/pack/temp"))))
data.to_json("all.json")
data.to_csv("all.csv")
print(data.head())