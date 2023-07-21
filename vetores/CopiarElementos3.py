from insert import insertVectorValues;

numbersCopy = [];
numbers = [];

numbers = insertVectorValues();


def transfer(vector):
    vectorCopy = [];

    #vectorCopy = vector.copy();

    while(True):
        vectorCopy.append(vector[0]);
        vector.remove(vector[0]);
        
        if(len(vector)<1):
            break;

    return (vectorCopy);

numbersCopy = transfer(numbers);

print(numbersCopy);