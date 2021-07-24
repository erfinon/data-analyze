from analyze import *
print(os.path.exists("temp/log000.txt"))
# all available - indexed from 0
print(len(os.listdir("temp")))
#initialize into all.json
print(os.getcwd())
print("enter file amount >")
ing = True
climit = int(input())
c = 0
while(c < climit):#len(os.listdir("temp"))):
    if(os.path.exists("temp/log{}.txt".format(lformat(c)))): 
        f = open("temp/log{}.txt".format(lformat(c)))
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
            print("{}:{}".format(c,len(os.listdir("temp"))))
            print(ing)
            ing = not(ing)
    c+=1

#data.to_json("all.json")
data.to_csv("all.csv",chunksize=400)
print(data.head())