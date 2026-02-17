# 🤖 AI WhatsApp Automation Bot

A serverless-ready backend system that receives WhatsApp messages, processes them using **Google Gemini AI**, and sends intelligent automated responses.

Built using **Python, FastAPI, WhatsApp Cloud API, and Google Gemini**.

## 📸 WhatsApp Bot Demo

Below is an example conversation showing the bot responding with context-aware replies.

![WhatsApp Bot Demo](assets/whatsapp-demo.png)

---

---

## Features

Receive WhatsApp messages via webhook
Parse and route complex webhook JSON payloads
Generate AI responses using Gemini API
Send automated replies via WhatsApp Cloud API
Maintain short-term conversation memory for multi-turn interactions
Secure webhook verification & token management
Production-ready error handling & logging
Cloud deployable (GCP / AWS)

---

## Architecture

```
User → WhatsApp → Meta Webhook
           ↓
        FastAPI Webhook Server
           ↓
      Message Processing Layer
           ↓
   Conversation Memory (per user)
           ↓
        Gemini AI Engine
           ↓
   WhatsApp Cloud API Response
```

---

## 🛠 Tech Stack

**Backend**

* Python
* FastAPI
* Async processing

**APIs & Integrations**

* WhatsApp Cloud API (Meta)
* Google Gemini API

**Cloud & DevOps**

* ngrok (local tunneling)

---

## Project Structure

```
whatsapp-ai-bot/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── webhook_handler.py
│   ├── gemini_service.py
│   ├── whatsapp_service.py
│   ├── conversation_store.py│   
|   ├── utils.py
│
├── requirements.txt
└── .env
```

---

## Conversation Memory (Multi-Turn Context)

The bot maintains short-term conversation history per user to support context-aware, multi-step interactions.

### How it works

* Stores recent messages per user session
* Sends conversation context to Gemini
* Limits stored history to reduce token usage
* Enables natural multi-turn conversations

### Current behavior

* Memory stored in RAM (resets on restart)
* Keeps last few messages per user
* Optimized for performance & cost

### Production upgrade (optional)

Replace in-memory storage with:

* Firestore
* Redis
* DynamoDB

---

## ⚙️ Setup Instructions

### 1 Clone Repository

```bash
git clone https://github.com/yourusername/whatsapp-ai-bot.git
cd whatsapp-ai-bot
```

---

### 2 Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

---

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4 Environment Variables

Create a `.env` file:

```
WHATSAPP_TOKEN=your_meta_token
PHONE_NUMBER_ID=your_phone_number_id
VERIFY_TOKEN=myverifytoken123
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🔑 API Setup

### WhatsApp Cloud API

1. Create Meta developer app
2. Add WhatsApp product
3. Get access token & phone number ID
4. Add your phone as test recipient

Docs: [https://developers.facebook.com/docs/whatsapp/cloud-api](https://developers.facebook.com/docs/whatsapp/cloud-api)

---

### Gemini API

1. Create API key in Google AI Studio
2. Enable Generative Language API
3. Link billing (required for quota)

Docs: [https://ai.google.dev/](https://ai.google.dev/)

---

## ▶️ Run Locally

### Start server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### Start ngrok tunnel

```bash
ngrok http 8000
```

Copy HTTPS URL.

---

## 🔗 Configure Webhook

In Meta Dashboard:

Callback URL:

```
https://YOUR-NGROK-URL/webhook
```

Verify Token:

```
myverifytoken123
```

Subscribe to:

* messages

---

## Testing

Send a WhatsApp message to the test number:

---

## Security Features

✔ Webhook verification
✔ Secure token storage via environment variables
✔ Signature validation support
✔ Error handling & fallback responses

---

## 📜 License

MIT License

---

## 👤 Author

**Suhas k m**
GitHub: [https://github.com/suhaskm28](https://github.com/suhaskm28)

---
