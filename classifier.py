from pprint import pprint
import random
from nltk import NaiveBayesClassifier
from nltk.classify.util import accuracy
from sklearn.model_selection import KFold
from training_set_util import load_training_set
from ml_util import extract_bigrams

categories = {1: 'Wanted', 2: 'Unwanted'}

def bag_of_words(words):
    return dict([(word, True) for word in words])

def create_training_dict(text, category):
    tokens = extract_bigrams(text)
    return [(bag_of_words(tokens), category)]

def classify(text, sender=None, subject=None):
    training_set = load_training_set()
    classifier = NaiveBayesClassifier.train(training_set)
    test_data = bag_of_words(extract_bigrams(text))
    if sender is not None:
        test_data[sender] = True
    if subject is not None:
        test_data[subject] = True
    classified = classifier.prob_classify(test_data)
    classified_labels = {categories.get(sample, 'Unknown'): classified.prob(sample) for sample in classified.samples()}
    pprint(classified_labels)
    return categories.get(classified.max(), 'Unknown')

def cross_validate():
    training_set = load_training_set()
    random.shuffle(training_set)
    average = 0
    cv = KFold(n_splits=10, shuffle=False, random_state=None)
    for traincv, evalcv in cv.split(training_set):
        classifier = NaiveBayesClassifier.train(training_set[traincv[0]:traincv[-1]])
        acc = accuracy(classifier, training_set[evalcv[0]:evalcv[-1]])
        print('Range: ', evalcv[0], 'to', evalcv[-1])
        print('Accuracy: %4.2f' % acc)
        average += acc
    print('Average accuracy: %4.2f' % (average / 10))
