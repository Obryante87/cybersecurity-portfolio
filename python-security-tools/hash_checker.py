import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    """
    Calculate the hash value of a file.

    Supported algorithms:
    - md5
    - sha1
    - sha256
    """

    try:
        hash_function = hashlib.new(algorithm)

        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_function.update(chunk)

        return hash_function.hexdigest()

    except FileNotFoundError:
        return "Error: File not found."

    except ValueError:
        return "Error: Unsupported hash algorithm."


if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    algorithm = input("Enter hash algorithm md5, sha1, or sha256: ").lower()

    result = calculate_hash(file_path, algorithm)
    print(f"{algorithm.upper()} hash: {result}")
