# Reusable: Optimizing for Future Use

The "Reusable" principle ensures that data is preserved in a way that allows it to be used in future research, potentially in contexts different from the original study. This is the ultimate goal of FAIR.

## R1. (Meta)data are richly described with a plurality of accurate and relevant attributes

### Principle Description
To reuse data, a researcher needs to trust it and understand exactly how it was generated. This requires extensive documentation beyond just discovery metadata.

### Implementation Guidelines
- **Detailed Methodology**: Describe experimental protocols, equipment, and software versions.
- **Variable Definitions**: Clearly define all variables, units of measurement, and allowable values.
- **Context**: Explain the scope and limitations of the data.

## R1.1. (Meta)data are released with a clear and accessible data usage license

### Principle Description
Users must know the legal conditions under which they can use the data. Ambiguity often leads to non-use.

### Implementation Guidelines
- **Standard Licenses**: Use standard licenses like Creative Commons (CC0, CC-BY, CC-BY-NC) or Open Data Commons.
- **Machine-Readable**: Include the license information in the metadata (e.g., `license: https://creativecommons.org/licenses/by/4.0/`).

### Examples
- **CC0 (Public Domain)**: No restrictions.
- **CC-BY (Attribution)**: Must cite the original author.

## R1.2. (Meta)data are associated with detailed provenance

### Principle Description
Provenance describes the history of the data: who created it, when, how, and what processing steps were applied.

### Implementation Guidelines
- **Workflow Documentation**: Record the analysis pipeline, including scripts and software versions.
- **Audit Trail**: Track changes and versions of the dataset.
- **Attribution**: List all contributors and their roles (e.g., using CRediT taxonomy).

## R1.3. (Meta)data meet domain-relevant community standards

### Principle Description
Different scientific communities have established standards for data sharing. Adhering to these ensures the data is useful to peers in that field.

### Implementation Guidelines
- **Community Standards**: Adopt standards like MIAME (Microarray), MINSEQE (Sequencing), or MIAPE (Proteomics).
- **Format Compliance**: Use file formats preferred by the community (e.g., FASTA/FASTQ for sequences, mzML for mass spec).

### Checklist for Reusability
- [ ] Is the data described with rich, accurate attributes?
- [ ] Is a clear license attached?
- [ ] Is the provenance (history) of the data documented?
- [ ] Does the data follow community standards?
