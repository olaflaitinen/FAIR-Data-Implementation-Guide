# Introduction to the Semantic Web for FAIR Data

The Semantic Web is a vision of the World Wide Web where data is machine-readable and linked, allowing computers to integrate and process information from different sources automatically. It provides the technological foundation for the "Interoperable" aspect of FAIR.

## Core Concepts

### 1. RDF (Resource Description Framework)
RDF is the standard data model for the Semantic Web. It represents information as "triples":
**Subject** -> **Predicate** -> **Object**

*Example:*
`Gene_X` (Subject) -> `encodes` (Predicate) -> `Protein_Y` (Object)

In a machine-readable format (Turtle):
```turtle
@prefix bio: <http://example.org/biology#> .
@prefix gene: <http://example.org/gene/> .
@prefix protein: <http://example.org/protein/> .

gene:BRCA1 bio:encodes protein:P38398 .
gene:BRCA1 bio:isAssociatedWith "Breast Cancer" .
```

### 2. URIs (Uniform Resource Identifiers)
Everything in the Semantic Web is identified by a URI. This ensures global uniqueness.
- Instead of "Gene X", we use `http://www.ncbi.nlm.nih.gov/gene/12345`.
- Instead of "encodes", we use `http://purl.obolibrary.org/obo/RO_0002205`.

### 3. Ontologies
Ontologies define the vocabulary (the predicates and classes) used in RDF. They provide the rules and relationships between concepts.
- **RDFS (RDF Schema)**: Defines classes and properties.
- **OWL (Web Ontology Language)**: Defines complex relationships (e.g., "A Human is a Mammal").

### 4. SPARQL
SPARQL is the query language for RDF data, similar to SQL for relational databases.

*Example Query: Find all proteins encoded by genes associated with Breast Cancer.*
```sparql
PREFIX bio: <http://example.org/biology#>

SELECT ?protein
WHERE {
  ?gene bio:isAssociatedWith "Breast Cancer" .
  ?gene bio:encodes ?protein .
}
```

## Why Use Semantic Web for FAIR?

1.  **Global Interoperability (I1, I2)**: Using URIs and standard ontologies means your data can be automatically merged with data from other labs without manual mapping.
2.  **Machine Reasoning**: Computers can infer new knowledge. If `Gene A` is a `Kinase`, and all `Kinases` are `Enzymes`, the computer knows `Gene A` is an `Enzyme`.
3.  **Linked Data (I3)**: You can link your data to the vast cloud of existing Linked Open Data (LOD), such as UniProt, ChEMBL, and Wikidata.

## Getting Started

1.  **Convert Data to RDF**: Use tools like [CSV2RDF](https://github.com/AtomGraph/CSV2RDF) to convert your spreadsheets.
2.  **Publish as Linked Data**: Host your RDF files or set up a "Triple Store" (graph database) like Blazegraph or Virtuoso.
3.  **Use JSON-LD**: A lightweight way to add semantic annotations to standard JSON files, widely used by Google and Schema.org.
