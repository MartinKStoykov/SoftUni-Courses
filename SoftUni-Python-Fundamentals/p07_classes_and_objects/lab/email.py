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
    elements = command.split(" ")
    sender = elements[0]
    receiver = elements[1]
    content = elements[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

indexes = input().split(", ")
for num in indexes:
    index = int(num)
    emails[index].send()
for email in emails:
    print(email.get_info())