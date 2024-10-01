---

# Legal Documentation Assistant

This project is a **Legal Documentation Assistant** designed to help users interact with legal documents efficiently through natural language queries and document retrieval. Built using **Langchain**, **OpenAI**, and **Django**, the app allows users to upload and query PDFs, locate relevant law firms via Google Maps, and access a personal chatbot for quick legal information.

## Features

### 1. PDF Query
- Upload PDF legal documents, contracts, or agreements.
- Use natural language to query the documents and retrieve specific sections or answers.
- Powered by **Langchain** and **OpenAI's GPT models**, ensuring accurate and context-aware document querying.

### 2. Google Maps API Integration
- Users can find nearby law firms or legal consultants using **Google Maps API**.
- Search functionality based on location or specific legal service needs.
- View law firms with details like name, address, and contact information.

### 3. Personal Chatbot
- A chatbot, built with **OpenAI**, offers instant responses to legal queries.
- Provides information on common legal terms, procedures, and document interpretations.
- Tailored to assist users with frequent questions regarding legal documentation.

---

## Tech Stack

### Frontend:
- **React** for building the user interface.
- **Tailwind CSS** for responsive and customizable UI design.

### Backend:
- **Django**: Backend framework to handle user authentication, file management, and API integration.
- **Langchain**: For connecting the chatbot and document query functionality with **OpenAI** models.
- **OpenAI**: GPT models are used for document comprehension, chat responses, and contextual legal assistance.

### Databases:
- **PostgreSQL**: For storing user data and uploaded legal documents.

### APIs & External Services:
- **Google Maps API**: Used for law firm location services.
- **OpenAI API**: For powering the chatbot and PDF query capabilities.

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js & npm
- PostgreSQL
- Google Maps API key
- OpenAI API key

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/legal-documentation-assistant.git
cd legal-documentation-assistant
```

2. **Backend Setup (Django)**
   - Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   - Set up environment variables:

   Create a `.env` file in the project root and add your Google Maps API key and OpenAI API key:

   ```bash
   GOOGLE_MAPS_API_KEY=your-google-maps-api-key
   OPENAI_API_KEY=your-openai-api-key
   ```

   - Run database migrations:

   ```bash
   python manage.py migrate
   ```

   - Start the Django development server:

   ```bash
   python manage.py runserver
   ```

3. **Frontend Setup (React)**

   Navigate to the `frontend` folder:

   ```bash
   cd frontend
   ```

   - Install frontend dependencies:

   ```bash
   npm install
   ```

   - Start the frontend:

   ```bash
   npm start
   ```

---

## Usage

### PDF Query
1. Upload your legal document via the dashboard.
2. Type your query in natural language (e.g., "What is the penalty clause in this contract?").
3. The system will fetch and display relevant sections of the document.

### Google Maps Integration
- Go to the "Find a Lawyer" section.
- Enter your location or allow the system to auto-detect your location.
- View law firms on the map with contact details.

### Personal Chatbot
- Access the chatbot through the "Ask a Legal Question" section.
- The bot can help with frequently asked legal questions, document interpretation, and general law advice.

---

## API Documentation

### PDF Query API
- **Endpoint**: `/api/pdf-query/`
- **Method**: POST
- **Request Body**:
  - `pdf_id` (string): ID of the uploaded PDF.
  - `query` (string): The natural language query.
- **Response**:
  - A text summary or specific answer extracted from the document.

### Google Maps API Integration
- **Endpoint**: `/api/find-lawyers/`
- **Method**: GET
- **Request Params**:
  - `location` (string): User's location for searching law firms.
- **Response**:
  - List of nearby law firms with names, addresses, and contact details.

### Chatbot API
- **Endpoint**: `/api/chatbot/`
- **Method**: POST
- **Request Body**:
  - `query` (string): User's legal question.
- **Response**:
  - A text response based on the query.

---

## Future Enhancements
- **Multi-language Support**: Add support for querying documents and interacting with the chatbot in multiple languages.
- **Advanced Analytics**: Provide analytics for law firms based on user interactions.
- **User Annotations**: Allow users to highlight sections of PDFs and add personal notes.

---

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Create a new Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any questions or inquiries, please contact:

- **Azlaan Shaikh**: azlaan@example.com

---

This README provides a complete overview of your project. You can update and tweak it based on specific requirements or additional features!
