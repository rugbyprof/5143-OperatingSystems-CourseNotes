import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None
        self.total = 0

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1
                self.total += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        for i in range(5):
            for j in range(5):
                if j > 0:
                    print(" , ",end="")
                pct = (int(self.sort_freq[i*5+j][1])/self.total)*100
                pct = "{:5.2f}".format(pct)
                print(f"{self.sort_freq[i*5+j][0]}:{pct}%",end=" ")
            print("")

if __name__=='__main__':
    url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    print("Downloading book ...")
    f = requests.get(url)
    text = f.text
    print("Calculating frequency...")
    F = Frequency()
    F.count(text)
    F.print()



