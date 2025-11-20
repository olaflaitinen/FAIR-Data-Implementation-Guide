# Clinical Trial Data Example

This directory demonstrates how to make clinical trial data FAIR while respecting patient privacy.

## Dataset Overview

- **Title**: Randomized Control Trial of Drug X for Hypertension
- **Type**: Clinical Data
- **Format**: CSV (de-identified)

## Files

- `data_dictionary.csv`: Definitions of all variables.
- `consent_form_template.pdf`: Blank copy of the patient consent form.
- `access_protocol.md`: Instructions for requesting access to the full dataset.

## FAIR Implementation

### Findable
- Registered in ClinicalTrials.gov (NCT00000000).
- Metadata indexed in Google Dataset Search.

### Accessible
- Summary statistics available for download.
- Individual Participant Data (IPD) available via secure enclave after DUA signature.

### Interoperable
- Variables mapped to CDISC standards.
- Disease terms mapped to SNOMED CT.

### Reusable
- Clear data usage agreement (DUA) provided.
- Analysis code provided in R.
