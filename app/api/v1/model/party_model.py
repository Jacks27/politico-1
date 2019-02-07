parties_list=[]

class PartyModel():
    """ parent class for party model"""
    def __init__(self):
        self.party = parties_list

    def save(self, name, hqAdress, logoUrl):
        party = {         
            'party_id':len(self.party)+1,
            'name':name,
            'hqAddress': hqAdress,
            'logoUrl': logoUrl 
        }
        self.party.append(party)
        return party

    def get_All_Parties(self):
        return self.party

    def get_Party(self, party_id):
        if self.party:
            for party_n in self.party:
                if party_n.get('party_id') == party_id:
                    return party_n           
                
            
                    
    def remove_party(self, party_id):
        if self.party:
            for party_n in self.party:
                if party_n.get('party_id') == party_id:
                    self.party.remove(party_n)
                    return True
        
        return False

    def update_party(self, party_id):
        if self.party:
            for party_n in self.party:
                if party_n.get('party_id') == party_id:
                    return party_n
        
                   
                         


