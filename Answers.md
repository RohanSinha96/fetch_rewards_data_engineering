# Answers to Questions
**How would you deploy this application in production?**<br>
**Ans** – Data Masking in a Separate Environment, that is , by deploying the application and data masking component in different environments as the data is sensitive. The 2 components are kept separate for security reasons. 

**What other components would you want to add to make this production ready?**<br>
**Ans** -  Security component is required as data can be retrieved before masking and can be dangerous for the users

**How can this application scale with a growing dataset.**<br>
**Ans** -  Adding more servers or memory can help with growing dataset. Data compression can also be used for fields like user ID which are not used in the process.

**How can PII be recovered later on?**<br>
**Ans** – We can create a separate application that can retrieve the original data. Since current encoding is SHA-265 it is not reversible. However, there are other approaches such as adding random noise or encryption which are reversible.

**What are the assumptions you made?**<br>
**Ans** – I have made the following assumptions:<br>
- Records that do have incorrect data (for example a field is missing) are ignored
- App version is of format X.Y.Z (for example 2.15.3). However, the field in the table is of type Integer and hence only first part, that is X, is considered (2 in the example given)
- create_date is retrieved from datetime as the date the code is executed


add