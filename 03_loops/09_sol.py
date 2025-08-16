items = ["apple","banana","orange","apple","mango"]
c=0
for item in items:
    if items.count(item)>1:
        c=1
        print(item)
        break
    else:
        continue
if c!=1:
    print("Unique")
