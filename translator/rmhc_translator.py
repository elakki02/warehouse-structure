!pip install fhir.resources requests

import csv
import uuid
import json
import requests
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.bundle import Bundle

LOCAL_SERVER_URL = "http://localhost:8080/fhir"  # Your Docker HAPI

def translate_and_send_rmhc(csv_data):
    reader = csv.DictReader(csv_data.splitlines())
    for row in reader:
        temp_uuid = f"urn:uuid:{uuid.uuid4()}"
        
        patient = Patient({
            "resourceType": "Patient",
            "identifier": [{"system": "http://rmhc.org/sid/policy-id", "value": row['policy_id']}],
            "name": [{"text": row['Name']}],
            "gender": {"F": "female", "M": "male"}.get(row['Sex'], "unknown")
        })
        
        fbs_obs = Observation({
            "resourceType": "Observation",
            "status": "final",
            "code": {"coding": [{"system": "http://loinc.org", "code": "1558-6", "display": "Fasting glucose"}]},
            "subject": {"reference": temp_uuid},
            "valueQuantity": {
                "value": float(row['FBS']) if row['FBS'] != '#N/A' else None,
                "unit": "mg/dL", "system": "http://unitsofmeasure.org", "code": "mg/dL"
            }
        })
        
        bundle = Bundle({
            "resourceType": "Bundle", "type": "transaction",
            "entry": [
                {"fullUrl": temp_uuid, "resource": patient.dict(), "request": {"method": "POST", "url": "Patient"}},
                {"resource": fbs_obs.dict(), "request": {"method": "POST", "url": "Observation"}}
            ]
        })
        
        resp = requests.post(LOCAL_SERVER_URL, json=bundle.dict())
        print(f"Patient {row['policy_id']}: {resp.status_code}")

# Sample data
rmhc_csv = """policy_id,Name,Sex,FBS
AND0010888,Patient1,F,159
AND0012586,Patient2,M,205.6"""
translate_and_send_rmhc(rmhc_csv)
