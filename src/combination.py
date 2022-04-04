import os
import json

def final_cameras(name, regions, rtsp="", interest_time="", floor=""):
    result = {
        "name": name,
        "rtsp": rtsp,
        "floor": floor,
        "interest_time": interest_time,
        "regions": regions
    }
    return result

def final(block_time, store_name, open_time, close_time, cameras):
    result = {
        "block_time": block_time,  
        "store_name": store_name,
        "open_time": open_time,
        "close_time": close_time,
        "cameras": cameras
    }
    return result
cameras = []
list_check = []
folder = "line_poly"
for i in os.listdir(folder):
    name = "_".join(i.split("_")[:-1])
    js = os.path.join(folder, i)
    if name not in list_check:
        list_check.append(name)
        with open(js, "r") as file:
            out = json.load(file)
            # print(out)
            # exit()
            camera = final_cameras(name=name, regions=out)
        cameras.append(camera)
    else:
        with open(js, "r") as file:
            out = json.load(file)
        for o in out:
            for c in cameras:
                if c['name'] == name:
                    c["regions"].append(o)
final = final(60, "", "", "", cameras)
with open("config_test.json", "w") as json_file:
    json.dump(final, json_file, indent = 4)