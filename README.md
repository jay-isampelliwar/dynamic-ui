# Dynamic UI Component Generator

A full-stack application that generates dynamic form components based on natural language requests using AI. The system consists of a FastAPI backend with an AI agent and a Next.js frontend that renders dynamic forms.

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   AI Agent      │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   (OpenAI GPT)  │
│                 │    │                 │    │                 │
│ • Chat Interface│    │ • UI Component  │    │ • Natural       │
│ • Dynamic Forms │    │   Generator     │    │   Language      │
│ • Field Mapper  │    │ • Response      │    │   Processing    │
│ • Validation    │    │   Parser        │    │ • Form Schema   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔄 Complete Flow: From API Call to Dynamic UI Rendering

### 1. User Input Phase

- User types a natural language request in the chat interface
- Example: "I need name, email, and phone number fields"

### 2. Frontend Processing

- **Component**: `DynamicUIChatInput.tsx`
- **Hook**: `useDynamicUIChat.ts`
- **API Service**: Integrated within the hook

```typescript
// User types message → sendMessage() called
const sendMessage = useCallback(async (content: string) => {
  // Add user message to chat
  const userMessage: DynamicUIMessage = {
    id: Date.now().toString(),
    content: content.trim(),
    role: "user",
    timestamp: new Date(),
  };

  // Call backend API
  const response = await sendDynamicUIMessage(content.trim());
});
```

### 3. Backend AI Processing

- **Endpoint**: `POST /generate-ui-component`
- **Agent**: `ui_component_agent` (OpenAI GPT-4)
- **Processing**: Natural language → Structured form schema

````python
@app.post("/generate-ui-component")
async def generate_ui_component(request: dict):
    user_message = request.get("message", "")
    response = await ui_component_agent.arun(user_message)

    # Parse AI response to extract component
    component_match = re.search(r'```component\s*\n(.*?)\n```', content, re.DOTALL)
    if component_match:
        component = json.loads(component_match.group(1).strip())

    return {
        "content": content,
        "component": component
    }
````

### 4. AI Agent Response Format

The AI agent is configured to return responses in this exact format:

```json
{
  "type": "form",
  "fields": [
    {
      "name": "fullName",
      "label": "Full Name",
      "type": "text",
      "required": true,
      "placeholder": "Enter your full name"
    },
    {
      "name": "email",
      "label": "Email Address",
      "type": "email",
      "required": true,
      "placeholder": "your.email@example.com"
    }
  ],
  "submitText": "Submit"
}
```

### 5. Frontend Component Rendering

- **Message List**: `DynamicUIMessageList.tsx`
- **Form Component**: `DynamicUIFormComponent.tsx`
- **Field Mapper**: `FieldMapper.tsx`

```typescript
// Message list renders each message
{
  messages.map((message) => (
    <div key={message.id}>
      <div>{message.content}</div>
      {message.component && (
        <DynamicUIFormComponent component={message.component} />
      )}
    </div>
  ));
}
```

### 6. Dynamic Field Rendering

The `FieldMapper` component maps field types to specific React components:

```typescript
switch (field.type) {
  case "text":
    return <TextField {...commonProps} />;
  case "email":
    return <EmailField {...commonProps} />;
  case "textarea":
    return <TextareaField {...commonProps} rows={field.rows || 3} />;
  case "select":
    return <SelectField {...commonProps} options={field.options || []} />;
  case "multiselect":
    return <MultiSelectField {...commonProps} options={field.options || []} />;
  case "number":
    return <NumberField {...commonProps} min={field.min} max={field.max} />;
  case "date":
    return <DateField {...commonProps} />;
  case "checkbox":
    return <CheckboxField {...commonProps} />;
  default:
    return <TextField {...commonProps} />;
}
```

## 🧩 Component Architecture

### Backend Components

#### 1. FastAPI Application (`app.py`)

- **CORS Configuration**: Allows frontend communication
- **AI Agent**: OpenAI GPT-4 powered component generator
- **Response Parser**: Extracts JSON components from AI responses
- **Error Handling**: Graceful error responses

#### 2. AI Agent Configuration

```python
ui_component_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="UI Component Generator expert",
    instructions="Generate dynamic form components based on user requests",
    expected_output="Structured JSON component format"
)
```

### Frontend Components

#### 1. Core Components

- **`ChatInterface.tsx`**: Main chat container
- **`DynamicUIMessageList.tsx`**: Renders chat messages and forms
- **`DynamicUIFormComponent.tsx`**: Dynamic form renderer
- **`FieldMapper.tsx`**: Field type router

#### 2. Field Components (`fields/`)

- **`TextField.tsx`**: Single line text input
- **`EmailField.tsx`**: Email validation input
- **`TextareaField.tsx`**: Multi-line text input
- **`SelectField.tsx`**: Dropdown selection
- **`MultiSelectField.tsx`**: Multiple choice selection
- **`NumberField.tsx`**: Numeric input with validation
- **`DateField.tsx`**: Date picker
- **`CheckboxField.tsx`**: Boolean input

#### 3. State Management

- **`useDynamicUIChat.ts`**: Chat state and API communication

## 📊 Data Flow Diagram

```
User Input
    ↓
Chat Interface
    ↓
useDynamicUIChat Hook
    ↓
API Service (integrated)
    ↓
FastAPI Backend
    ↓
AI Agent (OpenAI)
    ↓
Response Parser
    ↓
JSON Component
    ↓
Frontend Rendering
    ↓
FieldMapper
    ↓
Specific Field Components
    ↓
Dynamic Form Display
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- Python 3.8+
- OpenAI API key

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Environment Variables

```bash
# Backend (.env)
OPENAI_API_KEY=your_openai_api_key

# Frontend (.env.local)
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 💡 Usage Examples

### Example 1: Basic Contact Form

**User Input**: "I need a contact form with name, email, and message"

**AI Response**:

```json
{
  "type": "form",
  "fields": [
    {
      "name": "name",
      "label": "Full Name",
      "type": "text",
      "required": true,
      "placeholder": "Enter your full name"
    },
    {
      "name": "email",
      "label": "Email Address",
      "type": "email",
      "required": true,
      "placeholder": "your.email@example.com"
    },
    {
      "name": "message",
      "label": "Message",
      "type": "textarea",
      "required": true,
      "placeholder": "Enter your message..."
    }
  ],
  "submitText": "Send Message"
}
```

### Example 2: Complex Form with Options

**User Input**: "Create a job application form with experience level and skills"

**AI Response**:

```json
{
  "type": "form",
  "fields": [
    {
      "name": "experience",
      "label": "Years of Experience",
      "type": "select",
      "required": true,
      "options": [
        "0-1 years",
        "1-3 years",
        "3-5 years",
        "5-10 years",
        "10+ years"
      ]
    },
    {
      "name": "skills",
      "label": "Technical Skills",
      "type": "multiselect",
      "required": true,
      "options": ["JavaScript", "React", "Node.js", "Python", "Java", "SQL"]
    }
  ],
  "submitText": "Submit Application"
}
```

## 🔧 Supported Field Types

| Type          | Description               | Validation                 |
| ------------- | ------------------------- | -------------------------- |
| `text`        | Single line text input    | Required field validation  |
| `email`       | Email input               | Email format validation    |
| `textarea`    | Multi-line text input     | Required field validation  |
| `select`      | Dropdown selection        | Required field validation  |
| `multiselect` | Multiple choice selection | Required field validation  |
| `number`      | Numeric input             | Number validation, min/max |
| `date`        | Date picker               | Date format validation     |
| `checkbox`    | Boolean input             | Required field validation  |

## 🛡️ Validation & Error Handling

### Frontend Validation

- Required field validation
- Email format validation
- Number range validation
- Real-time error display

### Backend Error Handling

- AI response parsing errors
- API communication errors
- Graceful fallback responses

## 🔄 State Management

### Chat State

```typescript
interface ChatState {
  messages: DynamicUIMessage[];
  isLoading: boolean;
  error: string | null;
}
```

### Form State

```typescript
interface FormState {
  formData: Record<string, any>;
  errors: Record<string, string>;
}
```

## 🎨 Styling & UI

- **Framework**: Tailwind CSS
- **Design**: Clean, modern interface
- **Responsive**: Mobile-friendly design
- **Accessibility**: ARIA labels and keyboard navigation

## 🔍 Debugging & Development

### Backend Logging

```python
print("response", response.content)
print(f"Failed to parse component JSON: {e}")
```

### Frontend Logging

```typescript
console.log("response", response);
console.log("Valid component received:", component);
```

## 🚀 Future Enhancements

- [ ] Form submission handling
- [ ] Form templates library
- [ ] Advanced validation rules
- [ ] Form data persistence
- [ ] Export to PDF/Word
- [ ] Multi-language support
- [ ] Custom field types
- [ ] Form analytics

## 📝 API Documentation

### POST /generate-ui-component

Generate dynamic UI components from natural language.

**Request**:

```json
{
  "message": "Create a form with name and email fields"
}
```

**Response**:

```json
{
  "content": "I've created a contact form for you with the requested fields.",
  "component": {
    "type": "form",
    "fields": [...],
    "submitText": "Submit"
  }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
