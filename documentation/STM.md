# Source-to-Target Mapping (STM) - RMHC CSV → FHIR

## Mapping Overview
**Source**: RMHC Legacy CSV  
**Target**: FHIR R4 (Patient + Observation)  
**Date**: Jan 2026

## Patient Resource Mapping
| Source CSV Column | FHIR Element | Cardinality | Transformation Rule | Notes |
|-------------------|--------------|-------------|-------------------|-------|
| `policy_id` (e.g., AND0010888) | Patient.identifier[RMHC_ID].value | 1..1 | Direct copy | System: http://rmhc.org/sid/policy-id |
| `Name` | Patient.name[0].text | 1..1 | Direct copy | Human-readable name |
| `Sex` (F/M) | Patient.gender | 1..1 | F→"female", M→"male" | FHIR code mapping |
| `address` (if exists) | Patient.address | 0..* | Direct copy | Street, city, etc. |

## Observation Resource Mapping (FBS)
| Source CSV Column | FHIR Element | Cardinality | Transformation Rule | Notes |
|-------------------|--------------|-------------|-------------------|-------|
| `policy_id` | Observation.subject.reference | 1..1 | temp UUID linking to Patient | Transaction bundle |
| `FBS` | Observation.valueQuantity.value | 0..1 | float(FBS) if not '#N/A' | Fasting Blood Sugar |
| `FBS` | Observation.valueQuantity.unit | 1..1 | "mg/dL" | Fixed unit |
| Static | Observation.code.coding | 1..1 | LOINC:1558-6 "Fasting glucose" | http://loinc.org |
| Static | Observation.status | 1..1 | "final" | Clinical status |

## Sample RMHC CSV → FHIR
