lastvalue = 0
numberOfTimesDepthIncreases = 0

with open('input','r') as f:
    values = f.readlines()
    for value in values:
        if int(value) > lastvalue:
            if lastvalue != 0:
                numberOfTimesDepthIncreases+=1
        lastvalue = int(value)

print("The number of times the depth increased was:", numberOfTimesDepthIncreases)