import pickle
import io
from os import getcwd, listdir

from ml_util import strip_signature, extract_bigrams


def get_feature(word):
    return dict([(word, True)])


def build_training_set(path='../email_dataset'):
    training_set = []
    files = listdir(path)
    for email_file in files:
        with io.open('{}/{}'.format(path, email_file), 'r', encoding='utf8') as email:
            print(f'Parsing file: {email_file}')
            category, sender, receiver, subject = int(
                email.readline().strip()), email.readline().strip(), email.readline().strip(), email.readline().strip()
            print(f'Training set updated with: [{subject}]')
            text = email.read()
            text = strip_signature(text, sender)
            features = extract_bigrams(text)
            training_set = training_set + [(get_feature(word), category) for word in features]
            training_set = training_set + [({sender: True}, category), ({subject: True}, category)]
    return training_set


def build_training_set_from_text(text, category, sender=None, subject=None):
    text = strip_signature(text, sender)
    features = extract_bigrams(text)
    training_set = []
    training_set = training_set + [(get_feature(word), category) for word in features]
    training_set = training_set + [({sender: True}, category), ({subject: True}, category)]
    return training_set


def save_training_set(training_set, file_name='/training_sets/outlook_training_data.pickle'):
    with open(getcwd() + file_name, 'wb') as f:
        pickle.dump(training_set, f)


def load_training_set(file_name='/training_sets/outlook_training_data.pickle'):
    with open(getcwd() + file_name, 'rb') as f:  # Fixed mode to 'rb'
        data = pickle.load(f)
    return data
