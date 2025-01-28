import subprocess
import requests
import base64
import os

subscription_url = 'https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/splitted/subscribe'

input_file = 'config.txt'
output_file = 'valid_configs'
encoded_output_file = 'encoded_valid_configs'


if os.path.exists(input_file):
    os.remove(input_file)  
    print(f"{input_file} has been removed.")


response = requests.get(subscription_url)
print(f"HTTP Response Code: {response.status_code}")

if response.status_code == 200:
    try:
        decoded_content = base64.b64decode(response.text).decode('utf-8')

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(decoded_content)  
        print(f"Decoded subscription links saved to {input_file}")
    except Exception as e:
        print(f"Error while decoding or saving content: {e}")
else:
    print(f"Failed to retrieve the subscription link, status code: {response.status_code}")


try:

    result = subprocess.run(['./xray-knife', 'net', 'http', '--file', input_file,
                             '-o', output_file, '-a', '10000', '-s' , '-t', '150', '-u' , 'http://connectivitycheck.gstatic.com/generate_204' ,'-e'],
                            capture_output=True, text=True)

    print(f"Test Results:\n{result.stdout}")

    if result.returncode == 0:
        print(f"Test completed successfully. Valid configs saved to {output_file}")
    else:
        print(f"Error during testing: {result.stderr}")
except Exception as e:
    print(f"Error executing xray-knife command: {e}")

try:
    with open(output_file, 'r', encoding='utf-8') as f:
        valid_configs = f.read()

    encoded_content = base64.b64encode(valid_configs.encode('utf-8')).decode('utf-8')

    with open(encoded_output_file, 'w', encoding='utf-8') as f:
        f.write(encoded_content)

    print(f"Encoded valid configs saved to {encoded_output_file}")
except Exception as e:
    print(f"Error while encoding valid configs: {e}")


if os.path.exists(input_file):
    os.remove(input_file)  
    print(f"{input_file} has been removed.")

if os.path.exists(output_file):
    os.remove(output_file) 
    print(f"{output_file} has been removed.")
