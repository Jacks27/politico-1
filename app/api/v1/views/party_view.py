from flask import Flask, Blueprint, request, make_response, jsonify
import json
from app.api.v1.model.party_model import PartyModel, parties_list

my_v1= Blueprint('v1',__name__, url_prefix='/api/v1')

class Party:
  
    @my_v1.route('/parties', methods =['POST'])
    def post():
        """ function for posting data """
        data = request.get_json()
        name = data['name']
        hqAdress = data['hqAdress']
        logoUrl = data['logoUrl']
        new_pty=PartyModel().save(name, hqAdress, logoUrl)
        return make_response(jsonify({
            'msg':"Success"
        }), 201)

    @my_v1.route('/all_paties', methods=['GET'])
    def get_all_p():
        """return all parties """
        parties= PartyModel().get_All_Parties()
        return make_response(jsonify({
                    "msg":"Ok",
                    'party': parties        
        }))

    @my_v1.route('/get_party/<int:party_id>', methods=['GET'])
    def get_Party(party_id):
        party=PartyModel().get_Party(party_id)
        if party:
            return make_response(jsonify({
                'message':'Ok',
                'Party':party
            }), 200)
        else:
            return make_response(jsonify({
                'message':'Error no such party'
            }))
    @my_v1.route('/remove_party/<int:party_id>', methods=['DELETE'])
    def remove_party(party_id):
        party=PartyModel().remove_party(party_id)
        if party:
            return make_response(jsonify({
                'message':'Ok',
            }), 200)
        else:
            return make_response(jsonify({
                'message':'Error party could not be deleted'
            }))

    @my_v1.route('/update_party/<int:party_id>', methods = ['PATCH'])
    def Update_party(party_id):
        for party in parties_list:
            if party['party_id'] == party_id:
                data = request.get_json()
                party['name'] = data['name']
                return make_response(jsonify({
                    'msg':"Success"
                }), 200)

                update_party = {
                    new_name['name']: data['name']
                }
                parties_list.append(update_party)
                return make_response(jsonify({
                    "status": 200,
                    'success': "updated party {}".format(update_party)
                }))
        




