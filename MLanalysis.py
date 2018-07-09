from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import numpy as np

# Load files
seeds = np.loadtxt('seeds.txt', dtype=int)
counts = np.loadtxt('counts.txt', dtype=int).reshape(-1, 1)
wins = np.loadtxt('wins.txt', dtype=int)

# Split data into 80% training and 20% test data
seeds_train = seeds[:80]
counts_train = counts[:80]
wins_train = wins[:80]

seeds_test = seeds[80:]
counts_test = counts[80:]
wins_test = wins[80:]

# Compare classifiers

names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]


# print score for each method

for i in range(len(classifiers)):
    classifiers[i].fit(seeds_train, wins_train)
    print('%s :' % names[i] + str(classifiers[i].score(seeds_test, wins_test)))

