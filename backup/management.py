from flask import request, jsonify
from flask_restful import Resource
from crud import nf_instance

class NFInstance_Document(Resource):
    def put(self, nfInstanceId):
        return nf_instance.create_nf_instance(nf_profile=request.get_json(), nfInstanceId= nfInstanceId)
        # putData = request.get_json()
        # with open("static/getdata.json", "w") as outfile:
        #     json.dump(putData, outfile)
        # collection = app.free5gc_db.nfprofile
        # collection.insert_one(putData)
    def get(self, nfInstanceId):
        nf_prf = nf_instance.get_nf_instance(nfInstanceId= nfInstanceId)
        if nf_prf != None:
            nf_prf["_id"] = str(nf_prf["_id"])
            return nf_prf
        return None
    #     get_nf = nf_instance.get_nf_instance("63c40ad249632cef052d4595")
    #     return jsonify(get_nf)
        # getData = []
        # nfprofile_collection = app.free5gc_db.nfprofile
        # nfpfs = nfprofile_collection.find()
        # for nfpf in nfpfs:
        #     with open("static/getdata.json", "w") as outfile:
        #         json.dump(nfpf["nfServices"][0]["ipEndPoints"][0]["ipv4Address"], outfile)
        #     break
        # return 200
    def delete(self, nfInstanceId):
        return nf_instance.delete_nf_instance(nfInstanceId= nfInstanceId)
