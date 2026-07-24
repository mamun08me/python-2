'''
Mamun-01723111627
Arif-01711223344
Sakib-01819556677
Tamim-01912334455
Mushfiq-01515667788
Riyad-01312345678
Shanto-01411223344
Taskin-01616778899
Fizz-01715998877
Liton-01812334455
Soumya-01911223344
Mehidy-01512334455
Taijul-01311223344
Ebadot-01412334455
Shoriful-01612334455
Towhid-01712345678
Tanzim-01815667788
Rishad-01915667788
Jaker-01511223344
Hasan-01315667788'''

'''
List
tuple 
set 
Dictionary '''

contacts=[
    {
        "name": "Mamun",
        "phone": "01723111627"
    },
     
    {
        "name": "Arif",
        "phone": "01711223344"
    },
    {
        "name": "Sakib",
        "phone": "01819556677"
    },
    {
        "name": "Tamim",
        "phone": "01912334455"
    },
    {
        "name": "Mushfiq",
        "phone": "01515667788"
    },
    {
        "name": "Riyad",
        "phone": "01312345678"
    },
    {
        "name": "Shanto",
        "phone": "01411223344"
    },
    {
        "name": "Taskin",
        "phone": "01616778899"
    },
    {
        "name": "Fizz",
        "phone": "01715998877"
    },
    {
        "name": "Liton",
        "phone": "01812334455"
    },
    {
        "name": "Soumya",
        "phone": "01911223344"
    },
    {
        "name": "Mehidy",
        "phone": "01512334455"
    },
    {
        "name": "Taijul",
        "phone": "01311223344"
    },
    {
        "name": "Ebadot",
        "phone": "01412334455"
    },
    {
        "name": "Shoriful",
        "phone": "01612334455"
    },
    {
        "name": "Towhid",
        "phone": "01712345678"
    },
    {
        "name": "Tanzim",
        "phone": "01815667788"
    },
    {
        "name": "Rishad",
        "phone": "01915667788"
    },
    {
        "name": "Jaker",
        "phone": "01511223344"
    },
    {
        "name": "Hasan",
        "phone": "01315667788"
    }
        
]

for i in range(len(contacts)):
    print(f"{i+1}.{contacts[i]["name"]}:{contacts[i]["phone"]}")