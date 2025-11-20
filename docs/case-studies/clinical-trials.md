# Case Study: FAIR Clinical Trial Data

## Background
A multi-center clinical trial collected data on 500 patients. The data contained sensitive personal information (PII) and protected health information (PHI).

## The Challenge
How to make the data FAIR without compromising patient privacy or violating GDPR/HIPAA regulations.

## The Solution

### Step 1: De-identification
- Removed direct identifiers (names, IDs).
- Shifted dates and generalized ages (e.g., "80+" instead of "82").

### Step 2: Metadata Publication (F, A2)
- Created a detailed metadata record describing the study design, population, and variables.
- Published this metadata on a public repository with a DOI.
- **Crucially**: The metadata clearly stated that the *data* is controlled access.

### Step 3: Controlled Access (A1.2)
- Set up a Data Access Committee (DAC).
- Implemented a request process:
    1. Researcher submits proposal.
    2. DAC reviews proposal.
    3. Researcher signs Data Use Agreement (DUA).
    4. Secure download link generated.

### Step 4: Interoperability (I)
- Used CDISC SDTM standards for variable names.
- Mapped adverse events to MedDRA terminology.

## Outcome
The trial data was successfully reused by three independent groups for secondary analysis, maximizing the value of the participants' contribution while maintaining strict privacy standards.
