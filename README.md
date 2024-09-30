
# TICK MY WAY

## Overview

This project is designed to create an intuitive and interactive platform for educational content delivery and management. The core features include:

1. Dynamic Roadmap Feature: This allows students to follow a personalized learning path with a progress tracking system. The roadmap provides a visual structure for courses, enabling users to tick off milestones as they advance through their learning objectives. Instructors can easily build and adjust these roadmaps for different use cases.

2. Gamified Experience: The platform incorporates a gamification layer that introduces a premium currency system. Users can earn currency based on course progress, which can then be used to unlock profile customizations and other engaging features, enhancing motivation and interaction.

3. User-Friendly UI/UX: The interface is designed to be intuitive and responsive, catering to both students and instructors. It simplifies the process of course creation and management while offering a seamless user experience for students to navigate through their learning paths.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow the instructions below:

1. Clone the repository:
   ```bash
   git clone https://github.com/aiibooouuu/webtrial.git    
   ```

2. Navigate into the project directory:
   ```bash
   cd webtrial
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment (optional, if needed):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

## Usage

To run the project locally, follow these steps:

1. Start the Flask server:
   ```bash
   python main.py
   ```

2. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Features

- **Roadmap Section**: A dynamic roadmap for users to follow.
- **Authentication**: Login and registration functionality.
- **User Dashboard**: Personalized user information displayed from the database.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLAlchemy (or specify your DB)
- **Authentication**: Flask-Login, Flask-WTF
- **Session Handling**: Flask Session Management

## Contributing

Contributions are welcome! To contribute:

1. Fork the project.
2. Create your feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
