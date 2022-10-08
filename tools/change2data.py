
import os
import json

'''
category_id:
1  -- sleeve top           短袖上衣
2  -- long sleeve top      长袖上衣
3  -- short sleeve outwear 短袖外衣
4  -- long sleeve outwear  长袖外衣
5  -- vest     背心
6  -- sling    吊带
7  -- shorts   短裤
8  -- trousers 长裤
9  -- skirt    裙子
10 -- short sleeve dress 短袖连衣裙
11 -- long sleeve dress  长袖连衣裙
12 -- vest dress         背心裙
13 -- sling dress        吊带裙

'''

# num [3941, 1812, 47, 630, 961, 75, 2192, 3111, 1553, 763, 318, 826, 290]
name = ['short sleeve top', 'long sleeve top', 'short sleeve outwear',
        'long sleeve outwear', 'vest', 'sling', 'shorts', 'trousers',
        'skirt', 'short sleeve dress', 'long sleeve dress', 'vest dress',
        'sling dress']
name_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 获取根目录
root = os.getcwd()


# 所有路径
def All_path():
    json_path = r"E:\my\annos"
    img_path = r"E:\my\images"
    save_path  = r"E:\my\data"


    return json_path, img_path, save_path


# 列表转字符串
def list2str(a_list):
    return ",".join(list(map(str, a_list)))


def get_item(it):
    box = it['bounding_box']
    label = it['category_id'] - 1
    box = list2str(box)
    name_num[label] = name_num[label] + 1
    item = box + "," + str(label)
    print("num", name_num)
    return item


def test():
    json_file = 'DeepFashion2/train/annos/000001.json'
    with open(json_file, encoding='utf-8') as f:
        label = json.load(f)
        for key, val in label.items():
            # key: 'item1','item2' 'source' 'pair_id'
            # val: 'bounding_box'  'category_name' 'scale' 'viewpoint' 'occlusion'....
            if 'item' in key:
                print(label[key]['category_name'])
                print(label[key]['bounding_box'])

        f.close()


if __name__ == "__main__":

    file_path, img_path, save_path = All_path()
    # 191962
    for num in range(1, 10001):
        one = os.path.join(file_path, str(num).zfill(6) + ".json")
        img = os.path.join(img_path, str(num).zfill(6) + ".jpg")
        file1 = open(one)
        lines1 = file1.readlines()
        file1.close()
        mm = lines1[0]
        x = json.loads(mm)

        if len(x) == 3:
            it1 = x["item1"]
            item1 = get_item(it1)

            save = img + " " + item1 + "\n"

        if len(x) == 4:
            it1 = x["item1"]
            item1 = get_item(it1)

            it2 = x["item2"]
            item2 = get_item(it2)

            save = img + " " + item1 + " " + item2 + "\n"

        if len(x) == 5:
            it1 = x["item1"]
            item1 = get_item(it1)

            it2 = x["item2"]
            item2 = get_item(it2)

            it3 = x["item3"]
            item3 = get_item(it3)

            save = img + " " + item1 + " " + item2 + " " + item3 + "\n"

        if len(x) == 6:
            it1 = x["item1"]
            item1 = get_item(it1)

            it2 = x["item2"]
            item2 = get_item(it2)

            it3 = x["item3"]
            item3 = get_item(it3)

            it4 = x["item4"]
            item4 = get_item(it4)

            save = img + " " + item1 + " " + item2 + " " + item3 + " " + item4 + "\n"

        if len(x) == 7:
            it1 = x["item1"]
            item1 = get_item(it1)

            it2 = x["item2"]
            item2 = get_item(it2)

            it3 = x["item3"]
            item3 = get_item(it3)

            it4 = x["item4"]
            item4 = get_item(it4)

            it5 = x["item5"]
            item5 = get_item(it5)

            save = img + " " + item1 + " " + item2 + " " + item3 + " " + item4 + " " + item5 + "\n"

        if len(x) == 8:
            it1 = x["item1"]
            item1 = get_item(it1)

            it2 = x["item2"]
            item2 = get_item(it2)

            it3 = x["item3"]
            item3 = get_item(it3)

            it4 = x["item4"]
            item4 = get_item(it4)

            it5 = x["item5"]
            item5 = get_item(it5)

            it6 = x["item6"]
            item6 = get_item(it6)

            save = img + " " + item1 + " " + item2 + " " + item3 + " " + item4 + " " + item5 + " " + item6 + "\n"

        train_file = open(save_path + "/train1.txt", "a")
        train_file.write(save)
        train_file.close()


