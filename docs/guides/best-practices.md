# Best Practices for FAIR Data Implementation

This guide outlines recommended practices for institutions and research groups implementing FAIR principles.

## 1. Planning and Policy

### Develop a Data Policy
Institutions should have a clear policy requiring data management plans (DMPs) for all research projects. The policy should define ownership, retention periods, and funding for data stewardship.

### Budget for Data Management
FAIR data is not free. Include line items in grant proposals for:
- Data storage costs
- Repository deposition fees
- Personnel time (data curators, stewards)

## 2. Data Organization

### Consistent Naming Conventions
Adopt a standard file naming convention across the lab or organization.
- **Bad**: `final_data.csv`, `test.xls`
- **Good**: `2025-01-20_ProjectA_Experiment1_RawCounts.csv`

### Folder Structure
Organize data logically.
```
Project/
  ├── data/
  │   ├── raw/
  │   └── processed/
  ├── metadata/
  ├── scripts/
  └── results/
```

## 3. Metadata and Documentation

### Automate Metadata Collection
Don't rely on human memory. Use electronic lab notebooks (ELNs) or LIMS to capture metadata automatically at the point of data generation.

### Use Controlled Vocabularies
Avoid free-text fields for critical attributes. Use dropdowns or autocomplete fields linked to ontologies (e.g., NCBI Taxonomy, EFO).

## 4. Storage and Backup

### The 3-2-1 Rule
- **3** copies of the data
- **2** different media types (e.g., local server + cloud)
- **1** copy off-site

### Version Control
Use version control (git) for code and documentation. For data, use versioned datasets in repositories (e.g., Zenodo allows versioning).

## 5. Publication and Sharing

### Choose the Right Repository
Prioritize domain-specific repositories (e.g., GEO for genomics) over generalist ones (e.g., Figshare). They offer better metadata validation and discoverability.

### Publish Early
Consider publishing "data papers" or preprints to get credit for the dataset itself, independent of the main research findings.
