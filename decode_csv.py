import argparse
import html

def decode_csv(input_file, output_file):
    try:
        # Open the file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Decode any HTML entities (e.g., &#x644;)
        decoded_content = html.unescape(content)

        # Save the decoded content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_content)

        print(f"Decoded file saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except UnicodeDecodeError:
        print(f"Error: Failed to decode the file {input_file}. Check the file's encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Decode Arabic characters in CSV files.")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('output_file', help="Path to save the decoded CSV file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the decode function with the provided arguments
    decode_csv(args.input_file, args.output_file)
