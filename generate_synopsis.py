# -*- coding: utf-8 -*-
"""
SafarSathi Project Synopsis and PPT Generator
This script automatically generates a Word document (.docx) and PowerPoint presentation (.pptx)
for the SafarSathi project following the specified synopsis format.
"""
import sys
import io

# Set UTF-8 encoding for console output
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pptx import Presentation
from pptx.util import Inches, Pt as PptPt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor as PptRGBColor
import datetime

class SafarSathiDocumentGenerator:
    def __init__(self):
        self.project_name = "SafarSathi - AI Travel Planner"
        self.current_date = datetime.datetime.now().strftime("%B %Y")
        
    def create_synopsis_document(self):
        """Generate the synopsis document in Word format"""
        doc = Document()
        
        # Set page margins: 3.5cm left, 2.5cm top, 1.25cm right and bottom
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(2.5)
            section.bottom_margin = Cm(1.25)
            section.left_margin = Cm(3.5)
            section.right_margin = Cm(1.25)
        
        # Set default font to Times New Roman
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)
        
        # Title Page
        self.add_title_page(doc)
        doc.add_page_break()
        
        # Index
        self.add_index(doc)
        doc.add_page_break()
        
        # Introduction
        self.add_introduction(doc)
        doc.add_page_break()
        
        # Feasibility Study
        self.add_feasibility_study(doc)
        doc.add_page_break()
        
        # Methodology
        self.add_methodology(doc)
        doc.add_page_break()
        
        # Facilities Required
        self.add_facilities_required(doc)
        
        # Save document
        doc.save('SafarSathi_Project_Synopsis.docx')
        print("✅ Synopsis document created: SafarSathi_Project_Synopsis.docx")
        
    def add_title_page(self, doc):
        """Add title page"""
        # Add some spacing
        for _ in range(8):
            doc.add_paragraph()
        
        # Project Title
        title = doc.add_paragraph()
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = title.add_run(self.project_name)
        run.font.size = Pt(24)
        run.font.bold = True
        run.font.name = 'Times New Roman'
        
        doc.add_paragraph()
        
        # Subtitle
        subtitle = doc.add_paragraph()
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = subtitle.add_run("PROJECT SYNOPSIS")
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.name = 'Times New Roman'
        
        # Add spacing
        for _ in range(10):
            doc.add_paragraph()
        
        # Footer details
        footer = doc.add_paragraph()
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = footer.add_run(f"Submitted in {self.current_date}")
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        
    def add_index(self, doc):
        """Add index page"""
        heading = doc.add_heading('INDEX', level=1)
        heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
        heading.runs[0].font.name = 'Times New Roman'
        
        doc.add_paragraph()
        
        # Table of contents
        index_items = [
            ("1.", "Introduction", "3"),
            ("2.", "Feasibility Study", "6"),
            ("3.", "Methodology / Planning of Work", "8"),
            ("4.", "Facilities Required for Proposed Work", "10")
        ]
        
        for sr_no, item, page in index_items:
            p = doc.add_paragraph()
            p.add_run(f"{sr_no}\t{item}").font.name = 'Times New Roman'
            p.add_run(f"\t{page}").font.name = 'Times New Roman'
            p.paragraph_format.line_spacing = 1.5
    
    def add_introduction(self, doc):
        """Add introduction section"""
        heading = doc.add_heading('1. INTRODUCTION', level=1)
        heading.runs[0].font.name = 'Times New Roman'
        
        intro_paragraphs = [
            "SafarSathi is an intelligent AI-powered travel planning application designed to revolutionize the way people plan their trips. The name 'SafarSathi' is derived from Hindi words 'Safar' (journey) and 'Sathi' (companion), perfectly embodying its role as a trusted travel companion for every adventurer.",
            
            "In today's fast-paced world, planning a perfect trip can be time-consuming and overwhelming. Travelers often spend hours researching destinations, comparing hotels, planning itineraries, and managing budgets. SafarSathi addresses these challenges by leveraging artificial intelligence to create personalized, comprehensive travel plans in minutes.",
            
            "The application is built using modern web technologies and advanced AI capabilities. At its core, SafarSathi utilizes Streamlit for creating an intuitive and responsive user interface, LangChain for orchestrating AI workflows, and Groq's high-performance language models for generating intelligent travel recommendations.",
            
            "Key features of SafarSathi include:",
            
            "• Personalized Itinerary Generation: Creates detailed day-by-day travel plans based on user preferences, interests, and budget constraints.\n\n• Smart Hotel Recommendations: Suggests accommodation options within the specified budget range, considering location benefits and amenities.\n\n• Food & Dining Suggestions: Recommends local restaurants, street food spots, and must-try dishes for an authentic culinary experience.\n\n• Budget Optimization: Provides comprehensive budget breakdowns covering accommodation, food, activities, and transportation.\n\n• Transportation Planning: Offers practical advice on getting around the destination, including cost estimates and best options.\n\n• Local Insights: Shares valuable tips about customs, best times to visit attractions, hidden gems, and safety considerations.\n\n• Multiple Export Formats: Allows users to download itineraries in text, markdown, and JSON formats for easy access and sharing.",
            
            "The technology stack comprises Python as the primary programming language, Streamlit for the web framework, LangChain for AI orchestration, and integration with Groq's Mixtral-8x7B language model. The application follows modern software engineering principles with a focus on user experience, scalability, and maintainability.",
            
            "SafarSathi caters to diverse traveler types including budget backpackers, comfort seekers, luxury travelers, adventure enthusiasts, and culture seekers. Whether planning a weekend getaway, international adventure, family vacation, or solo trip, SafarSathi provides tailored recommendations that match individual travel styles and preferences.",
            
            "The application's intelligent design considers multiple factors such as travel duration, number of travelers, accommodation preferences, and specific interests ranging from sightseeing and adventure sports to food tours and cultural experiences. This comprehensive approach ensures that every generated itinerary is unique, practical, and aligned with the traveler's expectations."
        ]
        
        for para_text in intro_paragraphs:
            p = doc.add_paragraph(para_text)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
    
    def add_feasibility_study(self, doc):
        """Add feasibility study section"""
        heading = doc.add_heading('2. FEASIBILITY STUDY', level=1)
        heading.runs[0].font.name = 'Times New Roman'
        
        # Technical Feasibility
        subheading = doc.add_heading('2.1 Technical Feasibility', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        tech_feasibility = [
            "SafarSathi is technically feasible using readily available technologies and frameworks. The project utilizes Python, which is widely supported and has extensive libraries for web development and AI integration. Streamlit provides a rapid development framework for creating interactive web applications without complex frontend development.",
            
            "The integration with Groq API for language model capabilities is straightforward and well-documented. The LangChain framework offers robust tools for managing AI workflows and prompt engineering. All required dependencies are open-source or have accessible APIs, making the project implementable with standard development resources.",
            
            "The application can be deployed on various cloud platforms including Streamlit Cloud, AWS, Google Cloud Platform, or Azure, ensuring scalability and reliability. The technical stack is mature, well-tested, and supported by active developer communities."
        ]
        
        for para_text in tech_feasibility:
            p = doc.add_paragraph(para_text)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
        
        # Economic Feasibility
        subheading = doc.add_heading('2.2 Economic Feasibility', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        economic_feasibility = [
            "The project demonstrates strong economic feasibility with minimal initial investment requirements. Most dependencies are free and open-source. The Groq API offers competitive pricing with generous free tiers suitable for development and initial deployment.",
            
            "Development costs are primarily limited to developer time, as no expensive software licenses or hardware infrastructure is required. Deployment on platforms like Streamlit Cloud is free for personal projects and affordable for commercial use. The potential for monetization through premium features, affiliate partnerships with hotels and travel services, or subscription models makes the project economically viable."
        ]
        
        for para_text in economic_feasibility:
            p = doc.add_paragraph(para_text)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
        
        # Operational Feasibility
        subheading = doc.add_heading('2.3 Need and Significance', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        need_significance = [
            "The global travel industry is rapidly growing, with millions of travelers seeking efficient planning solutions. Traditional travel planning is time-consuming, requiring extensive research across multiple platforms. SafarSathi addresses this need by consolidating the entire planning process into a single, intelligent application.",
            
            "The significance of SafarSathi lies in its ability to democratize travel planning. By providing AI-powered personalized recommendations, it makes professional-quality travel planning accessible to everyone, regardless of their travel experience or budget. The application saves time, reduces planning stress, and enhances travel experiences through intelligent suggestions and comprehensive information.",
            
            "Furthermore, SafarSathi promotes informed travel decisions by providing budget breakdowns, local insights, and safety considerations. This transparency empowers travelers to make choices that align with their preferences and constraints, leading to more satisfying travel experiences."
        ]
        
        for para_text in need_significance:
            p = doc.add_paragraph(para_text)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
    
    def add_methodology(self, doc):
        """Add methodology section"""
        heading = doc.add_heading('3. METHODOLOGY / PLANNING OF WORK', level=1)
        heading.runs[0].font.name = 'Times New Roman'
        
        methodology_intro = "The development of SafarSathi follows a structured software development methodology comprising the following phases:"
        
        p = doc.add_paragraph(methodology_intro)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        for run in p.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
        
        methodology_steps = [
            ("Phase 1: Requirements Analysis and Design", 
             "Identify user requirements, define system architecture, design database schema (if needed), create UI/UX mockups, and define API integration specifications."),
            
            ("Phase 2: Environment Setup and Configuration",
             "Set up development environment, install required dependencies (Streamlit, LangChain, Groq API), configure API keys and environment variables, establish version control with Git, and create project structure."),
            
            ("Phase 3: Core Development",
             "Implement user interface using Streamlit framework, develop AI integration layer with LangChain, create prompt templates for itinerary generation, implement state management for user sessions, develop budget calculation and optimization logic, and integrate Groq API for language model capabilities."),
            
            ("Phase 4: Feature Implementation",
             "Build day-by-day itinerary generation, implement hotel recommendation system, create food and dining suggestion module, develop transportation planning features, add local tips and insights generation, implement multiple export formats (text, markdown, JSON), and create trip history and tracking functionality."),
            
            ("Phase 5: Testing and Quality Assurance",
             "Perform unit testing for individual components, conduct integration testing for API interactions, test user interface responsiveness and usability, validate itinerary generation accuracy and relevance, test budget calculations and edge cases, and perform security testing for API keys and user data."),
            
            ("Phase 6: Deployment and Documentation",
             "Deploy application on cloud platform (Streamlit Cloud/AWS/GCP), configure production environment variables, implement monitoring and logging, create user documentation and guides, prepare project synopsis and presentation, and establish maintenance procedures."),
            
            ("Phase 7: Maintenance and Enhancement",
             "Monitor application performance and user feedback, fix bugs and issues promptly, implement feature enhancements based on user needs, update AI models and prompts for better recommendations, and maintain documentation and codebase.")
        ]
        
        for phase, description in methodology_steps:
            # Phase heading
            subheading = doc.add_heading(phase, level=2)
            subheading.runs[0].font.name = 'Times New Roman'
            subheading.runs[0].font.size = Pt(12)
            
            # Phase description
            p = doc.add_paragraph(description)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
    
    def add_facilities_required(self, doc):
        """Add facilities required section"""
        heading = doc.add_heading('4. FACILITIES REQUIRED FOR PROPOSED WORK', level=1)
        heading.runs[0].font.name = 'Times New Roman'
        
        # Hardware Requirements
        subheading = doc.add_heading('4.1 Hardware Requirements', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        hardware_items = [
            "• Computer System: Intel Core i5 or equivalent processor (minimum)",
            "• RAM: 8 GB or higher",
            "• Storage: 256 GB SSD or higher",
            "• Internet Connection: Stable broadband connection (minimum 10 Mbps)"
        ]
        
        for item in hardware_items:
            p = doc.add_paragraph(item)
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
        
        # Software Requirements
        subheading = doc.add_heading('4.2 Software Requirements', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        software_items = [
            "• Operating System: Windows 11 / macOS / Linux",
            "• Programming Language: Python 3.8 or higher",
            "• Web Framework: Streamlit (latest version)",
            "• AI Framework: LangChain, LangChain-Core, LangChain-Community",
            "• Language Model API: Groq API (Mixtral-8x7B model)",
            "• Development Tools: Visual Studio Code or any Python IDE",
            "• Version Control: Git and GitHub",
            "• Environment Management: python-dotenv for configuration",
            "• Additional Libraries: typing-extensions, pydantic",
            "• Web Browser: Google Chrome, Firefox, or Safari (latest versions)",
            "• Deployment Platform: Streamlit Cloud / AWS / Google Cloud Platform"
        ]
        
        for item in software_items:
            p = doc.add_paragraph(item)
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
        
        # API Requirements
        subheading = doc.add_heading('4.3 API and External Services', level=2)
        subheading.runs[0].font.name = 'Times New Roman'
        
        api_items = [
            "• Groq API Key: Required for AI language model access",
            "• Internet connectivity for API calls and cloud services"
        ]
        
        for item in api_items:
            p = doc.add_paragraph(item)
            p.paragraph_format.line_spacing = 1.5
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
    
    def create_presentation(self):
        """Generate PowerPoint presentation"""
        prs = Presentation()
        prs.slide_width = Inches(10)
        prs.slide_height = Inches(7.5)
        
        # Slide 1: Title Slide
        self.add_title_slide(prs)
        
        # Slide 2: Project Overview
        self.add_overview_slide(prs)
        
        # Slide 3: Features
        self.add_features_slide(prs)
        
        # Slide 4: Technology Stack
        self.add_technology_slide(prs)
        
        # Slide 5: Architecture
        self.add_architecture_slide(prs)
        
        # Slide 6: Feasibility Study
        self.add_feasibility_slide(prs)
        
        # Slide 7: Methodology
        self.add_methodology_slide(prs)
        
        # Slide 8: User Interface
        self.add_ui_slide(prs)
        
        # Slide 9: Implementation
        self.add_implementation_slide(prs)
        
        # Slide 10: Facilities Required
        self.add_facilities_slide(prs)
        
        # Slide 11: Benefits
        self.add_benefits_slide(prs)
        
        # Slide 12: Future Enhancements
        self.add_future_slide(prs)
        
        # Slide 13: Thank You
        self.add_thankyou_slide(prs)
        
        prs.save('SafarSathi_Project_Presentation.pptx')
        print("✅ PowerPoint presentation created: SafarSathi_Project_Presentation.pptx")
    
    def add_title_slide(self, prs):
        """Add title slide to presentation"""
        slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
        
        # Add title
        title_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1))
        title_frame = title_box.text_frame
        title_frame.text = "SafarSathi"
        title_para = title_frame.paragraphs[0]
        title_para.font.size = PptPt(66)
        title_para.font.bold = True
        title_para.font.color.rgb = PptRGBColor(102, 126, 234)
        title_para.alignment = PP_ALIGN.CENTER
        
        # Add subtitle
        subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(3.5), Inches(8), Inches(0.8))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = "AI-Powered Travel Planner"
        subtitle_para = subtitle_frame.paragraphs[0]
        subtitle_para.font.size = PptPt(32)
        subtitle_para.font.color.rgb = PptRGBColor(118, 75, 162)
        subtitle_para.alignment = PP_ALIGN.CENTER
        
        # Add project synopsis text
        synopsis_box = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(8), Inches(0.5))
        synopsis_frame = synopsis_box.text_frame
        synopsis_frame.text = "PROJECT SYNOPSIS"
        synopsis_para = synopsis_frame.paragraphs[0]
        synopsis_para.font.size = PptPt(24)
        synopsis_para.font.bold = True
        synopsis_para.alignment = PP_ALIGN.CENTER
        
        # Add date
        date_box = slide.shapes.add_textbox(Inches(1), Inches(6.5), Inches(8), Inches(0.5))
        date_frame = date_box.text_frame
        date_frame.text = self.current_date
        date_para = date_frame.paragraphs[0]
        date_para.font.size = PptPt(18)
        date_para.alignment = PP_ALIGN.CENTER
    
    def add_overview_slide(self, prs):
        """Add project overview slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content
        
        title = slide.shapes.title
        title.text = "Project Overview"
        
        content = slide.placeholders[1].text_frame
        content.text = "SafarSathi - Your AI Travel Companion"
        
        points = [
            "Intelligent AI-powered travel planning application",
            "Creates personalized travel itineraries in minutes",
            "Comprehensive planning including hotels, food, and activities",
            "Budget-friendly recommendations",
            "User-friendly interface with modern design",
            "Multiple export formats for easy sharing"
        ]
        
        for point in points:
            p = content.add_paragraph()
            p.text = point
            p.level = 1
            p.font.size = PptPt(18)
    
    def add_features_slide(self, prs):
        """Add features slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Key Features"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        features = [
            "📅 Day-by-Day Itinerary Planning",
            "🏨 Smart Hotel Recommendations",
            "🍽️ Food & Dining Suggestions",
            "🚗 Transportation Planning",
            "💰 Budget Breakdown & Optimization",
            "🎯 Personalized Based on Interests",
            "📱 Multiple Travel Styles Support",
            "📥 Downloadable Itineraries (TXT, MD, JSON)"
        ]
        
        for feature in features:
            p = content.add_paragraph()
            p.text = feature
            p.font.size = PptPt(20)
            p.space_before = PptPt(6)
    
    def add_technology_slide(self, prs):
        """Add technology stack slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Technology Stack"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        # Frontend/Framework
        p = content.add_paragraph()
        p.text = "Frontend Framework"
        p.font.size = PptPt(22)
        p.font.bold = True
        p.space_before = PptPt(10)
        
        p = content.add_paragraph()
        p.text = "Streamlit - Modern web framework for Python"
        p.level = 1
        p.font.size = PptPt(18)
        
        # Backend/AI
        p = content.add_paragraph()
        p.text = "AI & Backend"
        p.font.size = PptPt(22)
        p.font.bold = True
        p.space_before = PptPt(10)
        
        p = content.add_paragraph()
        p.text = "LangChain - AI orchestration framework"
        p.level = 1
        p.font.size = PptPt(18)
        
        p = content.add_paragraph()
        p.text = "Groq API (Mixtral-8x7B) - High-performance LLM"
        p.level = 1
        p.font.size = PptPt(18)
        
        # Language
        p = content.add_paragraph()
        p.text = "Programming Language"
        p.font.size = PptPt(22)
        p.font.bold = True
        p.space_before = PptPt(10)
        
        p = content.add_paragraph()
        p.text = "Python 3.8+ with modern libraries"
        p.level = 1
        p.font.size = PptPt(18)
    
    def add_architecture_slide(self, prs):
        """Add system architecture slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "System Architecture"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        architecture_layers = [
            ("Presentation Layer", "Streamlit UI with responsive design"),
            ("Application Layer", "Business logic and state management"),
            ("AI Integration Layer", "LangChain orchestration and prompt engineering"),
            ("External Services Layer", "Groq API for language model inference"),
            ("Data Layer", "Session state and trip history management")
        ]
        
        for layer, description in architecture_layers:
            p = content.add_paragraph()
            p.text = f"{layer}"
            p.font.size = PptPt(20)
            p.font.bold = True
            p.space_before = PptPt(8)
            
            p = content.add_paragraph()
            p.text = description
            p.level = 1
            p.font.size = PptPt(16)
    
    def add_feasibility_slide(self, prs):
        """Add feasibility study slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Feasibility Study"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        # Technical Feasibility
        p = content.add_paragraph()
        p.text = "✅ Technical Feasibility"
        p.font.size = PptPt(24)
        p.font.bold = True
        p.font.color.rgb = PptRGBColor(0, 128, 0)
        
        p = content.add_paragraph()
        p.text = "Mature tech stack, well-documented APIs, scalable infrastructure"
        p.level = 1
        p.font.size = PptPt(16)
        
        # Economic Feasibility
        p = content.add_paragraph()
        p.text = "✅ Economic Feasibility"
        p.font.size = PptPt(24)
        p.font.bold = True
        p.font.color.rgb = PptRGBColor(0, 128, 0)
        p.space_before = PptPt(12)
        
        p = content.add_paragraph()
        p.text = "Low initial investment, free/affordable tools, monetization potential"
        p.level = 1
        p.font.size = PptPt(16)
        
        # Operational Feasibility
        p = content.add_paragraph()
        p.text = "✅ Need & Significance"
        p.font.size = PptPt(24)
        p.font.bold = True
        p.font.color.rgb = PptRGBColor(0, 128, 0)
        p.space_before = PptPt(12)
        
        p = content.add_paragraph()
        p.text = "Growing travel market, time-saving solution, accessible to all"
        p.level = 1
        p.font.size = PptPt(16)
    
    def add_methodology_slide(self, prs):
        """Add methodology slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Development Methodology"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        phases = [
            "Phase 1: Requirements Analysis & Design",
            "Phase 2: Environment Setup & Configuration",
            "Phase 3: Core Development (UI & AI Integration)",
            "Phase 4: Feature Implementation",
            "Phase 5: Testing & Quality Assurance",
            "Phase 6: Deployment & Documentation",
            "Phase 7: Maintenance & Enhancement"
        ]
        
        for phase in phases:
            p = content.add_paragraph()
            p.text = phase
            p.font.size = PptPt(20)
            p.space_before = PptPt(8)
    
    def add_ui_slide(self, prs):
        """Add user interface slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "User Interface Highlights"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        ui_features = [
            "Modern gradient design with purple theme",
            "Intuitive sidebar for trip planning inputs",
            "Interactive forms with real-time validation",
            "Responsive layout for all devices",
            "Tab-based navigation for organized content",
            "Download buttons for multiple formats",
            "Trip history tracking",
            "Comprehensive travel tips section"
        ]
        
        for feature in ui_features:
            p = content.add_paragraph()
            p.text = feature
            p.font.size = PptPt(20)
            p.space_before = PptPt(6)
    
    def add_implementation_slide(self, prs):
        """Add implementation details slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Implementation Highlights"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        implementations = [
            "State management using Streamlit session state",
            "AI prompt engineering for quality itineraries",
            "Dynamic budget calculations",
            "Multi-format export system (TXT, MD, JSON)",
            "Trip history persistence",
            "Error handling and validation",
            "Responsive UI components",
            "Deployed on Streamlit Cloud for easy access"
        ]
        
        for item in implementations:
            p = content.add_paragraph()
            p.text = item
            p.font.size = PptPt(20)
            p.space_before = PptPt(6)
    
    def add_facilities_slide(self, prs):
        """Add facilities required slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Facilities Required"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        # Hardware
        p = content.add_paragraph()
        p.text = "Hardware Requirements"
        p.font.size = PptPt(24)
        p.font.bold = True
        
        p = content.add_paragraph()
        p.text = "Core i5+ processor, 8GB+ RAM, 256GB+ SSD, Broadband internet"
        p.level = 1
        p.font.size = PptPt(16)
        
        # Software
        p = content.add_paragraph()
        p.text = "Software Requirements"
        p.font.size = PptPt(24)
        p.font.bold = True
        p.space_before = PptPt(12)
        
        software_list = [
            "Python 3.8+, Streamlit, LangChain",
            "Groq API, python-dotenv",
            "Git, VS Code, Modern web browser"
        ]
        
        for item in software_list:
            p = content.add_paragraph()
            p.text = item
            p.level = 1
            p.font.size = PptPt(16)
    
    def add_benefits_slide(self, prs):
        """Add benefits slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Benefits & Advantages"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        benefits = [
            "⏱️ Saves hours of manual planning time",
            "💡 Provides expert-level travel recommendations",
            "💰 Optimizes budget with detailed breakdowns",
            "🎯 Personalizes itineraries based on preferences",
            "🌍 Supports global destinations",
            "📱 Accessible anywhere with internet",
            "🔄 Keeps trip history for reference",
            "🎨 User-friendly and visually appealing"
        ]
        
        for benefit in benefits:
            p = content.add_paragraph()
            p.text = benefit
            p.font.size = PptPt(22)
            p.space_before = PptPt(8)
    
    def add_future_slide(self, prs):
        """Add future enhancements slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        
        title = slide.shapes.title
        title.text = "Future Enhancements"
        
        content = slide.placeholders[1].text_frame
        content.clear()
        
        enhancements = [
            "Real-time flight and hotel booking integration",
            "Weather forecasting and alerts",
            "Collaborative trip planning for groups",
            "Mobile application (iOS & Android)",
            "Integration with maps and navigation",
            "Social sharing and community reviews",
            "Multi-language support",
            "Offline itinerary access"
        ]
        
        for enhancement in enhancements:
            p = content.add_paragraph()
            p.text = enhancement
            p.font.size = PptPt(20)
            p.space_before = PptPt(6)
    
    def add_thankyou_slide(self, prs):
        """Add thank you slide"""
        slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
        
        # Thank you text
        thank_you_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1.5))
        thank_you_frame = thank_you_box.text_frame
        thank_you_frame.text = "Thank You!"
        thank_you_para = thank_you_frame.paragraphs[0]
        thank_you_para.font.size = PptPt(66)
        thank_you_para.font.bold = True
        thank_you_para.font.color.rgb = PptRGBColor(102, 126, 234)
        thank_you_para.alignment = PP_ALIGN.CENTER
        
        # Contact info
        contact_box = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(8), Inches(1))
        contact_frame = contact_box.text_frame
        contact_frame.text = "SafarSathi - AI Travel Planner\n✈️ Your Journey, Our Intelligence"
        
        for paragraph in contact_frame.paragraphs:
            paragraph.font.size = PptPt(24)
            paragraph.alignment = PP_ALIGN.CENTER
            paragraph.space_before = PptPt(12)
        
        # Project link
        link_box = slide.shapes.add_textbox(Inches(1), Inches(6), Inches(8), Inches(0.5))
        link_frame = link_box.text_frame
        link_frame.text = "https://safarsathi-3f9ghvrebapp2ijthmfaxe2.streamlit.app/"
        link_para = link_frame.paragraphs[0]
        link_para.font.size = PptPt(16)
        link_para.alignment = PP_ALIGN.CENTER
        link_para.font.color.rgb = PptRGBColor(102, 126, 234)

def main():
    """Main function to generate both documents"""
    print("🚀 SafarSathi Documentation Generator")
    print("=" * 50)
    
    try:
        generator = SafarSathiDocumentGenerator()
        
        print("\n📄 Generating synopsis document...")
        generator.create_synopsis_document()
        
        print("\n📊 Generating PowerPoint presentation...")
        generator.create_presentation()
        
        print("\n" + "=" * 50)
        print("✅ All documents generated successfully!")
        print("\nGenerated files:")
        print("  1. SafarSathi_Project_Synopsis.docx")
        print("  2. SafarSathi_Project_Presentation.pptx")
        print("\n💡 Run this script again after making changes to update both files.")
        
    except ImportError as e:
        print(f"\n❌ Error: Missing required library - {str(e)}")
        print("\n📦 Please install required packages:")
        print("   pip install python-docx python-pptx")
    except Exception as e:
        print(f"\n❌ Error generating documents: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
