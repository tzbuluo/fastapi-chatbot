# Product Requirements Document (PRD)

## Language & Project Info
- **Language**: Chinese
- **Programming Language**: Python
- **Project Name**: mgx_chatbot

## Product Definition

### Product Goals
1. **Efficient Data Processing**: Automate the cleaning and pairing of chat data from WeChat CSV exports.
2. **Seamless API Integration**: Integrate with Tencent Cloud DeepSeek API for model training and chat response generation.
3. **Interactive Prototype**: Enable real-time chat interaction through Protopie integration.

### User Stories
1. **As a data scientist**, I want to process WeChat chat data automatically so that I can focus on model training.
2. **As a developer**, I want to integrate with Tencent Cloud DeepSeek API so that I can generate chat responses efficiently.
3. **As a UX designer**, I want to prototype chat interactions in Protopie so that I can validate user flows.

### Competitive Analysis
1. **Dialogflow**: Pros - Easy to use, extensive documentation; Cons - Limited customization, costly at scale.
2. **Rasa**: Pros - Open-source, highly customizable; Cons - Steeper learning curve, requires more development effort.
3. **Microsoft Bot Framework**: Pros - Strong enterprise support, integrates with Azure; Cons - Complex setup, limited flexibility.
4. **IBM Watson Assistant**: Pros - Advanced NLP capabilities, enterprise-grade security; Cons - Expensive, complex pricing model.
5. **Wit.ai**: Pros - Free, easy to get started; Cons - Limited features, less control over model training.

### Competitive Quadrant Chart
```mermaid
quadrantChart
    title "Chatbot Framework Analysis"
    x-axis "Low Customization" --> "High Customization
    y-axis "Low Cost" --> "High Cost"
    quadrant-1 "High Customization, Low Cost"
    quadrant-2 "High Customization, High Cost"
    quadrant-3 "Low Customization, Low Cost"
    quadrant-4 "Low Customization, High Cost"
    "Dialogflow": [0.3, 0.7]
    "Rasa": [0.8, 0.3]
    "Microsoft Bot Framework": [0.6, 0.8]
    "IBM Watson Assistant": [0.7, 0.9]
    "Wit.ai": [0.2, 0.2]
    "Our Target Product": [0.75, 0.4]
```

## Technical Specifications

### Requirements Analysis
1. **Data Cleaning**: Automate the process of filtering and pairing chat messages.
2. **API Integration**: Implement API calls to Tencent Cloud DeepSeek for model training and chat response generation.
3. **Web Service**: Develop a FastAPI-based web service to handle chat requests.
4. **Protopie Integration**: Configure Protopie to interact with the chat API.

### Requirements Pool
- **P0**: Data cleaning script, API integration, FastAPI web service.
- **P1**: Protopie integration, unit tests, deployment scripts.
- **P2**: Performance testing, documentation.

### UI Design Draft
1. **Chat Interface**: Simple text input and output fields.
2. **Protopie Prototype**: Interactive chat flow with response display.

### Open Questions
1. What are the specific requirements for the Protopie integration?
2. Are there any additional data fields required for the model training?