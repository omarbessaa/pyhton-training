'''
the main conception 
'''
import json

class Company() :
    def __init__(self , company_name , company_price) :
        self.name = company_name
        self.price = company_price

    def __repr__ (self) :
        return 'company : {} , its price is {}'.format(self.name , self.price)

    def to_json(self) :
        return "{}".format(self.price)
        # if we need to add others options to our companies we can modify the format

class Stock_market() :
    # add a new company to the database
    @classmethod
    def add_company(cls, company_name , company_price):
        c = Company(company_name , company_price)
        # load the database file 
        with open('companies.json') as f :
            companies = json.load(f)
            
        # add the company
        companies[c.name] = c.to_json()

        with open('companies.json', 'w') as f :
            json.dump(companies , f)

        return "{{ {} : {} }}".format(company_name ,company_price)

    @classmethod
    def get_companies(cls) :
        with open('companies.json') as f :
            companies = json.load(f)
        
        return companies

    @classmethod
    def get_company(cls, company_name) :
        with open('companies.json') as f :
            companies = json.load(f)
        
        try :
            company_info = companies[company_name]
        except KeyError :
            return None
        else :
            return "{{ {} : {} }}".format(company_name ,company_info)

    @classmethod
    def delete_company(cls , company_name) :
        with open('companies.json') as f :
            companies = json.load(f)
        
        try :
            company_info = companies.pop(company_name)
        except KeyError :
            return None
        else :
            with open('companies.json', 'w') as f :
                json.dump(companies , f)
            
            return "{{ {} : {} }}".format(company_name ,company_info)
    
    @classmethod
    def update_company(cls , company_name , new_company_price) :
        with open('companies.json') as f :
            companies = json.load(f)
        
        if company_name in companies.keys() :
            companies[company_name] = new_company_price
            
            with open('companies.json', 'w') as f :
                json.dump(companies , f)
            
            return "{{ {} : {} }}".format(company_name , new_company_price)    
        else :
            return None
        