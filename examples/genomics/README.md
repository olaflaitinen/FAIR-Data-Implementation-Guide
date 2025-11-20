# Genomics Data Example

This directory contains an example of a FAIR-compliant genomics dataset description.

## Dataset Overview

- **Title**: RNA-Seq analysis of drug-resistant bacteria
- **Type**: Transcriptomics
- **Format**: FASTQ (raw), BAM (aligned), CSV (counts)

## Files

- `metadata.json`: Complete metadata description in JSON-LD format.
- `sample_attributes.csv`: Detailed sample information.
- `protocol.md`: Step-by-step library preparation and sequencing protocol.

## FAIR Implementation

### Findable
- Assigned DOI: `10.5281/zenodo.example`
- Keywords: `RNA-Seq`, `Bacteria`, `Drug Resistance`, `Transcriptomics`

### Accessible
- Data available via HTTPS.
- Metadata accessible publicly; raw data requires request due to size.

### Interoperable
- Metadata uses Schema.org and NCBI Taxonomy terms.
- Gene IDs mapped to Ensembl Bacteria.

### Reusable
- License: CC-BY 4.0
- Detailed provenance in `protocol.md`.
