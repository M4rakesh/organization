import json


organizations=[]
def load_data():
    file=open('organizations.json','r')
    data=json.load(file)
    file.close()
    global organizations
    organizations=data['organizations']
    print("Dati ir ievaditi")

def add_organization():

    organization_name=input('Oganization name: ')
    organization_adress=input('Organization adress: ')
    organization_id=input('Organization id: ')

    organization={
        'name':organization_name,
        'adress':organization_adress,
        'id':organization_id,
        'contacts': []
        }
    while (True):
        response=input("Do you want to add a contact(y/n) ")
        if response=='y':
            contact_name=input("Contact name: ")
            contact_position=input("Contact position: ")
            contact_id=input("Contact id: ")
            contact={
                'name':contact_name,
                'position':contact_position,
                'id':contact_id,
                }
            organization['contacts'].append(contact)
        elif response=='n':
            break
    organizations.append(organization)
def print_organization():
    for organization in organizations:
            print('---ORGANISATION---')
            print(f"{organization['name']}({organization['id']})")
            print(f"Adrese:{organization['adress']}")
            print(f"Kontaktu skaits: {len(organization['contacts'])}")
def save_data():
    data={
            'organizations':organizations
        }
    print("Saving data...")
    try:

        file = open('organizations.json','w')
        json.dump(data,file,indent=4)
    except FileNotFoundError:
        print('gftfdf')

def find_organization_by_id():
    organizations_id=input('Ievadiet organizācijas ID: ')
    for organization in organizations:
        if organization['id']== organizations_id:
            print('---ORGANIZACIJA---')
            print(f"{organization['name']}({organization['id']})")
            break
def count_organizations():
    print(f"Org sk ir {len(organizations)}")
def list_organition_ids():
    for i in organizations:
        print('\n'+i['id'])
def organization_exists():
    a=input("Ievadiet id la iparbaudit vai tas jau ir: ")
    for organization in organizations:
        if organizations['id'] == a:
            return True
def delete_organization_by_id():
    b=input('Ievadiet organizācijas ID: ')
    for organization in organizations:
        if organization['id']== b:
            organization.remove(organizations)
            
            break
def main():
    load_data()
    #find_organization_by_id()
    #count_organizations()
    #organization_exists()
    #list_organition_ids()
    #delete_organization_by_id()
    while (True):
        response=input('(1)Add organization (2) Print organizations (3)Exit ')
        if response=='1':
            add_organization()
        elif response=='2':
            print_organization()
        elif response=='3':
            save_data()
            print('gg,ja livaju tima rakov!')
            exit()
        else:
            print('Choose a number between 1 and 3')
            continue
main()