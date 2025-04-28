# FastAPI Project with ngrok

This repository contains a FastAPI application. To expose the FastAPI app publicly using **ngrok**, follow the instructions below.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn (for serving FastAPI)
- ngrok (to expose the app publicly)

## Installation

### Step 1: Clone the repository

Clone the FastAPI repository to your local machine:

```bash
git clone https://github.com/AdbulrhmanEldeeb/smart_resever
cd smart_resever
```

## Step 2: Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```
### Step 3: Install ngrok

To expose your FastAPI app to the internet, you'll need ngrok.

#### On Linux/macOS:

1.  **Download ngrok:**
    Get the latest version from the [official website](https://ngrok.com/download). For example:
    ```bash
    wget [https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz)
    ```

2.  **Extract the downloaded file:**
    ```bash
    tar -xvzf ngrok-v3-stable-linux-amd64.tgz
    ```
    *(Replace the filename if you downloaded a different version/architecture)*

3.  **Move the ngrok binary to your PATH:**
    Move the extracted `ngrok` executable to a directory included in your system's PATH, like `/usr/local/bin`:
    ```bash
    sudo mv ngrok /usr/local/bin
    ```

4.  **Verify the installation:**
    ```bash
    ngrok version
    ```

#### On Windows:

1.  **Download ngrok:**
    Download the Windows zip file from [ngrok.com/download](https://ngrok.com/download).

2.  **Extract and Place:**
    Extract the `.zip` file. Place the `ngrok.exe` file in a folder that is either in your system's PATH or easily accessible from your command prompt/terminal.

3.  **Verify (Optional but recommended):**
    Open a terminal in the directory where you placed `ngrok.exe` (or anywhere if it's in your PATH) and run:
    ```bash
    ngrok version
    ```

### Step 4: Add ngrok Authentication Token

To use more features and longer tunnel durations, authenticate your ngrok client.

1.  **Get your token:**
    Sign up or log in to your [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to find your auth token.

2.  **Add the token:**
    Run the following command, replacing `YOUR_NGROK_AUTH_TOKEN` with the actual token from your dashboard:
    ```bash
    ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
    ```

### Step 5: Run FastAPI locally

Start your FastAPI application using Uvicorn. Make sure you are in the directory containing your `main.py` file (or equivalent).

```bash
cd src 
```
run the app
```bash
uvicorn main:app --port 5000 --reload
```

Your FastAPI app should now be running locally, typically on http://127.0.0.1:5000. Check your terminal output for the exact address and port.

## Step 6: Expose the FastAPI app using ngrok
Open a new terminal window (leave Uvicorn running in the first one).

Start ngrok tunnel:
Run the following command, replacing 8000 if your FastAPI app is running on a different port:

```bash
ngrok http 5000
```
Get the public URL:
ngrok will give you a public url with a format like this:
https://"unique_id".ngrok-free.app

copy and paste it in the streamlit ui 

then choose destination and the speed the the data will be sent to the server