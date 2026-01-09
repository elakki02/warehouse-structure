Profile: RMHCObservation
Parent: Observation
Id: rmhc-observation
Title: "RMHC Clinical Observation Profile"
Description: "Profile for clinical metrics like Fasting Blood Sugar, BMI, and Weight."

* status = #final
* subject 1..1 MS
* subject only Reference(RMHCPatient) // Link back to the RMHC Patient profile
* code MS
* valueQuantity 0..1 MS
* valueQuantity.unit MS
* valueQuantity.system = "http://unitsofmeasure.org"
