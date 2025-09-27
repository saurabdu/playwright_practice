# from requests import *
# import json
#
#
# def test_practice():
#     response = get("https://api.restful-api.dev/objects?id=3&id=5&id=10")
#     print(response.status_code)
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json()['page'] == 2
#     assert len(response.json()['data']) == 6
#
#
# def test_post():
#     requestBody = {
#         "name": "Apple MacBook Pro 16",
#         "data": {
#             "year": 2019,
#             "price": 1849.99,
#             "CPU model": "Intel Core i9",
#             "Hard disk size": "1 TB"
#         }
#     }
#     response = post("https://api.restful-api.dev/objects", data=json.dumps(requestBody))
#     print(response.status_code)
#     print(response.json())
#     assert response.status_code == 201
#     assert response.json()['name'] == "Apple MacBook Pro 16"
#     assert response.json()['data']['price'] == "849.99"


import functools
import logging

# Configure the basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_class_method(func):
    """
    A decorator that logs the class and method name before calling the method.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Access the class and method names from the `self` object and `func`
        class_name = self.__class__.__name__
        method_name = func.__name__

        # Log the message with the extracted names
        logging.info(f"Class: {class_name}, Method: {method_name} - Starting...")

        try:
            # Call the original method
            result = func(self, *args, **kwargs)
            logging.info(f"Class: {class_name}, Method: {method_name} - Finished successfully.")
            return result
        except Exception as e:
            # Log any exceptions that occur during execution
            logging.exception(f"Class: {class_name}, Method: {method_name} - An error occurred: {e}")
            raise

    return wrapper


# Define a class with a decorated method
class TestRunner:
    def __init__(self, name):
        self.name = name

    @log_class_method
    def test_run(self, test_case_id):
        """Simulates running a test with a specific ID."""
        print(f"Executing test '{test_case_id}' for runner '{self.name}'...")
        # Simulates a potential operation or check
        if test_case_id == "critical_failure":
            raise ValueError("Test failed due to a critical error.")
        return f"Test '{test_case_id}' completed successfully."


# --- Usage example ---
runner = TestRunner("IntegrationTestRunner")

# Call the decorated method on the instance
try:
    result = runner.test_run("login_page")
    print(f"Result: {result}\n")
except Exception as e:
    print(f"Caught exception: {e}\n")

# Trigger the error condition to demonstrate logging exceptions
try:
    runner.test_run("critical_failure")
except ValueError as e:
    print(f"Caught expected exception: {e}\n")
