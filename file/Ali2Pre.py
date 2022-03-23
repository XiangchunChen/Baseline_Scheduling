import re

if __name__ == '__main__':
    num = 40
    f1 = open("Alibaba_dataset/Ali_task_"+str(num)+".csv", "r")
    f2 = open("Alibaba_dataset/task_pre_"+str(num)+".csv", "w")
    lines = f1.readlines()
    # id = 1
    for line in lines:
        # 找到该job中对应的subId
        # 第一个job自然是原数字
        info = line.split(",")
        line0 = info[0]
        taskId = info[1][2:]
        nums = re.findall(r"\d+\.?\d*", line0)
        # print(line)
        subId = int(taskId)*10+int(nums[0])
        # print(line0)
        if len(nums) == 1:
            # num1 = int(nums[0])
            start = subId
            # end = int(taskId)*10+int(nums[0])
            f2.write(str(start)+","+str(start)+"\n")
        elif len(nums) == 2:
            # num1 = int(nums[0])
            # num2 = int(nums[1])
            start = subId
            end = int(taskId)*10+int(nums[1])
            f2.write(str(end)+","+str(start)+"\n")
        elif len(nums) == 3:
            start = subId
            end1 = int(taskId)*10+int(nums[1])
            end2 = int(taskId)*10+int(nums[2])
            f2.write(str(end1)+","+str(start)+"\n")
            f2.write(str(end2)+","+str(start)+"\n")
        elif len(nums) == 4:
            start = subId
            end1 = int(taskId)*10+int(nums[1])
            end2 = int(taskId)*10+int(nums[2])
            end3 = int(taskId)*10+int(nums[3])
            f2.write(str(end1)+","+str(start)+"\n")
            f2.write(str(end2)+","+str(start)+"\n")
            f2.write(str(end3)+","+str(start)+"\n")
        elif len(nums) == 5:
            start = subId
            end1 = int(taskId)*10+int(nums[1])
            end2 = int(taskId)*10+int(nums[2])
            end3 = int(taskId)*10+int(nums[3])
            end4 = int(taskId)*10+int(nums[4])
            f2.write(str(end1)+","+str(start)+"\n")
            f2.write(str(end2)+","+str(start)+"\n")
            f2.write(str(end3)+","+str(start)+"\n")
            f2.write(str(end4)+","+str(start)+"\n")
        else:
            # print(line)
            print("wrong:",line)
    f1.close()
    f2.close()