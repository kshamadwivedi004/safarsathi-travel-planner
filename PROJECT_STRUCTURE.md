# SafarSathi Project Structure

## 📁 Directory Structure

```
Safarsathi-main/
├── static/
│   └── styles.css                          # External CSS stylesheet
├── app.py                                  # Main Streamlit application
├── .env                                    # Environment variables (API keys)
├── requirements.txt                        # Application dependencies
├── requirements_docs.txt                   # Documentation generation dependencies
├── generate_synopsis.py                    # Documentation generator script
├── README.md                              # Project README
├── DOCUMENTATION_README.md                # Documentation system guide
├── QUICK_START_DOCS.md                    # Quick start guide
├── PROJECT_STRUCTURE.md                   # This file
├── Trip_Planner_AI.ipynb                  # Jupyter notebook (if applicable)
├── SafarSathi_Project_Synopsis.docx       # Generated synopsis document
└── SafarSathi_Project_Presentation.pptx   # Generated PowerPoint presentation
```

## 📝 File Descriptions

### Core Application Files

#### [`app.py`](app.py:1)
Main application file for the SafarSathi AI Travel Planner
- **Lines 1-20**: Imports and Streamlit page configuration
- **Lines 21-27**: CSS loading function (loads from [`static/styles.css`](static/styles.css:1))
- **Lines 197-212**: PlannerState TypedDict definition
- **Lines 213-232**: Session state initialization
- **Lines 234-244**: LLM initialization with caching
- **Lines 246-270**: Itinerary prompt template
- **Lines 272-297**: Itinerary creation function
- **Lines 299-308**: History saving function
- **Lines 310-669**: Main application logic with UI

**Key Features**:
- Streamlit-based web interface
- AI-powered itinerary generation using Groq API
- Budget planning and optimization
- Multiple export formats (TXT, MD, JSON)
- Trip history tracking
- External CSS loading for better organization

#### [`static/styles.css`](static/styles.css:1)
External CSS stylesheet for the application
- **Lines 1-3**: Font import (Poppins)
- **Lines 5-10**: Global styling
- **Lines 12-20**: Main app background gradients
- **Lines 22-173**: Component styling (buttons, cards, containers, etc.)
- **Lines 175-183**: Sidebar custom styling
- **Lines 185-194**: Tab styling

**Design Features**:
- Purple gradient theme (#667eea to #764ba2)
- Modern card-based layout
- Hover effects and transitions
- Responsive design
- White background for content areas

### Documentation System

#### [`generate_synopsis.py`](generate_synopsis.py:1)
Automated documentation generator
- **Lines 1-17**: Imports and encoding setup
- **Lines 19-838**: SafarSathiDocumentGenerator class
  - `create_synopsis_document()`: Generates Word document
  - `create_presentation()`: Generates PowerPoint presentation
  - Various helper methods for each section

**Usage**:
```bash
python generate_synopsis.py
```

#### [`DOCUMENTATION_README.md`](DOCUMENTATION_README.md:1)
Complete documentation system guide
- Overview of the documentation generator
- Detailed usage instructions
- Synopsis and presentation structure
- Customization guidelines
- Troubleshooting tips

#### [`QUICK_START_DOCS.md`](QUICK_START_DOCS.md:1)
Quick start guide for documentation
- Simple step-by-step instructions
- Format specifications
- Auto-update system explanation
- Tips and troubleshooting

### Configuration Files

#### [`.env`](.env:1)
Environment variables (not tracked in git)
```env
GROQ_API_KEY=your_api_key_here
```

#### [`requirements.txt`](requirements.txt:1)
Python dependencies for the application
- streamlit
- langchain, langchain-core, langchain-groq, langchain-community
- python-dotenv
- groq
- typing-extensions, pydantic

#### [`requirements_docs.txt`](requirements_docs.txt:1)
Dependencies for documentation generation
- python-docx (Word document generation)
- python-pptx (PowerPoint generation)

### Generated Documentation

#### `SafarSathi_Project_Synopsis.docx`
Professional synopsis document following academic format
- A4 size, Times New Roman 12pt
- Proper margins (3.5cm left, 2.5cm top, 1.25cm right/bottom)
- Contains: Title page, Index, Introduction, Feasibility Study, Methodology, Facilities Required

#### `SafarSathi_Project_Presentation.pptx`
Professional PowerPoint presentation
- 13 slides covering all project aspects
- Purple gradient theme matching app design
- Ready for project presentations

## 🔄 Recent Changes

### CSS Refactoring
The CSS has been extracted from inline styling in [`app.py`](app.py:1) to a separate file [`static/styles.css`](static/styles.css:1):

**Benefits**:
1. **Better Organization**: Separation of concerns between logic and styling
2. **Easier Maintenance**: Update styles without touching Python code
3. **Reusability**: CSS can be shared or referenced
4. **Cleaner Code**: Reduced clutter in main application file
5. **Professional Structure**: Follows web development best practices

### Update Process

To update styles:
1. Edit [`static/styles.css`](static/styles.css:1)
2. Refresh the Streamlit app (it will automatically reload CSS)

To update documentation:
1. Make changes to project code
2. Run `python generate_synopsis.py`
3. New documents will be generated with current date

## 💡 Best Practices

### Development
1. Keep API keys in `.env` file (never commit to git)
2. Update documentation after major changes
3. Test CSS changes in browser before committing
4. Use version control for all code changes

### Documentation
1. Regenerate synopsis before submission
2. Review generated documents for accuracy
3. Customize generator script for specific needs
4. Keep documentation in sync with code

### Deployment
1. Ensure `.env` file is configured on deployment platform
2. Verify `static/` directory is included in deployment
3. Test CSS loading on deployed instance
4. Check all file paths are relative

## 🚀 Quick Commands

```bash
# Run the application
streamlit run app.py

# Generate documentation
python generate_synopsis.py

# Install app dependencies
pip install -r requirements.txt

# Install doc generation dependencies
pip install -r requirements_docs.txt

# Install all dependencies
pip install -r requirements.txt -r requirements_docs.txt
```

## 📈 Future Improvements

- [ ] Add automatic documentation generation on code changes
- [ ] Implement CSS preprocessing (SASS/LESS)
- [ ] Add theme customization options
- [ ] Create additional documentation templates
- [ ] Add automated testing for UI components
- [ ] Implement CI/CD pipeline for documentation

## 🤝 Contributing

When contributing to this project:
1. Update relevant documentation
2. Follow existing code structure
3. Test both application and documentation generation
4. Update this structure document if adding new files
5. Ensure CSS changes are compatible across browsers

## 📞 Support

For questions about the project structure:
- Review this document
- Check [`DOCUMENTATION_README.md`](DOCUMENTATION_README.md:1) for documentation specifics
- See [`QUICK_START_DOCS.md`](QUICK_START_DOCS.md:1) for quick references
- Refer to inline comments in source files
