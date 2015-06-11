__author__ = 'Iosu'


from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier as OvsA


def classifier_randomForest(features, labels):
    print "Training the random forest..."

    # Initialize a Random Forest classifier with 100 trees
    forest = RandomForestClassifier(n_estimators = 100)

    # Fit the forest to the training set, using the bag of words as
    # features and the sentiment labels as the response variable

    forest = forest.fit(features, labels)

    return forest


def classifier_svm(features, labels):

    clf = svm.LinearSVC()
    clf.fit(features, labels)

    return clf


def onevsall(tweets_features, train_labels):
    clf = OvsA.OneVsRestClassifier(svm.LinearSVC(random_state=0))
    OvsA.fit(tweets_features, train_labels)

    return clf