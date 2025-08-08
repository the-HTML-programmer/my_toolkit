from my_toolkit.math_ops.basic import add, subtract
from my_toolkit.string_ops.utils import reverse_string, count_vowels
from my_toolkit.file_ops.file_handler import write_to_file, read_from_file

if __name__ == "__main__":
    # Math examples
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))

    # String examples
    word = "Hello World"
    print("Reversed:", reverse_string(word))
    print("Vowel count:", count_vowels(word))

    # File examples
    write_to_file("sample.txt", "This is a test file.")
    print("File content:", read_from_file("sample.txt"))
