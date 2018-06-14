import sklearn
print('Running hello-world.py')
# smooth is 1 and bumpy is 0 
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# apples are 0 and oranges are 1 
labels = [0, 0, 1, 1]
print('The inputs to the classifier (features): ' + str(features))
print('The output we want (labels): ' + str(labels))
# We will use a classifier implemented as a decision tree
from sklearn import tree
clf = tree.DecisionTreeClassifier()
# a learning algorithm creates classifiers
# it learns by finding patterns in the training data
# the function that 'finds-patterns-in-data' is called 'fit'
clf = clf.fit(features, labels)

for i in range(50, 180, 10):
	for j in range(0, 2):
		if j == 0:
			texture = "bumpy"
		else:
			texture = "smooth"
		print("Predicting grams: " + str(i) + " and texture: " + texture)
		p = clf.predict([[i, j]])
		if p == 0:
			print("apple")
		else: 
			print("orange")
