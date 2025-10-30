# 📈 Product Marketer AI Assistant

A Streamlit-powered web application designed for product marketers to rapidly generate engaging product descriptions and relevant social media hashtags using the Groq API for lightning-fast AI inference.

## 🚀 Live Demo

Experience the app in action: [https://aprorduct-description.streamlit.app/](https://aprorduct-description.streamlit.app/)

## ✨ Features

*   **AI-Powered Content Generation:** Generate unique product descriptions and a list of social media hashtags.
*   **Fast Inference:** Leverages the Groq API (using the `llama3-8b-8192` model) for incredibly quick content generation.
*   **Customizable Descriptions:**
    *   Input Product Name, Category, Key Features, and Target Audience.
    *   Select from various **Tones of Voice** (Professional, Friendly, Luxurious, Adventurous, Playful, Informative, Persuasive, Funny/Humor).
    *   Choose **Description Length** (Short - 1 paragraph, Medium - 2 paragraphs, Long - 3 paragraphs).
*   **Multiple Variations:** Generates 2 distinct descriptions and their associated hashtags by default.
*   **Regenerate Option:** Easily re-run the generation process with the same inputs.
*   **Download Content:** Save the generated descriptions and hashtags to a text file.
*   **User-Friendly UI:** Clean and intuitive interface built with Streamlit.

## 🛠️ Technologies Used

*   **Frontend/Backend:** Streamlit (Python framework)
*   **Large Language Model (LLM):** Groq API (`llama3-8b-8192` model)
*   **Environment Management:** `python-dotenv`

## ⚙️ How to Run Locally

To run this application on your local machine, follow these steps:

### 1. Prerequisites

*   **Python 3.7+:** Ensure Python is installed on your system.
*   **Groq API Key:**
    *   Sign up at [console.groq.com/keys](https://console.groq.com/keys).
    *   Generate a new API key. Keep this key confidential.

### 2. Setup

1.  **Clone the Repository (or Download):**
    ```bash
    git clone https://github.com/YOUR_USERNAME/your-repo-name.git
    cd your-repo-name # Replace with your actual repository name
    ```
    *(If you just uploaded files manually to GitHub, then download the repository as a ZIP from GitHub and extract it.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    *   Create a file named `.env` in the root directory of your project (the same folder as `app.py`).
    *   Add your Groq API key to this file:
        ```
        GROQ_API_KEY="your_groq_api_key_here"
        ```
    *   **Important:** The `.env` file is included in `.gitignore` and should **never** be committed to GitHub for security reasons.

### 3. Run the Application

```bash
streamlit run app.py
