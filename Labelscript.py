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


Subject: My Journey through the Campus Grad GBS Hackathon
Dear Team,
I am excited to share my journey through the Campus Grad GBS Hackathon, where our team emerged in the top 3 (we were first!). I hope this story inspires you as much as it has inspired me.
The Campus Grad GBS Hackathon
The first invitation mail sent by GBS Innovation Council was on March 6th. This invitation was for campus grads who joined in 2023, and it was the first-ever GBS Campus Grads Innovation Hackathon. Registrations launched from March 12th. We were provided with a survey link and a list of problem statements, initially 23, which got cut down to 17.
Over 120 campus graduates registered for the event and ideated on 17 problem statements in the areas of:
	1. Carbon efficient green engineering
	2. Digital Customer experience
	3. Risk, security, and fraud prevention
We were given the choice to select two problem statements we were interested in working on, but for execution, we would be assigned one project to ensure an even distribution of team members across the problem statements. I chose Green Mailbox and Synthetic Data Generator.
On April 2nd, I got to know I was assigned to the Green Mailbox project. Along with me, there were 9 more members assigned to the project. As we were 10 members for the same project, we were split into two teams, each containing 5 members. I was aligned to team 1. We were provided with a detailed problem statement and team details. The team included the idea (project idea) owner - Ram, GDL SPOC Praveen Yedluri, Project managers Sreeram Raghavan, Hamsa Lakshmi, and Vinothkumar Babu, and two mentors Sahiti Challa and Vishnu Priya. We were told to subscribe to this project in OpenTap as well to get documented there. Team members were given 2-3 days to raise an ARM ticket for access, and finally, as a team, we started the project on April 8th.
We scheduled regular meetings within the team to collate ideas on how to approach the project. We came up with a tech stack and a rough flow of how to approach the project. We raised requests from MyTechnology for the software/sandbox, etc., required to implement the project. Meetings with the mentors and project manager happened once a week to show our progress, get constant feedback, suggestions, and corrections if we were going wrong somewhere. We were asked to create a private repository in Bitbucket and made every team member an admin so everyone could work on the code.

From the day we started to the day we concluded the hackathon, our project evolved tremendously. Initially, it resembled a college project, but through continuous refinement, it transformed into a robust solution, the best we could do considering the amount of time given. We explored every aspect of the project comprehensively, not just for the sake of completing it, but to perfect it.
We were meticulous about the dataset we used, ensuring we only worked with the corpus of mails generic to everyone and not project/application specific. We sticked strictly to the bank's guidelines, utilizing only the libraries and tools approved for use, as confirmed through our artifacts. Every step was taken with caution and compliance in mind.
we were also tasked with creating a detailed PPT. This presentation included the problem statement, our proposed solution, and, most importantly, its impact on the business. We highlighted how our project, falling under the green engineering category, contributes to sustainable practices.
We incorporated CO2e data from legitimate sources to demonstrate the effectiveness of our model in promoting green engineering and reducing the carbon footprint. We ensured our vision and long-term goals for the project were clear, emphasizing its alignment with environmental sustainability.

First Evaluation
The first evaluation presentation happened on May 23rd with cross GDL SPOCS, including Sandeep K Chauhan and Rustum Anwar. The presentation was evaluated on the following metrics:
	1. Business Impact
	2. Idea feasibility
	3. Creativity/Overall Presentation
	4. What thought process was put into this idea
	5. Team efforts put in
The results of the 1st evaluation came on May 30th. Out of 19 cohorts, our team 1 and team 2 for the same project got selected in the top 6. After that, we were given the option to either combine the teams (team 1 and team 2) into one and make the case stronger or put them separately as we did in the 1st evaluation. After discussion with team 2 and mentors, we decided to merge.
Hackathon Sprints
So overall, the hackathon happened in two sprints:
	• Sprint 1: Solution design and execution (April 8 to May 14) - 17 projects - 21 cohorts - 120 grads - 33 SME mentors
	• Sprint 2: GDL Innovation SPOCS evaluation - 6 projects - 9 cohorts - 40 grads
The top 6 ideas were:
	1. Book Your Parking Spot in One Click
	2. Bot for Onboarding New Resources
	3. Database Space Forecaster
	4. Synthetic Data Generator
	5. Access Classification System for Toxic Access Identification
	6. Green Mailbox
	
Dry Run and Final Presentation
On June 17th, the dry run session happened. We got to see the other top 6 ideas (9 cohorts). Every campus grad gave their best in the presentation. Every idea was unique and the best in its own way. I realized other people had done very interesting things, and something we could also learn.

 We got a little nervous but kept our calm, believed in ourselves, and presented our presentation. We were given 15 minutes to present the PPT and demo, followed by questions. We were not allowed to go over the time limit we had.
The major feedback we got was to focus on three things: the take-off (how impactful the idea is, they suggested having a funny intro to get everyone's attention), the landing (how it's impacting the business, to show it via metrics if possible), and the demo. They also suggested recording the demo using the PPT record option and keeping that at the end of the slide to save time. Since we were not allowed to go beyond the time limit we had, the demo associate was asked to present the whole PPT, and we had two presenters to avoid confusion and minimal handover of the PPT.
Finally, the final presentation happened on June 19th. It went great. We presented to senior leadership, including Mangesh Chore, Ramakrishnan Venkatachalam, Gaurav Mongia, Suchishree Chatterjee, and Jagadish Reddy. We got to hear from each one of them about how excited they were, their suggestions/feedback, and appreciations. It was a great day.

I would like to specially thank my teammates specially, Lalasa and Nisha. Can't thank them enough. We three were consistent throughout the journey and helped each other.
I made some friends too!!!

Key Learnings
	1. One major takeaway was that even very small things matter. The hackathon was not just about the code, demo, or technical aspects; it included every aspect that could be covered. Each line or word in our presentation needed to be precise and backed by clear sources, explaining how and why it was relevant.
	2. Confidence in presenting 
	3. Approach to the solution is one thing, but being prepared to address every aspect surrounding it is crucial.
	4. What ,How, Why- making these questions your best friend. Since they are asked every time 
	5. It was not at all about the end product or high technology we use, it was about what change this idea will bring into the business. 
	6. Learned to work in a team(Prepare to network), Know what you can offer in a team, Set your expectations(Do some homework)
	7.  Learn how to pitch an idea, practice your pitch.
	
	
It was a transformative experience for me. Hackathons aren't just about coding and tech, they're about collaboration and learning from each other, which is pretty awesome if you ask me.
Needless to say, Hackathons can change your perspective towards coding, for good. Period.


Best regards,
[Your Name]
