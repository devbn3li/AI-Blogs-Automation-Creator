# Project Setup Instructions

This README provides the instructions to clone and run the project locally. Follow the steps below to set up the project environment and run the application successfully.

## Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **virtualenv** (to create a virtual environment)
- **Azure Subscription** (with access to Azure AI services if applicable)
- **Git**

## Cloning the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/devbn3li/AI-Blogs-Automation-Creator
   ```

4. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

## Setting Up the Virtual Environment

1. Create a virtual environment in the project directory:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

## Installing Dependencies

1. Ensure you are in the project directory with the virtual environment activated.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Azure AI Configuration

1. Ensure you have the following Azure AI details:
   - **Connection String**
   - **AI Model Name** (e.g., `gpt-4o-mini` or another model used in the project)
2. Add your Azure configuration in the project files or as environment variables. For example:

   ```bash
   export AZURE_CONNECTION_STRING="your-connection-string"
   export AZURE_AI_MODEL="gpt-4o-mini"
   ```

### Setting Up Environment Variables

1. Create a `.env` file in the root directory.
2. Add the following content to the `.env` file:

   ```env
   PROJECT_CONNECTION_STRING="your-azure-connection-string-here"
   ```

3.Replace `"your-azure-connection-string-here"` with your actual Azure connection string.
This setup keeps your sensitive information secure and separates configuration from the code.

## Running the Application

1. Run the main script:

   ```bash
   python3 main.py
   ```

2. Follow any on-screen instructions (e.g., input your company data).

## Output

The generated blog files will be saved in the `output/` directory within the project folder. Each blog will be saved as a Markdown (`.md`) file, with filenames generated based on the blog titles.

## Project Structure

Here is an overview of the project structure:

``` Markdown
project-directory/
├── config.py           # Configuration layer (templates, services, rules)
├── logic.py            # Logic layer (content generation, SEO, linking)
├── model.py            # AI model layer (OpenAI integration)
├── main.py             # Entry point for the application
├── output/             # Directory for generated blog files
├── requirements.txt    # Project dependencies
└── README.md           # Instructions to set up and run the project
```

## Troubleshooting

- **Virtual Environment Activation Issues**:
  Ensure you have the correct Python version and that `virtualenv` is installed.

- **Dependency Issues**:
  Double-check the `requirements.txt` file and ensure all required libraries are installed.

- **Azure AI Errors**:
  Verify your connection string and model configurations. Ensure your Azure subscription has access to the AI services being used.

## Contributions

Feel free to fork this repository and submit pull requests for enhancements or bug fixes. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
