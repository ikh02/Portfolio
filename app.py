from flask import Flask, render_template, abort

app = Flask(__name__)

# A "database" of your project information
PROJECTS = {
    'car-dealership': {
        'title': 'FYP Car Dealership Website (Python Flask)',
        'thumbnail': 'FYP.png',  # <-- NEW
        'full_description': 'Our final year project is a fully functional, interactive web portal designed for a car dealership. It was built using the Python Flask framework for the backend logic and routing. For data persistence, it utilizes SQLAlchemy to manage a database of vehicle inventory, customer inquiries, and sales records. The application has an AI intergrated chatbot that interprets the scraped data in order to support the client and the suggest the most compatible product.',
        'images': ['FYP2.png', 'FYP1.png'] # TODO: Replace with your actual image filenames
    },
    'currency-exchange-app': {
        'title': 'LBP-USD Currency Exchange Mobile App (Kotlin)',
        'thumbnail': 'Mobile.png',  # <-- NEW
        'full_description': 'Developed the native Android client for a comprehensive multi-platform currency exchange application. The app was built using Kotlin, as I implemented a fully reactive user interface that allows users to perform authentication, browse peer-to-peer exchange offers, and manage their own listings in real-time. This was achieved by integrating with a powerful REST API built on Flask and SQLAlchemy.',
        'images': ['Mobile1.png','Mobile2.png'] # TODO: Replace
    },
    'object-tracking': {
        'title': 'Real-Time Object Tracking (Python, PyTorch)',
        'thumbnail': 'AI2.png', # You will need to create this image
        'full_description': 'This project is a high-performance, real-time object detection and tracking system built with the YOLOv5 algorithm. The core of the system uses PyTorch for deep learning model development and training, and OpenCV for video processing. I implemented the complete pipeline, starting with preprocessing the extensive COCO dataset to prepare it for training. After training the YOLOv5 model, I exported it to the ONNX format for cross-framework compatibility. The final stage involves applying the trained model to live video streams, where it performs object detection, followed by NMS to eliminate duplicate detections and refine predictions.',
        'images': ['AI.png', 'AI3.png'] # You can use screenshots from your report
    },
    'cipher-encryption': {
        'title': 'Cipher Encryption Website (Python)',
        'thumbnail': 'CipherThumbnail.png',  # <-- NEW
        'full_description': 'This project is an educational and interactive website that explores the world of cryptography. I collaborated with team members to create a platform where users can learn about and experiment with various classical encryption and decryption techniques. The site provides tools to encode and decode messages using algorithms like the Caesar cipher, Vigenère cipher, and others, offering a hands-on approach to understanding foundational cryptographic concepts.',
        'images': ['Vigenere1.png','Vigenere2.png'] # TODO: Replace
    }
}


@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

# --- NEW DYNAMIC PROJECT ROUTE ---
@app.route('/project/<project_slug>')
def project_page(project_slug):
    # Find the project data from our dictionary
    project = PROJECTS.get(project_slug)
    
    # If the project doesn't exist, show a 404 error
    if not project:
        abort(404)
        
    # Otherwise, render the project page with the correct data
    return render_template('project_page.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)