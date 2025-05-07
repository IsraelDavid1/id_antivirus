# Phishing Detector

## About

**Phishing Detector** is the first module of the **id_antivirus** project, but it can also be used as a standalone tool.  
This tool analyzes URLs and uses machine learning to detect similarities with known phishing websites, returning a response indicating whether the URL might be malicious.

---

## Features

- **SSL Certificate Verification**: Opens a connection to check the validity of the SSL certificate.
- **URL Pattern Analysis**: Looks for suspicious words and abnormal patterns in the URL structure.

---

## How to Use

1. **Prerequisites**:
    - Make sure Python is installed on your system. If not, download it from [python.org](https://www.python.org/).
    - Install the required packages using the `requirements.txt` file. If you're using Termux, use `requirements_termux.txt`:
    ```bash
    pip install -r /path/to/requirements.txt
    ```

2. **Running the Program**:
    - Open your terminal or command prompt.
    - Navigate to the directory where `main.py` is located.
    - Run the program:
    ```bash
    python main.py
    ```

3. **Output**:
    - The program will ask for a URL or "q" to quit.
    - It will analyze the URL and display an alert if it suspects phishing.
    - If the scheme (`http://` or `https://`) is missing, it will notify you.
    - The program will keep running until you enter "q".

---

## Example Output

```bash
put the URL (or q to quit):  https://www.google.com
no phishing detected
detection time 3.38 seconds
```

---

## Motivation

I started this project to improve my skills in Python and machine learning.  
As a student passionate about both Python and cybersecurity, I thought: *Why not combine them?*  
It has been a great learning experience, and I hope this tool helps others improve their digital safety and inspires developers to grow their own skills.

---

## Contributing

If you'd like to contribute, feel free to fork the repository and open a pull request.  
You can help by:

- Adding new features (e.g., more data for model training)
- Improving the code or performance
- Fixing bugs or typos
- Translating the tool to other languages

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute it as you like.

