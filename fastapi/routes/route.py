from pymongo import MongoClient
from models.infos import Rec
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_infos():
    infos=list_serial(collection_name.find())  
    return infos

@router.post("/")
async def post_info(info: Rec):
    # Ouvrir le fichier et lire son contenu en binaire
    

    # Insérer le contenu du fichier dans la base de données
    document = {
        "firstName": info.firstName,
        "lastName": info.lastName,
        "cin": info.cin,
       
    }
    collection_name.insert_one(document)
    return {"message": "Les informations ont été enregistrées avec succès."}