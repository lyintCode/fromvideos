import re

def transponerer_file(file):
    final = []
    with open(file, 'r') as f:
        for line in f:
            output = ""
            line_lenght = len(line) - 1
            
            for i in range(0, line_lenght):
                if i%2 == 0:
                    output += line[i]
            
            final.append(output)
    return final

def transponerer_text(text):

    text = text.group(0)
    output = ""
    text_lenght = len(text) - 1
    
    for i in range(0, text_lenght):
        if i%2 == 0:
            output += text[i]
    
    return output.strip()

def transponerer_file_auto(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        pattern = re.compile(r"Transponerer\s'.*?'")

        for line in lines:
            if pattern.search(line):
                inside_pattern = re.compile(r"'.*?'")
                processed_line = inside_pattern.sub(transponerer_text, line)
                print(f"{processed_line.strip()}'")
            else:
                print(line.strip())

def prefills_text(text):
    if len(text) > 1:
        bytes_array = bytearray(len(text) // 2)

        for i in range(0, len(text), 2):
            bytes_array[i // 2] = int(text[i:i + 2], 16)
            bytes_array[i // 2] ^= 165

        decoded_text = bytes_array.decode('ascii')
        return decoded_text

def prefills_auto(file):
    with open(file, 'r') as f:
        hex_pattern = re.compile(r"Prefills\s+'([0-9A-F]+)'")
        for line in f:
            if re.search(hex_pattern, line):
                start_index = line.find("'") + 1
                end_index = line.rfind("'")
                hex_sequence = line[start_index:end_index]
                result = prefills_text(hex_sequence)
                print(line.replace(hex_sequence, result))
            else:
                print(line.strip())

if __name__ == '__main__':
    prefills_auto('3_2.ps1')
