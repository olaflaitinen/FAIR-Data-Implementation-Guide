# FAIR Data Exercises

These exercises are designed to help you understand and apply FAIR principles.

## Exercise 1: The "Un-FAIR" Dataset
**Scenario**: You receive a USB drive from a retired colleague containing a folder named `Project_X_Final`. Inside, there is a file called `data.xls`.

**Task**: Open the file (mockup below) and identify 5 violations of FAIR principles.

| Col1 | Col2 | Col3 | Col4 |
|------|------|------|------|
| 1    | 0.5  | M    | ?    |
| 2    | 0.8  | F    | yes  |
| 3    | 1.2  | M    | no   |

**Answer Key**:
1. **F2 (Metadata)**: No column headers explaining what the data is.
2. **I1 (Format)**: `.xls` is a proprietary binary format (better: `.csv`).
3. **R1 (Context)**: No units for Col2.
4. **R1 (Context)**: "M/F" and "yes/no" are undefined codes.
5. **F1 (PID)**: No persistent identifier for the dataset.

---

## Exercise 2: Create a PID
**Scenario**: You have a dataset ready for publication. You want to reserve a DOI before the paper is accepted.

**Task**:
1. Go to [Zenodo Sandbox](https://sandbox.zenodo.org/).
2. Create an account (or log in with GitHub).
3. Click "New Upload".
4. Upload a dummy text file.
5. Fill in the required metadata fields (Title, Author, Description).
6. Save the record (do not publish yet).
7. **Question**: What is the DOI reserved for your upload?

---

## Exercise 3: Select an Ontology
**Scenario**: You are describing a dataset of bacterial infections. You have a column for "Organism".

**Task**:
1. Go to [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).
2. Search for "Escherichia coli".
3. Find the term in the "NCBI Taxonomy" ontology.
4. **Question**: What is the ID for *Escherichia coli*?
   - *Hint: It should look like `NCBITaxon:562`.*
5. **Question**: Why is using `NCBITaxon:562` better than just typing "E. coli"?

---

## Exercise 4: Write a Readme
**Scenario**: You have a folder with 10 images (`img01.tif` to `img10.tif`) of cells treated with Drug A.

**Task**: Write a `README.txt` file for this folder. Include:
- Project Title
- Date of experiment
- Description of the images (what microscope? what magnification?)
- Description of the treatment (Drug A concentration?)
- File naming convention explanation

---

## Exercise 5: License Picker
**Scenario**: You want to share your data so anyone can use it, but you want them to give you credit. You do not want them to sell your data.

**Task**:
1. Go to [Creative Commons Chooser](https://chooser-beta.creativecommons.org/).
2. Select "Yes" for "Do you want attribution?".
3. Select "No" for "Allow commercial uses?".
4. **Question**: Which license should you use?
   - *Answer: CC BY-NC 4.0*
