import json
import os
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

def load_portfolio_data():
    """Load portfolio data from JSON file"""
    try:
        with open('data/portfolio_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback data if JSON file not found
        return {
            "personal_info": {
                "name": "Raj Shukla",
                "title": "Computer Science Student",
                "email": "shuklaraj0002@gmail.com"
            },
            "projects": [],
            "skills": {"languages": [], "frameworks": [], "soft_skills": []},
            "experience": [],
            "education": [],
            "certificates": [],
            "achievements": []
        }

@main_bp.route('/')
def index():
    """Home page route"""
    data = load_portfolio_data()
    return render_template('index.html', data=data)

@main_bp.route('/about')
def about():
    """About page route"""
    data = load_portfolio_data()
    return render_template('index.html', data=data, section='about')

@main_bp.route('/projects')
def projects():
    """Projects page route"""
    data = load_portfolio_data()
    return render_template('index.html', data=data, section='projects')

@main_bp.route('/skills')
def skills():
    """Skills page route"""
    data = load_portfolio_data()
    return render_template('index.html', data=data, section='skills')

@main_bp.route('/experience')
def experience():
    """Experience page route"""
    data = load_portfolio_data()
    return render_template('index.html', data=data, section='experience')


