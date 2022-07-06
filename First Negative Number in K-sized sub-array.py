k=3
arr = [1,-3,-12,4,-5,6,-4,13,-2,6,7,5]
negatives = []
i,j = 0,0
while j < len(arr):
    if len(arr)==0:
        print(0)
    else:
        if j-i+1 < k :
            if arr[j] <0 :
                negatives.append(arr[j])
                
            j += 1
            
        elif j-i+1 == k :
            if i==0:
                if arr[j]<0:
                    negatives.append(arr[j])
                    
            else:
                if len(negatives) != 0 and negatives[0]==arr[i]:
                    print(negatives.pop(0))
                if arr[j]<0:
                    negatives.append(arr[j])
                if len(negatives)==0:
                    print(0)
                    
            j += 1
            i += 1
        
    
