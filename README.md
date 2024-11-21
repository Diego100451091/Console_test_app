# Console_test_app
This is a console test application that allows you to take tests, study the questions, or review previous incorrect answers.

## Introduction
Console_test_app is de p users prepare for exams by providing a platform to practice questions categorized by topics. It supports multiple-choice questions and keeps track of incorrect answers for further review.

## Features
- Multiple-choice questions
- Questions categorized by topics
- Review of previous incorrect answers
- Easy configuration through a JSON file
- Spanish and English language support

## Installation
To install the application, clone the repository and navigate to the project directory:

## Execution
To execute the application, you need to run the following command in the terminal:
```bash
python main.py
```

## Configuration
The application is configured to use the [questions.json](data/questions.json) file into the [data](data)  folder to load the questions. This file contains a dictionary with the questions grouped by topics. The strcture that this file should have is the following:
```json
{
    "Topic 1": [
        {
            "question": "Question 1",
            "options": {
                "a": "Option a",
                "b": "Option b",
                "c": "Option c",
                "d": "Option d"
            },
            "answer": "a"
        },
        ...
    ],
    "Topic 2": [...],
    ...
}
```

## Contribution
We welcome contributions to improve Console_test_app. To contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## Farewell
Thank you for using Console_test_app. We hope this tool helps you in your exam preparation. Good luck and success in your studies!



