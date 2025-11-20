# Interoperable: Integrating Data Across Systems

The "Interoperable" principle focuses on the ability of data to be integrated with other datasets and used by various applications or workflows for analysis, storage, and processing.

## I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation

### Principle Description
Data and metadata should be represented using a formal language that machines can parse and interpret. This avoids ambiguity and enables automated processing.

### Implementation Guidelines
- **Standard Formats**: Use established data formats like JSON-LD, RDF, XML, or HDF5.
- **Knowledge Representation**: Use ontologies or controlled vocabularies to define concepts.

### Examples
- **Bad**: A text file with "Gender: M".
- **Good**: An RDF triple using a defined ontology: `<subject> <http://schema.org/gender> <http://schema.org/Male>`.

## I2. (Meta)data use vocabularies that follow FAIR principles

### Principle Description
The vocabularies, ontologies, or thesauri used to describe the data must themselves be FAIR (Findable, Accessible, Interoperable, Reusable).

### Implementation Guidelines
- **Resolvable Terms**: Terms in the vocabulary should have unique, resolvable identifiers (URIs).
- **Documentation**: The vocabulary should be documented and accessible.

### Recommended Vocabularies
- **General**: Schema.org, Dublin Core.
- **Life Sciences**: Gene Ontology (GO), Chemical Entities of Biological Interest (ChEBI), Human Phenotype Ontology (HPO).

## I3. (Meta)data include qualified references to other (meta)data

### Principle Description
Data often relates to other data. These relationships should be explicitly defined using qualified references (links with meaning).

### Implementation Guidelines
- **Cross-Referencing**: Link to related datasets, publications, or samples using their PIDs.
- **Typed Links**: Specify the nature of the relationship (e.g., "isDerivedFrom", "citations", "isPartOf").

### Example
A processed genomics dataset should link back to the raw reads dataset:
```json
{
  "name": "Processed Gene Counts",
  "isBasedOn": "https://doi.org/10.5281/zenodo.raw_reads_id"
}
```

### Checklist for Interoperability
- [ ] Is the data in a standard, machine-readable format?
- [ ] Are controlled vocabularies or ontologies used?
- [ ] Are the vocabularies themselves FAIR?
- [ ] Are links to related resources explicit and qualified?
