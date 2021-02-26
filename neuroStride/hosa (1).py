from numpy import loadtxt
from keras.layers import Dense
from keras.models import Sequential
import sys

'''
1. Make the target class (whether they have disease or nah) the last value in each row of the csv
2. Clean the dataset so there are no empty values; if value is empty remove either the feature or the row
3. Make all the values seperated by comma with no space
4. run code like this:
    python script.py <filename>.csv <number of features>

    The number of features is the number of values per row in the dataset excluding the target class
'''
print(sys.argv[1])
print(sys.argv[2])

data = loadtxt(sys.argv[1], delimiter=",")

x = data[:,0:int(sys.argv[2])]
y = data[:,int(sys.argv[2])]

model = Sequential()
model.add(Dense(17, input_dim=17, activation="relu"))
model.add(Dense(13, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x, y, epochs=2000,batch_size=10)
_, a = model.evaluate(x, y)
model.save("Srimann.h5")

print("Acc: " + str(a*100))
