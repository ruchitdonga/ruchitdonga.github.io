import os
from app import app, cv_data
from flask import render_template

def build_static_site():
    print("Building static HTML for GitHub Pages...")
    with app.test_request_context():
        # Render the template using the existing data
        html_content = render_template('index.html', cv=cv_data)
        
        # Convert absolute /static/ paths to relative static/ paths for GitHub Pages
        html_content = html_content.replace('href="/static/', 'href="static/')
        html_content = html_content.replace('src="/static/', 'src="static/')
        # Convert internal Flask route links to static filenames (e.g. /contact -> contact.html)
        html_content = html_content.replace('href="/contact"', 'href="contact.html"')
        
        # Write the rendered HTML to index.html in the root directory
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        # Also render contact page to a static contact.html
        contact_content = render_template('contact.html', cv=cv_data)
        contact_content = contact_content.replace('href="/static/', 'href="static/')
        contact_content = contact_content.replace('src="/static/', 'src="static/')
        # Ensure any route links are static-friendly
        contact_content = contact_content.replace('href="/contact"', 'href="contact.html"')
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(contact_content)
            
    print("Success! 'index.html' has been generated in your project folder.")

if __name__ == "__main__":
    build_static_site()
