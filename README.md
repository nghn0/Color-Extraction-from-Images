# Color Extraction from Images

## Description
A web application that enables users to upload an image and extracts the most prominent colors from that image. The application processes the uploaded image using Python libraries and displays the extracted colors on the web page.

## Features
- **Image Upload**: Users can upload images using a simple form.
- **Color Extraction**: Analyzes the uploaded image and retrieves the top 100 unique colors.
- **Display Colors**: Shows the extracted colors on the results page in a visually appealing manner.
- **Responsive Design**: Utilizes Bootstrap to ensure a user-friendly experience on all devices.

## Technologies
- **Web Framework**: Flask for creating the web application.
- **Image Processing**: Pillow (PIL) for opening and manipulating images.
- **Data Handling**: NumPy for efficient array handling and color extraction.
- **Forms**: Flask-WTF for managing forms and file uploads.
- **Styling**: Flask-Bootstrap for responsive web design.

## Usage
1. Ensure that the required libraries (Flask, Flask-WTF, NumPy, Pillow, Flask-Bootstrap) are installed in your Python environment.
2. Run the application using Python, and navigate to the home page.
3. Upload an image using the provided form and submit it.
4. The application will extract the top colors and display them on the results page.

## Notes
This project demonstrates how to build a web application that processes images and extracts data from them. It highlights the integration of image processing with web frameworks, making it an excellent resource for learning about web development and data visualization in Python.
