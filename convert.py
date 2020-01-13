# -*- coding: utf-8 -*-
## usage: python convert.py [path to f.txt]
import sys

def start_convert(path):
    # convert encoding
    encoding1 = "cp950"
    encoding2 = "utf-8"
    # f = open(path, "r", encoding = encoding2)
    # content = f.read()
    # f.close()
    # f = open("temp_t.txt", "w", encoding = encoding2)
    # f.write(content)
    # f.close()
    # start processing
    with open(path, "r", encoding = encoding2) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    i = lines.index("==================================")
    participants = lines[3:i]
    participants = [participant.split(": ")[1] for participant in participants]
    words = lines[(i+1):]
    dic = {}
    for par in participants:
        dic[par] = []
    for word in words:
        temp = word.split(": ")
        dic[temp[0]].append(temp[1])
    for par in participants:
        out_file = "output/" + par.replace(" ", "_") + ".txt"
        with open(out_file, "w") as of:
            for sentence in dic[par]:
                of.write(sentence + "\n")

if __name__ == "__main__":
        start_convert("f.txt")