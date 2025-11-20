# Findable: The First Step in FAIR Data

The "Findable" principle ensures that data and metadata can be easily discovered by both humans and computer systems. This is the foundational step in the FAIR process, as data that cannot be found cannot be reused.

## F1. (Meta)data are assigned a globally unique and persistent identifier

### Principle Description
Every data element and its associated metadata must be assigned a globally unique and persistent identifier (PID). This ensures that the data can be unambiguously referenced over time, even if its location changes.

### Implementation Guidelines
- **Use Standard PIDs**: Utilize established identifier systems such as DOIs (Digital Object Identifiers), Handles, or URIs (Uniform Resource Identifiers).
- **Uniqueness**: Ensure the identifier is unique within the global scope, not just locally.
- **Persistence**: The organization assigning the identifier must commit to maintaining it indefinitely.

### Examples
- **DOI**: `10.5281/zenodo.1234567`
- **ORCID**: `0000-0002-1825-0097` (for researchers)
- **RRID**: `RRID:CVCL_0063` (for cell lines)

## F2. Data are described with rich metadata

### Principle Description
Metadata should be extensive enough to allow a user (human or machine) to understand the nature of the data and assess its relevance. "Rich" implies that the metadata goes beyond basic fields like title and author.

### Implementation Guidelines
- **Descriptive Attributes**: Include details about experimental conditions, parameters, variables, and units.
- **Contextual Information**: Provide information about the project, funding, and related publications.
- **Quality Metrics**: Include data quality indicators and validation results.

### Examples
- **Basic Metadata**: Title, Author, Date.
- **Rich Metadata**: Title, Author, Date, Abstract, Keywords, Methodology, Instrument Settings, Sample Characteristics, License, File Format.

## F3. Metadata clearly and explicitly include the identifier of the data it describes

### Principle Description
The metadata record must contain the PID of the data object it describes. This creates an explicit link between the description and the actual data.

### Implementation Guidelines
- **Explicit Linking**: Ensure the metadata file contains a field specifically for the data's PID.
- **Reciprocal Linking**: Ideally, the data file (if self-describing) should also reference its metadata PID.

### Example (JSON-LD)
```json
{
  "@context": "http://schema.org/",
  "@type": "Dataset",
  "identifier": "https://doi.org/10.5281/zenodo.1234567",
  "name": "Gene Expression Dataset",
  "description": "..."
}
```

## F4. (Meta)data are registered or indexed in a searchable resource

### Principle Description
Data and metadata should be included in search engines or catalogs that allow users to query and discover them.

### Implementation Guidelines
- **Repository Selection**: Deposit data in recognized domain-specific or generalist repositories (e.g., GenBank, UniProt, Zenodo, Dryad).
- **SEO for Data**: Ensure landing pages use structured data (like Schema.org) to be indexed by Google Dataset Search.

### Checklist for Findability
- [ ] Is a persistent identifier assigned?
- [ ] Is the metadata comprehensive?
- [ ] Does the metadata link to the data PID?
- [ ] Is the dataset indexed in a searchable repository?
