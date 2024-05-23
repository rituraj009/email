import random
from pprint import pprint
import win32com.client
from classifier import classify, categories
from training_set_util import load_training_set, save_training_set, build_training_set_from_text

class OutlookLib:
    def __init__(self, settings=None):
        if not settings:
            settings = {}
        self.settings = settings

    def get_messages(self, user, folder="Inbox", match_field="all", match="all"):
        outlook = win32com.client.Dispatch("Outlook.Application")
        myfolder = outlook.GetNamespace("MAPI").Folders[user]
        inbox = myfolder.Folders[folder]  # Inbox
        if match_field == "all" and match == "all":
            return inbox.Items
        else:
            messages = []
            for msg in inbox.Items:
                try:
                    if match_field == "Sender":
                        if msg.SenderName.find(match) >= 0:
                            messages.append(msg)
                    elif match_field == "Subject":
                        if msg.Subject.find(match) >= 0:
                            messages.append(msg)
                    elif match_field == "Body":
                        if msg.Body.find(match) >= 0:
                            messages.append(msg)

                except:
                    pass
            return messages

    def get_body(self, msg):
        return msg.Body

    def get_subject(self, msg):
        return msg.Subject

    def get_sender(self, msg):
        return msg.SenderName

    def get_recipient(self, msg):
        return msg.To

    def get_attachments(self, msg):
        return msg.Attachments

def parse_and_classify_emails(num_emails):
    outlook = OutlookLib()
    messages = outlook.get_messages('riturajsingh695308@gmail.com')  # Replace with your actual email
    count = 0
    emails = []

    for message in messages:
        if count >= num_emails:
            break
        try:
            email_info = {
                'sender': message.SenderName,
                'receiver': message.To,
                'subject': message.Subject,
                'body': message.Body.replace('\r\n', ' ').replace('\n', ' ').replace('\t', ' ')
            }
        except AttributeError as e:
            print(f"Skipping email due to missing attribute: {e}")
            continue
        
        emails.append(email_info)
        count += 1

    classified_emails = []
    for index, email in enumerate(emails, 1):
        category = classify(email['body'], sender=email['sender'], subject=email['subject'])
        if category == 'Unknown':
            print(f"Email {index} has an unknown category, skipping")
            continue
        classified_emails.append((email, category))
        print(f"Email {index}")
        print(f"Subject: {email['subject']}")
        print(f"Classified Category: {category}")
        print()

    return classified_emails

def add_to_training_set(classified_emails):
    cached_training_set = []
    count = 0
    update_count = 0

    for email, category in classified_emails:
        inv_categories = {v: k for k, v in categories.items()}
        category = inv_categories[category] if category in inv_categories else None
        if category is None:
            print(f"Skipping email with subject '{email['subject']}' due to unknown category")
            continue
        temporary = build_training_set_from_text(text=email['body'], category=category, sender=email['sender'], subject=email['subject'])
        cached_training_set += temporary
        count += 1

        if count >= 2:
            training_set = load_training_set()
            training_set += cached_training_set
            save_training_set(training_set)
            update_count += 1
            count, cached_training_set = 0, []

    if count > 0:  # If there are any remaining emails that didn't trigger the count >= 2 condition
        training_set = load_training_set()
        training_set += cached_training_set
        save_training_set(training_set)
        update_count += 1

    print(f'Training set updated and persisted with new items: {update_count}')

if __name__ == "__main__":
    num_emails = int(input("Enter the number of emails to parse: "))
    classified_emails = parse_and_classify_emails(num_emails)
    add_to_training_set(classified_emails)
