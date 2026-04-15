"""
Part 05: Error handling with file operations.
"""

# What the code  demonstrates:

# Case 1 (file exists): reads sample_data.txt and prints content.
# Case 2 (changed/wrong filename): tries sample_data_typo.txt, catches exception.
# Uses finally in both cases, so cleanup message always runs and file is closed when needed.
# When to use finally:

# Use finally when something must always happen, no matter success/failure.
# Common examples: close files, close DB connections, release locks, cleanup temp resources.

from pathlib import Path


def read_file_with_handling(file_name: str) -> None:
    """Read and print a file, handling common file errors."""
    file_path = Path(__file__).parent / file_name
    file_obj = None

    try:
        print(f"\nTrying to open: {file_path.name}")
        file_obj = open(file_path, "r", encoding="utf-8")
        content = file_obj.read()
        print("File content:")
        print(content)

    except FileNotFoundError:
        print(f"FileNotFoundError: '{file_path.name}' was not found.")
    except OSError as err:
        # OSError covers OS-level file issues (permissions, invalid path, etc.).
        print(f"OSError while opening '{file_path.name}': {err}")
    finally:
        # finally runs no matter what (success, handled error, or unhandled error).
        if file_obj is not None and not file_obj.closed:
            file_obj.close()
            print("finally: file was open, now closed.")
        else:
            print("finally: no open file to close.")


def run_demo() -> None:
    # Situation 1: File exists, content will be printed.
    read_file_with_handling("sample_data.txt")
    
    # You can comment out the first read_file_with_handling and run the second one to see the error handling in action.
    # Situation 2: Changed file name (wrong/missing file), except + finally run.
    read_file_with_handling("sample_data_typo.txt")


def validate_port(port: int) -> int:
    # raise means: stop here immediately if input is invalid.
    if not (0 <= port <= 65535):
        raise ValueError(f"Invalid port: {port}")
    return port


def raise_value_error_examples() -> None:
    print("\n--- raise ValueError examples ---")

    # Case 1: Matching except exists -> Python jumps to this except block.
    try:
        validate_port(99999)  # invalid, so ValueError is raised
    except ValueError as err:
        print(f"Case 1 handled: {err}")

    # Case 2: No matching except in this scope -> if we do not catch it,
    # Python shows traceback and program stops.
    # We wrap that call in another try here so this demo file can continue running.
    try:
        try:
            validate_port(-10)  # raises ValueError
        except TypeError:
            print("This will not run (error type is not TypeError).")
    except ValueError as err:
        print(f"Case 2 would stop program without this outer handler: {err}")

    # Case 3: Valid value -> no raise, function continues normally.
    ok_port = validate_port(8080)
    print(f"Case 3 valid port: {ok_port}")


# Why is bare `except:` without logging dangerous in a deployment script? / “Why is it risky to write except: (catch everything) and also not print/log the error, especially in deployment code?”
#Answer: It will silently swallow errors, making it difficult to debug and troubleshoot issues.

# Bad pattern:

# try:
#     deploy()
# except:
#     pass   # hides everything
# # Better pattern:


# try:
#     deploy()
# except Exception as err:
#     print(f"Deployment failed: {err}")   # or proper logger
#     raise  # re-raise so pipeline knows it failed

# When does `finally` run — only on success, only on error, or always?
#Answer: `finally` runs always, no matter if the `try` block succeeds or fails.

#  If `int("x")` runs inside `try` and raises `ValueError`, and you have `except TypeError`, what happens?
#Answer: The `ValueError` will be raised and the program will crash.
# Example: 
try:
    int("x")
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'x'")

# try:
#     num = int("x")          # raises ValueError
#     print("converted:", num)
# except TypeError:
#     print("Caught TypeError")

# HTTP request fails with timeout. Which is better: catch a broad `Exception` everywhere, or catch the library’s specific timeout exception type?
#Answer: Catch the library’s specific timeout exception type.
# Example:
# try:
#     request()
# except TimeoutError:
#     print("Timeout: request took too long")
# except Exception as err:
#     print(f"Other error: {err}")


# It is good practice to use `except: pass` so the script always exits with code 0.
#Answer: No, it is not good practice to use `except: pass` so the script always exits with code 0.
# Example:
# try:
#     deploy()
# except:
#     pass   # hides everything


if __name__ == "__main__":
    run_demo()
    raise_value_error_examples()
