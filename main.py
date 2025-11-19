class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Message:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.baza = []


    def add_contact(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        contact = Contact(name, phone)
        self.baza.append(contact)
        print("Contact added")

    def view_contact(self):
        for contact in self.baza:
            print(contact.name, contact.phone)

    def send_message(self):
        phone = input("Enter phone number that you want to send msg: ")
        for contact in self.baza:
            if contact.phone==phone:
                message = input("Enter your message: ")
                self.message = message
                self.name = contact.name
                print("Message sent successfully")
            else:
                print("Phone number not found")


    def view_message(self):
        for contact in self.baza:
            print(" To",self.name, "=>", self.message)

    def delete_message(self):
        for contact in self.baza:
            phone = input("Enter phone number that you want to delete msg: ")
            if contact.phone == phone:
                self.name.pop()
                self.message.pop()
                print("Message deleted successfully")
            else:
                print("You don't have any message")

mes = Message("dfjn", "dfsljfn")
def main(message: Message):
    while True:
        kod = input(" 1. Add contacts \n 2. Send messages \n 3. Delete messages \n 4. View contacts \n 5. View messages \n 6. Exit ")
        if kod == "1":
            message.add_contact()
        elif kod == "2":
            message.send_message()
        elif kod == "3":
            message.delete_message()
        elif kod == "4":
            message.view_contact()
        elif kod == "5":
            message.view_message()
        elif kod == "6":
            break
        else:
            print("Invalid command")

main(mes)
