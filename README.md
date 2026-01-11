1. Container Advantage:
Problem: When students work across Windows, macOS, and Linux systems, inconsistencies in Java versions, HAPI FHIR dependencies, and PostgreSQL configurations frequently result in “dependency hell.”
Solution: Docker standardises the entire technology stack with a single command that works identically across all machines.
Result: Every team member gets the identical production environment running instantly.
Port mapping bridges the isolated Docker container to access on localhost.

2. Semantic Integrity:
Problem: Converting legacy CSV data to proper FHIR codes when these mappings are scattered throughout Python code creates a maintenance nightmare.
Solution: FHIR Shorthand (FSH) profiles, combined with Concept Maps, ensure that all codes are validated at the server level, not hardcoded in application logic.
Result: The server itself validates and converts correctly to business rules live in the FHIR server, not scattered application code. 

3. Transactional Atomicity: No Orphaned Data
Problem: Creating a Patient first and Observations later can fail halfway, leaving orphaned clinical data with no patient reference.
Solution: Using FHIR transaction bundles with temporary UUIDs, Patients and their Observations are submitted together as a single operation.
Result: One request creates everything—or nothing at all. The FHIR server guarantees atomicity, preserving full referential and clinical integrity.
