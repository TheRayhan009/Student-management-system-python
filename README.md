# Student Data Management System

This script is designed to manage student data, including adding, deleting, checking, and displaying student records. It includes an admin password feature to ensure secure access.

## Features

### Admin Password Setup

- **Automatic Password Creation**: If the `adminpass.txt` file does not exist, the script will create it and write a default password (`i_love_rayhan`). This ensures that there is always a password file for authentication.
- **Secure Password Input**: The script uses the `getpass` module to securely input the admin password, which hides the input for security.

### Admin Password Verification

- **Password Prompt**: The script prompts the user to enter the admin password.
- **Verification**: The entered password is compared with the stored password in the `adminpass.txt` file. If the password is correct, the user gains access to the admin functionalities.

### Main Menu

- **Interactive Choices**: The script presents a menu with options for various student data management tasks. Users can select actions by entering the corresponding codes.

### Student Data Management

1. **Add New Student Data**:
    - **Input Prompt**: Prompts the user to enter student name, class, and roll number.
    - **Data Storage**: Appends the new student data to the `studentdatatherayhanpy.txt` file.
    - **Return to Previous Page**: Users can enter `/` to return to the previous page.

2. **Delete Student Data**:
    - **Input Prompt**: Prompts the user to enter the student name, class, and roll number.
    - **Data Deletion**: Reads the file, removes the matching student record, and rewrites the file without the deleted record.
    - **Return to Previous Page**: Users can enter `/` to return to the previous page.

3. **Check Student Data**:
    - **Input Prompt**: Prompts the user to enter the student name, class, and roll number.
    - **Data Verification**: Checks if the entered student data exists in the file and prints the result.
    - **Return to Previous Page**: Users can enter `/` to return to the previous page.

4. **Display All Student Data**:
    - **Data Display**: Reads and prints all student records from the file.

## How to Run the Script

1. **Ensure Python Installation**: Make sure Python is installed on your system.
2. **Save the Script**: Save the script as a `.py` file.
3. **Run the Script**: Use a Python interpreter to run the script.

    ```bash
    main.py
    ```

## File Structure

- **Script File**: The main Python script that contains the code for managing student data.
- **Data File (`studentdatatherayhanpy.txt`)**: Stores the student records.
- **Password File (`adminpass.txt`)**: Stores the admin password.

## Future Enhancements

- **Password Management**: Implement functionality to change the admin password.
- **Enhanced Validation**: Add validation checks for user inputs to ensure data integrity.
- **Improved User Interface**: Develop a graphical user interface (GUI) for a better user experience.
- **Database Integration**: Integrate with a database system for more robust data storage and management.

## Security Considerations

- **Password Protection**: Ensure the `adminpass.txt` file is securely stored and not accessible to unauthorized users.
- **Secure Input**: Use secure methods for password input and data handling to prevent unauthorized access.

## Conclusion

This script provides a basic but functional system for managing student data with an emphasis on secure access through an admin password. It is a foundational tool that can be expanded and improved upon to meet more complex requirements in the future.

### Made By THERAYHAN PY.
