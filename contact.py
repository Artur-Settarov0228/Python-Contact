from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact(contacts, name):
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Topildi:", contact)
            found = True
            break
    if not found:
        print("Kontakt topilmadi.")

            
    

def delete_contact(contacts):
    delete_name = input("O'chirmoqchi bo'lgan kontakt (nomi, familyasi, raqami): ").strip().lower()
    for contact in contacts:
        if contact['first_name'].lower() == delete_name or contact['last_name'].lower() == delete_name or contact['phone'].lower() == delete_name:
            contacts.remove(contact)
            print("Kontakt o'chirildi!")
        else:
            print("Bunday kontakt topilmadi.")

    def update_contact():
        update_name = input("Yangilamoqchi bo'lgan kontakt ismi: ").strip().lower()
    found = False

    for contact in contacts:
        if contact['first_name'].lower() == update_name:
            print("Hozirgi ma'lumotlar:"),
            f"{contact['first_name']} {contact['last_name']} | {contact['phone']} | {contact['group']}"

            # Ism
            while True:
                new_first_name = input(f"Yangi ism ({contact['first_name']}): ")
                if new_first_name == "":
                    new_first_name = contact['first_name']
                    break
                elif not new_first_name.isalpha():
                    print("Xato ism!", "red")
                else:
                    break

            # Familya
            while True:
                new_last_name = input(f"Yangi familya ({contact['last_name']}): ")
                if new_last_name == "":
                    new_last_name = contact['last_name']
                    break
                elif not new_last_name.isalpha():
                    print("Xato familya!")
                else:
                    break

            # Telefon
            while True:
                new_phone = input(f"Yangi raqam ({contact['phone']}): ")
                if new_phone == "":
                    new_phone = contact['phone']
                    break
                elif not new_phone.isdigit():
                    print("Faqat raqam kiriting!", "red")
                else:
                    break

            # Guruh
            while True:
                group_input = input("== Yangi guruh tanlang ==\n1. Oila\n2. Do'stlar\n3. Ish\n4. Boshqalar\n")
                if group_input == "":
                    new_group = contact['group']
                    break
                elif group_input == "1":
                    new_group = "Oila"
                    break
                elif group_input == "2":
                    new_group = "Do'stlar"
                    break
                elif group_input == "3":
                    new_group = "Ish"
                    break
                elif group_input == "4":
                    new_group = "Boshqalar"
                    break
                else:
                    print(colored("Xato tanlov", "red"))

            
    

