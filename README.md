# Backend File Store Service

This project implements a simple file store service with an HTTP server and a command-line client, allowing users to add, remove, update, and list files. Additionally, it includes utilities for counting words and finding frequent words across the stored files.

---

## Table of Contents

- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
  - [Run the Server](#run-the-server)
  - [Use the Client](#use-the-client)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Docker](#docker)
  - [Kubernetes](#kubernetes)
- [Contributing](#contributing)
- [License](#license)

---

## Technologies

- **Backend**: Python (Flask)
- **CLI Client**: Python (argparse)
- **Testing**: Pytest
- **Containerization**: Docker
- **Deployment**: Kubernetes

---

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/backend-file-store.git
   cd backend-file-store
   ```

2. Set up a virtual environment (recommended for Python projects):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   .\venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r server/requirements.txt
   ```

4. For Docker (optional), build the Docker image:
   ```bash
   docker build -t backend-file-store ./docker
   ```

---

## Usage

### Run the Server

1. Navigate to the `/server` directory:
   ```bash
   cd server
   ```

2. Run the Flask server:
   ```bash
   python app.py
   ```

   By default, the server will be available at `http://127.0.0.1:5000`.

---

### Use the Client

The client is a command-line tool for interacting with the server.

1. Navigate to the `/client` directory:
   ```bash
   cd client
   ```

2. To add files to the server:
   ```bash
   python cli.py add <file1> <file2> ...
   ```

3. To list all files:
   ```bash
   python cli.py list
   ```

4. To remove a file:
   ```bash
   python cli.py remove <filename>
   ```

5. To update a file:
   ```bash
   python cli.py update <filename> <file_path>
   ```

6. To get the word count of all files:
   ```bash
   python cli.py wordcount
   ```

7. To get the most frequent words across all files:
   ```bash
   python cli.py freq-words --order dsc --limit 10
   ```

---

## Testing

### Run Tests

To run the tests for the server and client:

1. Install testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests using pytest:
   ```bash
   pytest tests/
   ```

---

## Deployment

### Docker

1. Build the Docker image:
   ```bash
   docker build -t backend-file-store ./docker
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 backend-file-store
   ```

### Kubernetes

To deploy the service on Kubernetes:

1. Ensure you have a working Kubernetes or OpenShift cluster. You can use [Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/) or [Kind](https://kind.sigs.k8s.io/) for local clusters.

2. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
   ```

3. To expose the service (if using Minikube or Kind):
   ```bash
   kubectl expose deployment backend-file-store --type=NodePort --name=backend-file-store-service
   ```

---

## Contributing

We welcome contributions to this project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
