<table align="center"><tr><td align="center" width="9999">
<h1>Merlin - GPT4 Python Wizard</h1>
<img src="merlin.png" align="center" width="1000" alt="Project icon">
</td></tr></table>

<div align="center">

</div>


Built in Python and powered by ChatGPT, Merlin is a mystical Python code wizard that conjures the magical essence of 
programming by automating essential tasks in your Python files. Prepare to be enchanted as Merlin weaves its spells to 
generate docstrings, unit tests, and type hints - all with a flick of its metaphorical wand!

Simply run Merlin in the root of your Python project and it will automatically scan your project for Python files, and 
then generate docstrings, unit tests, and type hints for all of your functions and classes!

## Requirements
Before using Merlin, you'll need to ensure that your system meets the following prerequisites:

### Obtaining an OpenAI API Key and Creating a .env File
Merlin utilizes OpenAI's API to enhance its functionality. To access OpenAI's services, you will need an API key. 
Follow these steps to obtain an API key and create a .env file for your project:

#### Obtain an OpenAI API Key
1. Visit the [OpenAI website](https://openai.com/) and sign up for an account if you don't already have one. 
Note that you may be required to join a waitlist or subscribe to a paid plan, depending on the API access level you need.

2. Once you have an account and are logged in, navigate to the [API Keys page](https://platform.openai.com/account/api-keys) on the OpenAI platform.

3. Click on the "Create API Key" button, and a new API key will be generated for you. Make sure to copy the key and store it in a secure location, as you won't be able to view it again.

#### Create a .env File
In the root directory of your Merlin project, create a new file named .env. This file will store environment variables, 
including your OpenAI API key.

Open the .env file in a text editor and add the following line, replacing <your_api_key> with the API key you obtained 
from OpenAI:

```bash
OPENAI_API_KEY=<your_api_key>
```

Save the file and close the text editor.

Now, Merlin will automatically use your OpenAI API key when making requests to the API. Make sure to keep your .env 
file secure and avoid committing it to version control systems, as it contains sensitive information.

### Python
> ⚠️Python 3.6 or higher is required for Merlin. If you do not have Python installed or need to update it, visit the 
[official Python website](https://www.python.org/downloads/) to download and install the appropriate version for your 
operating system.

Verify your Python installation by opening a terminal (or command prompt) and running the following command:

```bash
python --version
```
This should display your installed Python version. Make sure it is 3.6 or higher.


### Docker
If you prefer using Docker to run Merlin, you will need to install Docker on your machine. For installation 
instructions, visit the [official Docker website](https://docs.docker.com/) and follow the guide for your operating system.

After installing Docker, verify that it is running correctly by opening a terminal (or command prompt) 
and executing the following command:

```
docker --version
```
This should display your installed Docker version. If you encounter any issues or need further guidance, 
consult the [Docker documentation](https://docs.docker.com/).

## Usage options

### Option 1: Docker

1. Build the Docker image:

```bash
docker build -t merlin .
```

2. Run the container:
This will mount the current directory as a volume in the container, so that Merlin can access your Python files.
Merlin will then go and automatically generate any missing dosctrings, type hints, and unit tests for any python files
that it finds in or under the current working directory.
```bash
docker run --rm -v $(pwd):/app merlin
```

### Option 2: Virtualenv

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On Linux or macOS
```bash
source /venv/bin/activate
```
- On Windows
```bash
.\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run Merlin
This will mount the current directory as a volume in the container, so that Merlin can access your Python files.
Merlin will then go and automatically generate any missing dosctrings, type hints, and unit tests for any python files
that it finds in or under the current working directory.
```bash
python merlin.py
```

### License
[View License](LICENSE.md)
