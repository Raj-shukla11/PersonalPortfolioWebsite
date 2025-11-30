import logging
from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('All fields are required!', 'error')
            return render_template('contact.html')
        
        # Log the contact form submission
        contact_data = {
            'timestamp': datetime.now().isoformat(),
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        
        # Print to console as requested
        print("=== NEW CONTACT FORM SUBMISSION ===")
        print(f"Timestamp: {contact_data['timestamp']}")
        print(f"Name: {contact_data['name']}")
        print(f"Email: {contact_data['email']}")
        print(f"Subject: {contact_data['subject']}")
        print(f"Message: {contact_data['message']}")
        print("=====================================")
        
        # Log to application logger
        logging.info(f"Contact form submission: {contact_data}")
        
        # Try to write to file as backup
        try:
            with open('contact_submissions.log', 'a') as f:
                f.write(f"{contact_data}\n")
        except Exception as e:
            logging.error(f"Failed to write contact submission to file: {e}")
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact.contact'))
    
    return render_template('contact.html')
