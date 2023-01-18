import sys
sys.path.append('./')
import Assignment_Submission;
inp = input()
item_price = {}
items = inp.replace("{","").replace("}","").replace('"','').split(",")
for i in items:
    item_price[i.split(":")[0]] = int(i.split(":")[1])
print(Assignment_Submission.question4(item_price))
