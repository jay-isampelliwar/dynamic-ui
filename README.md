# Weather Assistant

A modern AI-powered weather assistant with a beautiful chat interface. The application uses OpenAI's function calling to get real-time weather data for any location.

## Features

- 🤖 AI-powered weather assistant using OpenAI GPT-3.5-turbo
- 🌤️ Real-time weather data from OpenMeteo API
- 💬 Modern chat interface with message history
- 🎨 Beautiful UI built with Next.js, TypeScript, and Tailwind CSS
- ⚡ Fast API backend with FastAPI
- 🔧 Function calling for precise weather data retrieval

## Tech Stack

### Backend

- **FastAPI** - Modern Python web framework
- **OpenAI** - AI language model integration
- **OpenMeteo** - Free weather API
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend

- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide React** - Beautiful icons
- **pnpm** - Fast package manager

## Project Structure

```
pth/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── openai_client.py     # OpenAI integration
│   ├── tools/
│   │   └── weather.py       # Weather API tool
│   ├── model/
│   │   └── weather_model.py # Weather data models
│   ├── constants/
│   │   └── tool_call_schema.py # Function calling schemas
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── src/
    │   ├── app/             # Next.js app directory
    │   ├── components/      # React components
    │   │   └── ChatInterface.tsx
    │   └── lib/
    │       └── utils.ts     # Utility functions
    ├── package.json
    └── pnpm-lock.yaml
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- pnpm
- OpenAI API key

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:

   ```bash
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   pnpm install
   ```

3. Start the development server:

   ```bash
   pnpm dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Usage

1. Open the chat interface in your browser
2. Ask about the weather for any location, for example:
   - "What's the weather like in New York?"
   - "How hot is it in Tokyo right now?"
   - "What's the temperature in London?"

The AI assistant will:

1. Understand your request
2. Extract location information
3. Use the weather tool to get real-time temperature data
4. Provide a natural language response

## API Endpoints

- `GET /` - Health check
- `POST /weather` - Weather information endpoint
  - Body: `{"user_prompt": "string"}`

## Development

### Backend Development

The backend uses FastAPI with automatic API documentation. Visit `http://localhost:8000/docs` to see the interactive API documentation.

### Frontend Development

The frontend uses Next.js with:

- App Router for routing
- TypeScript for type safety
- Tailwind CSS for styling
- Lucide React for icons

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
