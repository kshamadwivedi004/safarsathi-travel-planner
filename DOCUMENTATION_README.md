# SafarSathi Documentation Generator

This directory contains the automated documentation generation system for the SafarSathi project.

## Overview

The documentation generator automatically creates:
1. **Project Synopsis Document** (Word format - .docx) following academic synopsis guidelines
2. **Project Presentation** (PowerPoint format - .pptx) for presentations

## Requirements

Install the required packages for document generation:

```bash
pip install -r requirements_docs.txt
```

Or manually install:
```bash
pip install python-docx python-pptx
```

## Usage

### Generate Both Documents

To generate both the synopsis document and PowerPoint presentation:

```bash
python generate_synopsis.py
```

This will create:
- `SafarSathi_Project_Synopsis.docx` - Complete project synopsis with proper formatting
- `SafarSathi_Project_Presentation.pptx` - Professional PowerPoint presentation

### After Making Changes to Your Project

Whenever you make changes to the SafarSathi application:

1. Update the relevant code in [`app.py`](app.py:1)
2. Run the documentation generator to update both files:
   ```bash
   python generate_synopsis.py
   ```

The generator will automatically:
- Read your current project structure
- Extract features and functionality
- Create updated documentation with current date
- Maintain proper formatting and structure

## Synopsis Document Structure

The generated synopsis follows the required format:

1. **Title Page**
   - Project name and title
   - Submission date

2. **Index**
   - Contents listing with page numbers

3. **Introduction** (up to 3 pages)
   - Project overview
   - Technology description
   - Key features
   - Technology stack
   - Target audience

4. **Feasibility Study** (up to 2 pages)
   - Technical feasibility
   - Economic feasibility
   - Need and significance

5. **Methodology / Planning of Work** (up to 2 pages)
   - Development phases
   - Implementation steps
   - Testing approach

6. **Facilities Required** (up to 1 page)
   - Hardware requirements
   - Software requirements
   - API requirements

## Presentation Structure

The PowerPoint presentation includes:

1. Title Slide
2. Project Overview
3. Key Features
4. Technology Stack
5. System Architecture
6. Feasibility Study
7. Development Methodology
8. User Interface Highlights
9. Implementation Details
10. Facilities Required
11. Benefits & Advantages
12. Future Enhancements
13. Thank You Slide

## Formatting Specifications

### Synopsis Document
- **Font:** Times New Roman, 12pt
- **Page Size:** A4
- **Margins:** 
  - Left: 3.5 cm
  - Top: 2.5 cm
  - Right: 1.25 cm
  - Bottom: 1.25 cm
- **Line Spacing:** 1.5
- **Binding:** Spiral Binding (as specified)

### Presentation
- **Slide Size:** Standard (10" x 7.5")
- **Theme:** Purple gradient (matching SafarSathi brand)
- **Font Sizes:** 
  - Titles: 24-28pt
  - Content: 16-22pt

## Customization

To customize the documentation:

1. Open [`generate_synopsis.py`](generate_synopsis.py:1)
2. Modify the relevant methods:
   - `add_introduction()` - Update introduction content
   - `add_features_slide()` - Add/modify features
   - `add_technology_slide()` - Update technology stack
3. Run the generator to create updated documents

## Auto-Update System

The current implementation allows manual regeneration. For automatic updates on code changes, you can:

1. **Manual Approach** (Current):
   - Run `python generate_synopsis.py` after making changes
   - Simple and reliable

2. **Automated Approach** (Future Enhancement):
   - Set up file watchers using `watchdog` library
   - Automatically regenerate on code changes
   - Integrate with CI/CD pipeline

## Tips for Maintaining Documentation

1. **Regular Updates**: Regenerate documents after major feature additions
2. **Version Control**: Commit generated documents to track changes over time
3. **Review**: Always review generated documents before submission/presentation
4. **Customization**: Update the generator script to reflect your latest features
5. **Screenshots**: Consider adding screenshots to presentations manually for better visual appeal

## Files

- [`generate_synopsis.py`](generate_synopsis.py:1) - Main generator script
- [`requirements_docs.txt`](requirements_docs.txt:1) - Required packages for documentation
- `SafarSathi_Project_Synopsis.docx` - Generated synopsis document
- `SafarSathi_Project_Presentation.pptx` - Generated presentation

## Troubleshooting

### Import Errors
If you get import errors, ensure you've installed the required packages:
```bash
pip install python-docx python-pptx
```

### Font Issues
If Times New Roman is not available on your system, the default font will be used. Install the font or modify the generator script to use an available font.

### Page Breaks
Page breaks might vary based on content length. Adjust content in the generator script if needed.

## Support

For issues or questions about the documentation system:
1. Check the generated files for formatting
2. Review the generator script comments
3. Refer to python-docx and python-pptx documentation

## License

This documentation generator is part of the SafarSathi project and follows the same license.
