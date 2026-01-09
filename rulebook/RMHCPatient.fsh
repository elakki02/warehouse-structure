Profile: RMHCPatient
Parent: Patient
Id: rmhc-patient
Title: "RMHC Andipatti Patient Profile"
Description: "Profile for demographic and health records from RMHC Andipatti."

// Mandatory Name and Gender according to RMHC data requirements
* name 1..* MS
* gender 1..1 MS

// Slicing for policy_id (e.g., AND0010888)
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains RMHC_ID 1..1 MS
* identifier[RMHC_ID].system = "http://rmhc.org/sid/policy-id"
* identifier[RMHC_ID].value 1..1 MS

// Mapping Location/GPS data using standard extensions
* extension contains http://hl7.org/fhir/StructureDefinition/geolocation named geolocation 0..1 MS

// Constraints on Address and Contact No.
* address MS
* telecom MS
