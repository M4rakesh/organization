import json
import datetime

dalibnieki=[]
def load_data():
    file=open('dalibnieki.json','r')
    data=json.load(file)
    file.close()
    global dalibnieki
    dalibnieki=data['dalibnieki']
    print("Dati ir ievaditi")


def add_organization():

    d_name=input('Name: ')
    d_adress=input('Adress: ')
    d_id=input('Id: ')
    d_tel=input('Tālr.')


    dalibnieks={
        'name':d_name,
        'adress':d_adress,
        'id':d_id,
        'talr':d_tel,
        'contacts': []
        }
    while (True):
        response=input("Vai vēlaties pieteikties apmeklejumam?(y/n) ")
        if response=='y':
            laik_s=input("Cik ilgs apmeklējums: ")
            dvieli=int(input("Dvieļi (viena dvieļa maksa 50 centi): "))
            apm_id=input("Apmekletaja id: ")
            datums=print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            if dvieli>=0:
                a=0.5
                d=dvieli*a
                print(f"dvieļu noma maksa būs:{d}")

                contact={
                'laiks':laik_s,
                'Dvieli':dvieli,
                'id':apm_id,
                'date': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                }
            dalibnieks['contacts'].append(contact)
        elif response=='n':
            break
    dalibnieki.append(dalibnieks)
def print_organization():
    print("dfh")
    for dalibnieks in dalibnieki:
            print('DALĪBNIEKS:')
            print(f"ID:{dalibnieks['id']}")
            print(f"{dalibnieks['name']} {dalibnieks['talr']} {dalibnieks['adress']}")
def save_data():
    data={
            'dalibnieki':dalibnieki
        }
    print("Saving data...")
    try:

        file = open('dalibnieki.json','w')
        json.dump(data,file,indent=4,ensure_ascii=False)
    except FileNotFoundError:
        print('gftfdf')

def find_organization_by_id():
    dalibnieki_id=input('Ievadiet darbnieka  ID: ')
    for dalibnieks in dalibnieki:
        if dalibnieks['id']== dalibnieki_id:
            print('DALĪBNIEKS:')
            print(f"{dalibnieks['name']} ({dalibnieks['id']})")
            
            while (True):
                response=input("Vai vēlaties pieteikties apmeklejumam?(y/n) ")
                if response=='y':
                        laik_s=input("Cik ilgs apmeklējums: ")
                        dvieli=int(input("Dvieļi (viena dvieļa maksa 50 centi): "))
                        apm_id=input("Apmekletaja id: ")
                        datums=print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                        if dvieli>=0:
                            a=0.5
                            d=dvieli*a
                            print(f"dvieļu noma maksa būs:{d}")

                            contact={
                                'laiks':laik_s,
                                'Dvieli':dvieli,
                                'id':apm_id,
                                'date': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                            }
                        dalibnieks['contacts'].append(contact)
                elif response=='n':
                    break
def count_organizations():
    print(f"Org sk ir {len()}")
def list_organition_ids():
    for i in dalibnieki:
        print('\n'+i['id'])
def organization_exists():
    a=input("Ievadiet id la iparbaudit vai tas jau ir: ")
    for dalibnieki in a:
        if ['id'] == a:
            return True
def delete_organization_by_id():
    b=input('Ievadiet organizācijas ID: ')
    for dalbnieki in dalibnieki:
        if dalibnieki['id']== b:
            dalibnieki.remove()
            
            break
        
def main():
    load_data()
    find_organization_by_id()
    #count_organizations()
    #organization_exists()
    #list_organition_ids()
    #delete_organization_by_id()
    while (True):
        response=input('(1)Pievieno apmeklētāju (2) Izprinte apmeklētāja datus (3)Iziet (4)atjaunot datus ')
        if response=='1':
            add_organization()
        elif response=='2':
            print_organization()
        elif response=='3':
            save_data()
            print('gg,ja livaju tima rakov!')
            exit()
        elif response=='4':
            find_organization_by_id()
            save_data()
            print('gg,ja livaju tima rakov!')
            
        else:
            print('Choose a number between 1 and 4')
            continue
main()