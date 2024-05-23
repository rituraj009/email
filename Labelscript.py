import os
import random

def add_label_to_emails(directory):
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a text file
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Generate a random label (1 or 2)
            label = random.choice([1, 2])

            # Add the label at the top of the file content
            new_content = '{}\n{}'.format(label, content)

            # Write the new content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f'Added label {label} to {filename}')

# Specify the absolute path to the directory containing the email text files
email_dataset_directory = r'C:\Users\wwwri\OneDrive\Desktop\Sarajuni\email\email_dataset'

# Call the function to add labels to all email files
add_label_to_emails(email_dataset_directory)







- 
- the first part is Collecting dataset
- so using python script we will be parsing emails from resulting folders and downloading them in text files,
- text files will contain details like

—> sender’s name

—> receiver’s name

—> subject

—> body

- For an effective dataset collection, we are taking mails from test and filtered folders which have “wanted” and “unwanted” mails respectively. and then download them in text format, and finally run a script to label them.
- By this, our dataset is ready for the next stage which is preprocessing.

## **Feature extraction**

The goal of feature extraction is to convert raw text data into a format that a ML model can understand and learn from.

**Process**:

1. **Text Preprocessing**:
    - **Remove Stopwords**: First, we remove common words like "the", "and", "is", which don't carry much meaning on their own.
    - **Tokenization**: Then, we break down the text into individual words or tokens.

1. **Filtering Tokens**:
    - We filter out any tokens that are not useful for our analysis. For example, we might remove numbers or special characters that don't convey meaningful information.

These features then help our model learn to distinguish between different types of emails, like sorting them into "wanted" or "unwanted" categories.

## **Email Classifier Construction**

- The Naive Bayes classifier is used to train on the extracted features.

Classification Stage

1. Loads the trained classifier.
2. Extracts features from the input text.
3. Classifies the text based on these features.
4. finds the probabilities for each class and returns the class with the highest probability.

after these 

## **The best part of this implementation,**

After the classification of new emails, these emails will be added to the training dataset for improving the classification, therefore with each classification of email, it will increase its classification accuracy. 

It supports, a crucial aspect of machine learning known as "online learning" or "incremental learning. In this approach, the model learns continuously as new data becomes available, and it adapts its predictions accordingly.
