# Contributing to FAIR Data Implementation Guide

Thank you for your interest in contributing to the FAIR Data Implementation Guide. This document provides guidelines for contributing to this repository.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Process](#contribution-process)
- [Style Guidelines](#style-guidelines)
- [Documentation Standards](#documentation-standards)
- [Quality Assurance](#quality-assurance)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### Reporting Issues

- Use the GitHub issue tracker to report bugs, suggest enhancements, or request new features
- Before creating an issue, search existing issues to avoid duplicates
- Provide clear, descriptive titles and detailed descriptions
- Include relevant context such as your use case, domain, or specific requirements

### Suggesting Enhancements

- Submit enhancement suggestions as GitHub issues with the "enhancement" label
- Clearly describe the proposed enhancement and its benefits
- Provide examples or use cases where applicable
- Consider backwards compatibility and impact on existing users

### Contributing Documentation

- Improve existing documentation for clarity and accuracy
- Add missing documentation for undocumented features
- Create new guides, case studies, or examples
- Fix typos, grammatical errors, or formatting issues

### Contributing Code

- Submit new templates for different data types or domains
- Develop validation scripts and automation tools
- Improve existing scripts for better performance or functionality
- Add test coverage for validation tools

### Contributing Templates

- Contribute metadata templates for additional standards
- Provide data management plan templates for specific funders or institutions
- Submit domain-specific documentation templates

### Contributing Case Studies

- Share real-world implementations (anonymized as needed)
- Document lessons learned and best practices
- Provide complete examples with metadata and documentation

## Getting Started

1. **Fork the Repository**: Create a personal fork of the repository on GitHub

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/your-username/FAIR-Data-Implementation-Guide.git
   cd FAIR-Data-Implementation-Guide
   ```

3. **Create a Branch**: Create a feature branch for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**: Implement your contribution following the style guidelines

5. **Test Your Changes**: Validate that templates are well-formed and scripts execute correctly

6. **Commit Your Changes**: Write clear, concise commit messages
   ```bash
   git commit -m "Add: Brief description of changes"
   ```

7. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request**: Open a pull request from your fork to the main repository

## Contribution Process

### Pull Request Guidelines

- Provide a clear title and description of your changes
- Reference any related issues using keywords (e.g., "Fixes #123" or "Addresses #456")
- Ensure all files follow the repository's structure and organization
- Update relevant documentation to reflect your changes
- Ensure your code or templates are well-commented and documented

### Review Process

- All contributions will be reviewed by maintainers
- Reviewers may request changes or clarifications
- Address review feedback promptly and professionally
- Once approved, maintainers will merge your contribution

### Acceptance Criteria

Contributions will be accepted if they:

- Align with the repository's purpose and scope
- Follow established style and documentation guidelines
- Are well-tested and validated
- Do not introduce breaking changes without justification
- Include appropriate documentation

## Style Guidelines

### Documentation Style

- Use clear, professional, academic language
- Avoid emojis, informal language, or colloquialisms
- Write in active voice where possible
- Use proper grammar, spelling, and punctuation
- Structure documents with clear headings and sections
- Include a table of contents for longer documents

### Markdown Formatting

- Use standard Markdown syntax
- Format code blocks with appropriate language identifiers
- Use tables for structured information
- Include links to referenced documents and resources
- Ensure proper indentation for nested lists

### File Naming Conventions

- Use lowercase with hyphens for file names: `example-file-name.md`
- Use descriptive names that clearly indicate content
- Maintain consistent naming patterns within directories

### Template Standards

- Include comprehensive comments explaining each field
- Provide example values where appropriate
- Follow established metadata standards (Dublin Core, DCAT, Schema.org)
- Validate JSON, XML, and other structured formats for correctness

### Code Standards

- Write clean, readable, well-commented code
- Follow PEP 8 for Python scripts
- Include docstrings for all functions and classes
- Provide usage examples in comments or separate documentation
- Handle errors gracefully with informative messages

## Documentation Standards

### Structure Requirements

All documentation should include:

- Clear title and purpose statement
- Table of contents (for documents longer than one page)
- Logically organized sections with descriptive headings
- References to related documents and external resources
- Examples demonstrating key concepts
- Date of last update

### Content Requirements

- Begin with an introduction explaining the document's purpose
- Define technical terms or link to the glossary
- Provide step-by-step instructions where applicable
- Include concrete examples from life sciences domains
- Cite authoritative sources for principles and standards
- Conclude with next steps or related resources

### Academic Rigor

- Cite original sources for FAIR principles and related concepts
- Reference peer-reviewed literature where applicable
- Provide DOIs or persistent URLs for citations
- Maintain factual accuracy and current information
- Distinguish between requirements and recommendations

## Quality Assurance

### Before Submitting

- Validate all JSON and XML files for syntax correctness
- Test Python scripts for basic functionality
- Check all internal links to ensure they work
- Proofread documentation for spelling and grammar
- Ensure no emojis or informal language is present
- Verify that changes align with repository standards

### Validation Tools

Use the validation scripts in `scripts/validation/` to check:

- Metadata template correctness
- FAIR compliance of examples
- Link integrity in documentation

### Testing Guidelines

For code contributions:

- Include test cases demonstrating functionality
- Document expected inputs and outputs
- Test edge cases and error conditions
- Ensure compatibility with Python 3.7+

## Questions?

If you have questions about contributing, please:

- Review existing documentation in the `docs/` directory
- Search closed issues for similar questions
- Open a new issue with the "question" label
- Contact repository maintainers

## Recognition

Contributors will be acknowledged in the repository. Significant contributions may warrant co-authorship in academic citations.

Thank you for helping make scientific data more FAIR!
