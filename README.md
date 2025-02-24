# CB_Selenium_Demo

#### This project demonstrates Selenium and the best practices of modern test automation, written in Python and targeting the Commerce Bank website(https://www.commercebank.com/). Without an account to log into this demonstration is seemingly trivial in that it showcases functionalities on less relevant aspects of the website, however these are the same techniques which will be used to verify critical UXs in a real test suite.

## Best Practices

*   **Page Object Model (POM):** The idea of the POM, for selenium, is to separate the code for tests from the code for each page of the web app being tested(specifically locators and common actions). This reduces code duplication(increasing D.R.Y.ness) and improves maintainability and readability.
*   **Effective Locators:** The most important part of writing resilient and maintainable Selenium test suites are locators or identifiers. These are how selenium tests actually pick out the elements of the html of the webpage to target, such as the text box to fill in your name or password, buttons to press, divs to check for specific text. The priority of these locators is: `ID > Name > CSS Selector > XPath` for element identification. Test IDs and names must be written into the src code, however CSS Selector and XPath can change drastically with minor revisions to the web app styling or layout.
*   **Explicit Waits:** Use `WebDriverWait` for robust and efficient waiting for elements, avoiding `implicit waits` and `time.sleep()`. WebDriverWait is capable of telling when the page has loaded completely and the locators mentioned above will be available, time.sleep() on the other hand may take longer than necessary or if the pages takes longer to load cause a falsely failing test.
*   **Data-Driven Testing:** Externalize test data (CSV, JSON, etc.) to run tests with multiple datasets easily. This is the basic Software Engineering wide idea of separating functionalities from data or inputs allowing for reusability, minimizing repetition and increasing maintainability.
*   **Screenshots on Failure and Critical Steps:** Automatically capture screenshots when tests fail for easier debugging and visual evidence or to verify the proper visual display of critical parts of the UX workflow being verified(think displaying the correct text and styling for transferring funds).
*   **Exception Handling:** Implement robust exception handling to prevent test crashes and ensure graceful failure.
*   **Browser Settings:** Set browser zoom to 100% and maximize the browser window for consistent test execution.
*   **Behavior Driven Development (BDD):** Explore BDD frameworks like Cucumber for plain language test cases and improved collaboration.
*   **Logging & Reporting:** Implement logging and reporting for detailed test execution information and summaries. If a test fails, we need to know exactly what happened and where things went awry.
*   **CI/CD:** Use tools like GitHub Actions to automatically execute Selenium test suites upon merging or committing code to critical branches, enabling early issue detection and simplifying the identification of problematic code changes.

## How To Run Tests
```
pytest tests/ --html=report.html
```