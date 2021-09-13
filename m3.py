import csv
from collections import Counter
from types import MemberDescriptorType

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
total_weight = 0
total_entries = len(file_data)
asc_data = []

for i in file_data:
    total_weight += float(i[2])
    asc_data.append(float(i[2]))

asc_data.sort()

def mean(total_weight, total_entries) :
   mean = total_weight/total_entries
   print("Mean is: " + str(mean))

def median(total_entries, asc_data) :
    if total_entries%2 == 0:
        med1 = float(asc_data[total_entries//2])
        med2 = float(asc_data[total_entries//2-1])
        med = (med1 + med2)/2
    else:
        med = float(asc_data[total_entries//2])
    print("Medain is: " + str(med))

def mode(asc_data) :
    data = Counter(asc_data)
    modeDataForRange = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }
    for weight,occurence in data.items():
        if 75 < weight < 85:
            modeDataForRange["75-85"]+=occurence
        elif 85 < weight < 95:
            modeDataForRange["85-95"]+=occurence
        elif 95 < weight < 105:
            modeDataForRange["95-105"]+=occurence
        elif 105 < weight < 115:
            modeDataForRange["105-115"]+=occurence
        elif 115 < weight < 125:
            modeDataForRange["115-125"]+=occurence
        elif 125 < weight < 135:
            modeDataForRange["125-135"]+=occurence
        elif 135 < weight < 145:
            modeDataForRange["135-145"]+=occurence
        elif 145 < weight < 155:
            modeDataForRange["145-155"]+=occurence
        elif 155 < weight < 165:
            modeDataForRange["155-165"]+=occurence
        elif 165 < weight < 175:
            modeDataForRange["165-175"]+=occurence

    modeRange, modeOccurence = 0, 0

    for range, occurence in modeDataForRange.items():
        if occurence > modeOccurence:
            modeRange, modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode = float((modeRange[0]+modeRange[1])/2)
    print(f"mode is: {mode:2f}")

mean(total_weight, total_entries)
median(total_entries, asc_data)
mode(asc_data)