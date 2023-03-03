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
data_input = input()

while data_input != "Stop":
    data_input = data_input.split()
    email = Email(data_input[0], data_input[1], data_input[2])
    emails.append(email)
    data_input = input()

indexes = [int(x) for x in input().split(", ")]

for i, email in enumerate(emails):
    if i in indexes:
        emails[i].send()
    print(email.get_info())

    # print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")
