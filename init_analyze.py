from analyze import *
print(os.path.exists("pack/temp/log000.txt"))
# all available - indexed from 0
print(len(os.listdir("pack/temp")))
#initialize into all.json
print(os.getcwd())
c = 0
while(c < 5):#len(os.listdir("temp"))):
    if(os.path.exists("pack/temp/log{}.txt".format(lformat(c)))): 
        f = open("pack/temp/log{}.txt".format(lformat(c)))
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

    print("{}:{}".format(c,len(os.listdir("pack/temp"))))
data.to_json("all.json")
data.to_csv("all.csv")
print(data.head())