# Accessible: Ensuring Data Availability

The "Accessible" principle ensures that once a user has found the required data, they know how to access it, possibly including authentication and authorization. Note that "Accessible" does not imply "Open"; data can be FAIR even if it is private or requires permission to access.

## A1. (Meta)data are retrievable by their identifier using a standardized communications protocol

### Principle Description
Users should be able to retrieve the data or metadata using the identifier assigned in F1, via a standard protocol.

### Implementation Guidelines
- **Standard Protocols**: Use widely adopted protocols like HTTP, HTTPS, or FTP.
- **Direct Resolution**: The identifier (e.g., DOI) should resolve to the location of the data or a landing page.

### Examples
- Clicking a DOI link (`https://doi.org/...`) redirects the browser via HTTPS to the dataset landing page.
- Using a REST API to retrieve metadata via an HTTP GET request.

## A1.1 The protocol is open, free, and universally implementable

### Principle Description
The communication protocol should not be proprietary or require specialized, paid software to implement.

### Implementation Guidelines
- **Avoid Proprietary Protocols**: Do not use protocols that require purchasing a license.
- **Global Standards**: Stick to IETF or W3C standards (e.g., HTTP, FTP, SMTP).

## A1.2 The protocol allows for an authentication and authorization procedure, where necessary

### Principle Description
For sensitive data (e.g., patient records), access may need to be restricted. The protocol must support mechanisms for verifying identity and permissions.

### Implementation Guidelines
- **Authentication**: Verify who the user is (e.g., OAuth, API keys, login systems).
- **Authorization**: Verify what the user is allowed to do (e.g., read-only, download, edit).
- **Defined Process**: Clearly document how a user can request access.

### Use Case: Clinical Data
A dataset containing patient genomic data is discoverable (Findable) through public metadata. However, downloading the raw data (Accessible) requires the user to log in and sign a Data Use Agreement.

## A2. Metadata are accessible, even when the data are no longer available

### Principle Description
Data may be deleted or lost over time, or may be too expensive to maintain. However, the metadata describing the data should persist indefinitely to support historical record-keeping and citation.

### Implementation Guidelines
- **Tombstone Pages**: If a dataset is removed, the PID should resolve to a "tombstone" page explaining that the data is gone but displaying the original metadata.
- **Archival Policy**: Repositories should have a clear policy on metadata retention.

### Checklist for Accessibility
- [ ] Can the data be retrieved via a standard protocol (HTTP/HTTPS)?
- [ ] Is the protocol free and open?
- [ ] If access is restricted, is the authentication process clearly documented?
- [ ] Will metadata remain available if the data is deleted?
