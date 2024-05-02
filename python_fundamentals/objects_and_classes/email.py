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


emails = []
command = input()

while command != "Stop":
    entry = command.split()
    sender = entry[0]
    receiver = entry[1]
    content = entry[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

indecies = [int(index) for index in input().split(', ')]
for index in indecies:
    emails[index].send()
for current_email in emails:
    print(current_email.get_info())
