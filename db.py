import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except Exception as err:
        print(f'An error occurred: {err}')
    else:
        return response.text

def write_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except IOError as e:
        print(f'Failed to write to file {filename}. Error: {e}')

def main():
    url = 'http://example.com/data'
    filename = 'example.txt'

    data = fetch_data(url)
    if data:
        write_data_to_file(data, filename)

if __name__ == '__main__':
    main()