# Case Study: Proteomics Data Standardization

## Background
A proteomics core facility generated mass spectrometry data for various clients. The data was often delivered as proprietary vendor files.

## The Challenge
Proprietary formats locked the data into specific software ecosystems, hindering interoperability and long-term reuse (I1, A1.1).

## The Solution

### Step 1: Open Formats
- Converted all raw vendor files to `mzML`, an open, XML-based standard format developed by HUPO-PSI.

### Step 2: Metadata Standardization
- Adopted the MIAPE (Minimum Information About a Proteomics Experiment) guidelines.
- Documented instrument settings, peak picking parameters, and database search settings.

### Step 3: Public Repository
- Deposited data into PRIDE (Proteomics Identifications Database), a member of the ProteomeXchange consortium.

## Outcome
The data became part of the global proteome knowledge base. The use of open formats allowed bioinformaticians to develop new open-source tools for analyzing the data, which would have been impossible with proprietary files.
