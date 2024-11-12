organizations=[]
organizations_a={
    'name':'Tesla',
    'adress':'Tesla ave 1,USA',
    'id':'8646678',
    'contacts':[
        {
            'name':'Dainis',
            'position':'CTO'
            id=1
            'name':'Jāzeps',
            'position':'CSA'
            id=2
        }
    ]
}

organizations_b={
    'name':'Audi',
    'adress':'Allroad,USA',
    'id':'864348'
    'contacts':[
        {
            'name':'Dainiki',
            'position':'df'
            id=1
            'name':'Raviki',
            'position':'sdfg'
            id=2
            }
            ]
}
for organization in organizations:
    print('---ORGANISATION---')
    print(f"{organization['name']}({organization['id']})")
    print(f"Adrese:{organization['adress']}")
    print(f"Kontaktu skaits: {len(organization['contacts'])}") 
organizations.append(organizations_a)
organizations.append(organizations_b)
print(organizations)