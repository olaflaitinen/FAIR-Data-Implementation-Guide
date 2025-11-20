# Ontology Development and Selection Guide

Ontologies are critical for FAIR data (Principle I2). They provide the shared vocabulary that makes data interoperable. This guide explains how to select existing ontologies and, if absolutely necessary, how to create your own.

## Part 1: Selecting an Ontology (Don't Reinvent the Wheel!)

**Rule #1**: Always look for an existing ontology before creating a new one.

### Where to Search
1.  **BioPortal**: [https://bioportal.bioontology.org/](https://bioportal.bioontology.org/) - The largest repository of biomedical ontologies.
2.  **OLS (Ontology Lookup Service)**: [https://www.ebi.ac.uk/ols/index](https://www.ebi.ac.uk/ols/index) - EBI's search service.
3.  **Fairsharing.org**: Search for standards recommended by your community.

### Selection Criteria
- **Coverage**: Does it cover the terms you need?
- **Maintenance**: Is it actively maintained? Check the last update date.
- **Community Use**: Is it widely used in your field? (e.g., GO for gene function, DOID for diseases).
- **Format**: Is it available in standard formats (OWL, OBO)?

### Common Ontologies in Life Sciences
- **Gene Ontology (GO)**: Molecular function, biological process, cellular component.
- **Human Phenotype Ontology (HPO)**: Phenotypic abnormalities.
- **Chemical Entities of Biological Interest (ChEBI)**: Small chemical compounds.
- **NCBI Taxonomy**: Organism names and classification.
- **Uberon**: Anatomy.

## Part 2: Creating an Application Ontology

If you cannot find an ontology that fits your needs, you may need to create a small "application ontology" that extends existing ones.

### Tools
- **Protégé**: [https://protege.stanford.edu/](https://protege.stanford.edu/) - The standard desktop tool for editing OWL ontologies.
- **Robot**: [http://robot.obolibrary.org/](http://robot.obolibrary.org/) - Command-line tool for automating ontology workflows.

### Best Practices
1.  **Reuse Terms**: Import terms from existing ontologies (e.g., using MIREOT) rather than recreating them.
2.  **Define Classes**: Create a hierarchy. `Specific_Term` is_a `General_Term`.
3.  **Add Metadata**: Give every term a clear definition, label, and unique ID.
4.  **Use BFO**: Align your ontology with the Basic Formal Ontology (BFO) top-level structure for maximum interoperability.

### Example: Defining a New Term
If you are studying a specific "Lab Protocol X", define it as:
- **Label**: Lab Protocol X
- **ID**: MYONTO:0000001
- **Parent**: `protocol` (from OBI - Ontology for Biomedical Investigations)
- **Definition**: "A protocol for extracting DNA from..."

## Part 3: Mapping Terms

If you have legacy data with free-text labels, you need to map them to ontology IDs.
- **Zooma**: [https://www.ebi.ac.uk/spot/zooma/](https://www.ebi.ac.uk/spot/zooma/) - Automated mapping tool from EBI.
- **Manual Curation**: Use spreadsheets to map "Heart Attack" -> `DOID:10763` (Myocardial Infarction).
