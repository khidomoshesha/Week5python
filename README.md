# Week5python

# This README file provides a combined overview and instructions for two Python programs: `Book.py` and `Animal.py`, both       demonstrating fundamental concepts of object-oriented programming.

### Running the Book Code (`book.py`)

1.  **Save the file:** Ensure that the code for the `Book` class is saved in a file named `book.py` in your local repository.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved `book.py` using the `cd` command. For example:
    ```bash
    cd path/to/your/repository
    ```
    (Replace `path/to/your/repository` with the actual path to where you've saved the file).
4.  **Execute the script** using the Python interpreter. **Type the following command and press Enter:**
    ```bash
    python book.py
    ```
    (You might need to use `python3` instead of `python` if your system uses `python3` to invoke Python 3).

#### Expected Output (`book.py`)

When you run the `book.py` script using the command `python book.py` (or `python3 book.py`), you should see the following output printed to your terminal:

You are absolutely right! My apologies for the slight oversight in the book.py README instructions. Let's refine that section to be crystal clear about the command to run.

Here's the updated section for running book.py that you can replace in your README file:

Markdown

### Running the Book Code (`book.py`)

1.  **Save the file:** Ensure that the code for the `Book` class is saved in a file named `book.py` in your local repository.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved `book.py` using the `cd` command. For example:
    ```bash
    cd path/to/your/repository
    ```
    (Replace `path/to/your/repository` with the actual path to where you've saved the file).
4.  **Execute the script** using the Python interpreter. **Type the following command and press Enter:**
    ```bash
    python book.py
    ```
    (You might need to use `python3` instead of `python` if your system uses `python3` to invoke Python 3).

#### Expected Output (`book.py`)

When you run the `book.py` script using the command `python book.py` (or `python3 book.py`), you should see the following output printed to your terminal:

Book 1:
Title: The Hitchhiker's Guide to the Galaxy
Author: Douglas Adams
Publication Year: 1979

Book 2:
Title: Pride and Prejudice
Author: Jane Austen
Publication Year: 1813

Fiction Book:
Title: To Kill a Mockingbird
Author: Harper Lee
Publication Year: 1960
Genre: Classic Literature

This output shows the information for two `Book` objects and one `FictionBook` object, demonstrating the attributes and the overridden method from the parent class.

### Running the Animal Code (`animal.py`)

1.  **Save the file:** Make sure the code for the `Animal`, `Dog`, `Bird`, and `Fish` classes is saved in a file named `animal.py` in your local repository.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved `animal.py` using the `cd` command. For example:
    ```bash
    cd path/to/your/repository
    ```
    (Replace `path/to/your/repository` with the actual path).
4.  **Execute the script** using Python. **Type the following command and press Enter:**
    ```bash
    python animal.py
    ```
#### Expected Output (`animal.py`)

When you run the `animal.py` script using the command `python animal.py` (or `python3 animal.py`), you should see the following output:

Running on four legs.
Flying through the air.
Swimming in the water.

This output demonstrates polymorphism, where the `move()` method is called on different animal objects, and each object executes its specific implementation of the `move()` method.