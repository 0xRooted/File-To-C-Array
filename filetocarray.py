import pathlib
from PIL import Image

class image_to_c_array:
    
    def __init__(self, image_path, output_path, format_bytes_count, char_array_name, include_header_guard=False, include_header_guard_name=None, reset_output_file=True):
        self.image_path = image_path
        self.output_path = output_path
        self.file_bytes = pathlib.Path(image_path).read_bytes()
        self.char_array_name = char_array_name
        self.format_bytes_count = format_bytes_count
        self.include_header_guard_name = include_header_guard_name
        self.include_header_guard = include_header_guard
        self.reset_output_file = reset_output_file
        self.file_bytes_len = 0
        for _b in self.file_bytes:
            self.file_bytes_len += 1
    
    def grab_string(self):
        if self.include_header_guard:
            data = "#ifndef {}\n#define {}\nunsigned char {}[{}] = {{\n\t".format(self.include_header_guard_name, self.include_header_guard_name, self.char_array_name,self.file_bytes_len)
        else:
            data = "unsigned char {}[{}] = {{\n\t".format(self.char_array_name, self.file_bytes_len)
        count = 0
        for x in self.file_bytes:
            if count == self.format_bytes_count:
                data += "\n\t"
                count = 0
            temp_data = str(hex(x))
            if len(temp_data) == 3:
                temp_data = temp_data.replace("0x", "0x0")
            data += temp_data.upper() + ", "
            count += 1
        if self.include_header_guard_name:
            data += "\n};\n#endif\n"
        else:
            data += "\n};\n\n"
        
        return data
    
    def save(self):
        if self.reset_output_file:
            open(self.output_path, 'w+').close()
        
        with open(self.output_path, 'a+') as f:
            f.write(self.grab_string())
