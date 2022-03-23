import random
import re

if __name__ == '__main__':
    num = 40
    f1 = open("Alibaba_dataset/Ali_task_"+str(num)+".csv", "r")
    f2 = open("Alibaba_dataset/task_info_"+str(num)+".csv", "w")
    lines = f1.readlines()
    # id = 1
    for line in lines:
        info = line.split(",")
        nums = re.findall(r"\d+\.?\d*", info[0])
        taskId = info[1][2:]
        subId = int(taskId)*10+int(nums[0])
        # print("subId", subId)
        process_time = int(info[4]) - int(info[3])
        # print(line)
        cload = int(info[5]) * process_time
        if len(nums) == 1:
            dataSize = random.randint(0,100)+cload/2
        else:
            dataSize = 0
        # process_time = int(info[4]) - int(info[3])
        release_time = 0
        source = 1
        # id = id + 1
        f2.write(str(subId)+","+str(taskId)+","+str(dataSize)+","
                 +str(cload)+","+str(release_time)+","+str(source)+","
                 +str(process_time)+"\n")
    f1.close()
    f2.close()