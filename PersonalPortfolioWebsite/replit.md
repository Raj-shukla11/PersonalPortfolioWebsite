# Portfolio Website - Raj Shukla

## Overview

This is a personal portfolio website built with Flask showcasing Raj Shukla's work as a Computer Science student and Machine Learning enthusiast. The application presents his projects, skills, experience, downloadable resume, and provides a contact form for potential opportunities.

## Recent Changes (January 2025)

✓ Removed blog section as requested by user
✓ Added download resume section with PDF access
✓ Integrated professional profile photo
✓ Added certificate download links and verification URLs
✓ Enhanced certificate display with credential IDs
✓ Updated navigation to replace Blog with Resume
✓ Added responsive styling for profile photo and resume section

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a simple Flask-based web architecture with a modular blueprint structure. It's designed as a static portfolio with dynamic contact form functionality, using JSON for data storage and file-based logging for contact submissions.

### Architecture Pattern
- **MVC Pattern**: Flask templates (View), Blueprint routes (Controller), JSON data files (Model)
- **Blueprint Architecture**: Modular route organization separating main portfolio pages from contact functionality
- **Static Asset Management**: CSS, JavaScript, and images served through Flask's static file handling

## Key Components

### 1. Flask Application Core
- **Main Application** (`app.py`): Central Flask app configuration with blueprint registration
- **Entry Point** (`main.py`): Alternative entry point for running the application
- **Development Configuration**: Debug mode enabled, proxy fix for deployment environments

### 2. Blueprint Structure
- **Main Blueprint** (`blueprints/main.py`): Handles portfolio display routes (home, about, projects, skills)
- **Contact Blueprint** (`blueprints/contact.py`): Manages contact form submission and validation
- **Modular Design**: Separates concerns and allows for easy feature expansion

### 3. Data Management
- **JSON-based Data Store** (`data/portfolio_data.json`): Contains all portfolio information including personal details, projects, skills, education, and experience
- **File-based Logging**: Contact form submissions logged to both console and file system
- **Fallback Data**: Graceful handling when JSON file is unavailable

### 4. Frontend Architecture
- **Bootstrap Framework**: Uses Replit's dark theme variant for consistent styling
- **Responsive Design**: Mobile-first approach with Bootstrap's grid system
- **Template Inheritance**: Base template with extending child templates for DRY principles
- **Interactive Elements**: Smooth scrolling, typing effects, and scroll animations

## Data Flow

### Portfolio Data Flow
1. Route handler calls `load_portfolio_data()`
2. Function attempts to read from `data/portfolio_data.json`
3. If file exists, JSON data is parsed and returned
4. If file missing, fallback data structure is provided
5. Data passed to template for rendering

### Contact Form Flow
1. User submits contact form via POST request
2. Form data extracted and validated
3. Submission logged to console with formatted output
4. Data appended to `contact_submissions.log` file
5. Application logger records submission
6. Success message flashed to user
7. User redirected to prevent resubmission

## External Dependencies

### Frontend Libraries
- **Bootstrap CSS**: Replit's dark theme variant for consistent UI
- **Font Awesome**: Icon library for visual elements
- **Custom CSS**: Additional styling for branding and animations

### Python Packages
- **Flask**: Web framework for application structure
- **Werkzeug**: WSGI utilities including ProxyFix for deployment

### Data Sources
- **JSON Files**: Local file system for portfolio data storage
- **Log Files**: Local file system for contact form submissions

## Deployment Strategy

### Development Environment
- **Local Development**: Flask development server with debug mode
- **Host Configuration**: Configured to run on `0.0.0.0:5000` for external access
- **Environment Variables**: Session secret key configurable via environment

### Production Considerations
- **Proxy Support**: ProxyFix middleware configured for reverse proxy deployments
- **Session Security**: Environment-based secret key configuration
- **Logging**: Structured logging system ready for production monitoring
- **Static Assets**: CDN-hosted external dependencies for better performance

### Scalability Notes
- **Stateless Design**: No database dependencies, easily horizontally scalable
- **File-based Storage**: Contact submissions stored locally (consider external storage for production)
- **Template Caching**: Flask template caching available for performance optimization

## Key Features

### Portfolio Showcase
- Single-page application design with smooth navigation
- Comprehensive sections for projects, skills, experience, education, and resume
- Professional profile photo integration
- Responsive design optimized for all device sizes
- Professional dark theme with consistent branding

### Resume & Credentials Management
- Downloadable PDF resume with direct links
- Certificate downloads and verification links
- Professional credential display with IDs
- Resume highlights summary section

### Contact Management
- Validated contact form with required field checking
- Multiple logging mechanisms for reliable data capture
- User-friendly feedback with flash messages
- Prevention of form resubmission through redirect pattern

### Performance Optimizations
- JSON-based data loading for fast page rendering
- CDN-hosted external resources
- Minimal server-side processing for portfolio display
- Efficient template inheritance structure