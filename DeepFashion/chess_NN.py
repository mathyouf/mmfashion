from chess_guesser import main
from chess_guesser import print_Gameboard
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = []
Y = []
n = 10
for pair in main(n):
    # print_Gameboard(pair[1], pair[0])
    pair[0].append(n)
    X.append(pair[0])
    Y.append(pair[1][-1][-1])

#validate data shape
X = np.asarray(X)
Y = np.asarray(Y)

# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
print("Input X Vals", X_test)
print("Predictions", predictions)
print("Real Values", y_test)