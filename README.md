[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# PDF Summarizer API

## 🛠 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/pdf-summarizer-api.git
   cd pdf-summarizer-api
Set up environment variables:

bash
cp env.example .env   # Creates a new .env file from the template
nano .env            # Edit to add your API keys (Ctrl+X to save)
Install dependencies:

bash
pip install -r requirements.txt
Run the API locally:

bash
uvicorn main:app --reload
text

---

#### 2. **Local Development Workflow**
- **`.env.local` vs `.env`**:
  - `.env` → For actual keys (gitignored, never pushed)
  - `env.example` → Template (safe to push)
  
Example workflow:
```bash
# 1. Create your real .env file (secret)
cp env.example .env
nano .env  # Add real keys

# 2. For testing different configs
cp .env .env.local  # Optional