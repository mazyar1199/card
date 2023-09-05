sum=0
i=1
while True:
    score = float(input("score (-1 to end): "))
    if (score==-1):
        break
    sum+=score
    
    i+=1
ave=sum/i

print("ave: ",ave)