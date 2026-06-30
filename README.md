# My Demo App

A simple dummy demo project that integrates a Python backend with npm scripts.

## Directory Structure

```text
my-demo-app/
├── README.md
├── docs/
│   └── architecture.md
├── src/
│   └── app.py
└── package.json
```

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/)
- [Node.js and npm](https://nodejs.org/)

### Running the App

To run the application, navigate to the `my-demo-app` directory and use the npm start script:

```bash
npm start
```

This will run `python src/app.py` and start a local HTTP server. Open your browser and navigate to:

[http://localhost:8000](http://localhost:8000)

## API Endpoints

- `GET /`: Serves the interactive user interface.
- `GET /api/info`: Returns dummy JSON data with status details.
