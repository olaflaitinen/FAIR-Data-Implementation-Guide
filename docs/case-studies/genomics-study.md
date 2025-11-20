# Case Study: Making Genomics Data FAIR

## Background
A research group at University X generated RNA-Seq data from 100 bacterial samples to study antibiotic resistance. Initially, the data was stored on local hard drives with cryptic filenames like `sample1_final.fastq`.

## The Challenge
- **Findability**: No one outside the lab knew the data existed.
- **Accessibility**: Data could only be shared by mailing hard drives.
- **Interoperability**: Metadata was in a handwritten notebook.
- **Reusability**: No license was attached, and methods were undocumented.

## The Solution

### Step 1: Organization and Metadata (F2, R1)
- Renamed files using a consistent convention: `ProjectID_SampleID_Date_ReadDirection.fastq`.
- Created a `sample_metadata.csv` file listing Strain, Antibiotic, Concentration, and Date for each sample.

### Step 2: Standards and Vocabularies (I1, I2)
- Mapped antibiotic names to ChEBI identifiers.
- Used NCBI Taxonomy IDs for bacterial strains.

### Step 3: Repository Submission (F4, A1)
- Uploaded raw reads to the Sequence Read Archive (SRA).
- Uploaded processed count tables and code to Zenodo.

### Step 4: Identifiers and Linking (F1, F3, I3)
- SRA assigned an accession number (e.g., SRP123456).
- Zenodo assigned a DOI (e.g., 10.5281/zenodo.123456).
- The Zenodo record linked to the SRA accession.

## Outcome
The dataset was cited 15 times in the first year. Other researchers combined it with their own data to perform a meta-analysis, leading to a new discovery about resistance mechanisms.
