class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mails = []
command = input()
while not command == "Stop":
    [s, r, c] = command.split()
    emails = Email(s, r, c)
    mails.append(emails)
    command = input()

mails_to_be_sent = [int(i) for i in input().split(', ')]

for i in mails_to_be_sent:
    mails[i].send()


for emails in mails:
    print(emails.get_info())
