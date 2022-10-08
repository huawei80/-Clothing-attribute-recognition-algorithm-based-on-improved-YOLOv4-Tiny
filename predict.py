'''
predict.py有几个注意点
1、无法进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
2、如果想要保存，利用r_image.save("img.jpg")即可保存。
3、如果想要获得框的坐标，可以进入detect_image函数，读取top,left,bottom,right这四个值。
4、如果想要截取下目标，可以利用获取到的top,left,bottom,right这四个值在原图上利用矩阵的方式进行截取。
'''
from PIL import Image
import os
from yolo import YOLO
import cv2
yolo = YOLO()

def getPath(level,path):
    allFileNum =0
    dirList = []
    fileList = [ ]
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            
            mypath =os.path.join(path + '/' + f)
            #if mypath.lower().endswith(('.txt')):
            if mypath.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            # 添加文件
                fileList.append(mypath)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            # print('-' * (int(dirList[0])), dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            getPath((int(dirList[0]) + 1), path + '/' + dl)
    return fileList
    for fl in fileList:
        # 打印文件
        # print('-' * (int(dirList[0])), fl)
        # print(fl)

        allFileNum = allFileNum + 1
        # save_jpg = save_path_jpg + "/" + str(allFileNum)+ ".jpg"
        # # save_jpg = self.save_path_jpg + "/" + str(self.allFileNum).zfill(6)+ ".jpg"
        # shutil.copyfile(fl ,save_jpg)
        # print(save_jpg)


fileList = getPath(0,r"E:\datasets\DeepFashion2\val\image")
for fl in fileList:  
    # img = fl
    # print(img)

    my_jpg = r"E:\datasets\DeepFashion2\val\image"
    img = ""
    num = fl.split("/")[-1].split(".")[0]
    if(int(num) > 12000 ):
        img = my_jpg + "/" + fl.split("/")[-1].split(".")[0] + ".jpg"
    # img = cv2.resize(img,(64,64))
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)

        savep = r"C:\Users\sky\Desktop\1/" + fl.split("/")[-1].split(".")[0] +  "res2_1.jpg"
        print(savep)
        r_image.save(savep)
        r_image.show()
