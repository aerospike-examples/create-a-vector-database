# Create a Vector Database and learn about LLMs

This repository is designed for a workshop about learning vector database, LLMs, RAGs and so on.

To interact with the LLM portion, you will need access to an OpenAI API key or Google Gemini service account.
In the `/config/config.env` file, add your information as follows:

- For OpenAI
  ```
  PROJECT_ID="Your projectID if needed"
  LOCATION=
  OPENAI_API_KEY="your OpenAI API key"
  MODEL_ID="the model to use, e.g. gpt-4o"
  PATH_TO_AUTH=
  ```
- For Google Gemini
  ```
  PROJECT_ID="Your projectID"
  LOCATION="Your project location, e.g. us-central1"
  OPENAI_API_KEY=
  MODEL_ID="the model to use, e.g. google/gemini-1.5-flash-002"
  PATH_TO_AUTH="path to your auth.json file"
  ```

There are two ways to interact with this repo:

### With containers

1. Build and deploy the containers:
   ```
   DOCKER_BUILDKIT=0 docker compose up -d
   ```
2. Access the frontend at http://localhost:4173.
3. Use an IDE, like [VS Code](https://code.visualstudio.com/), to connect to the running container named `server`.
4. Navigate to the `/server/` directory to interact with the backend code.

### Without containers

>**Note**
>
>Python 3.10, Node.js 22, and Yarn 1.22 are required to run this demo

Be sure to export the necessary environment variables from above to interact with the LLM.

1. From the `/website/` directory run:
   ```
   yarn && yarn dev
   ```
   Access the frontend at http://localhost:4173. 
2. From the `/server/` directory run:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8080 --reload
   ```