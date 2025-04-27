
def selectionSort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range (i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index= j
        

        arr[i],arr[min_index]=arr[min_index],arr[i]

        print (F"The Output After Pass {i+1} is : {arr}")


# arr=[38,57,23,54,23,21,2]
# selectionSort(arr)

userInput = input ("Enter the Num Seperated By Spaces = ")
userInput=userInput.split()
userInput=[int(i) for i in userInput]
selectionSort(userInput)
