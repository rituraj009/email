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
