# python-challenge

Hi All,

1. Please find the URL containing the link to Git Hub repository containing the Python home-work solution:

    Repo for Python Homework
        https://github.com/anand-sharan/python-challenge

2. Please find the steps of Python homework solution:

    PyBank
    -------
    Python script for analyzing the financial records of a company. Provided with finacial data set budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.

    The Python script analyzes the financial records calculates each of the following:

    * The total number of months included in the dataset

    * The net total amount of "Profit/Losses" over the entire period

    * The average of the changes in "Profit/Losses" over the entire period

    * The greatest increase in profits (date and amount) over the entire period

    * The greatest decrease in losses (date and amount) over the entire period

    Steps to execute the script and validate the solution:

    Step 1. Download the git hub repository to local folder on your computer
    Step 2. Change your working directory to `~/python-challenge/PyBank`
    Step 3. Ensure python is activated by running command `source activate PythonData`
    Step 4. Execute command `python main.py` to check the solution
    Step 5. Validate output displayed on screen for `Financial Analysis`
    Step 6. Change your working directory to `~/python-challenge/PyBank/analysis`
    Step 7. Open file output.csv in Excel or any text editor to view solutions output file


    PyPoll
    -------
    Python Script for analysis a set of poll data. Provided a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate.

    The Python script analyzes the votes and calculates each of the following:

    * The total number of votes cast

    * A complete list of candidates who received votes

    * The percentage of votes each candidate won

    * The total number of votes each candidate won

    * The winner of the election based on popular vote.

        Steps to execute the script and validate the solution:

        Step 1. Download the git hub repository to local folder on your computer
        Step 2. Change your working directory to `~/python-challenge/PyPoll`
        Step 3. Ensure python is activated by running command `source activate PythonData`
        Step 4. Execute command `python main.py` to check the solution
        Step 5. Validate output displayed on screen for `Election Results`
        Step 6. Change your working directory to `~/python-challenge/PyPoll/analysis`
        Step 7. Open file output.csv in Excel or any text editor to view solutions output file

    PyParagraph
    -------
    Python script to automate the analysis of passage using  metrics. Script will need to do the following:

        * Import a text file filled with a paragraph of your choosing.

        * Assess the passage for each of the following:

        * Approximate word count

        * Approximate sentence count

        * Approximate letter count (per word)

        * Average sentence length (in words)

        Steps to execute the script and validate the solution:

        Step 1. Download the git hub repository to local folder on your computer
        Step 2. Change your working directory to `~/python-challenge/PyParagraph`
        Step 3. Ensure python is activated by running command `source activate PythonData`
        Step 4. Execute command `python main.py` to check the solution
        Step 6. Change your working directory to `~/python-challenge/PyPoll/output`
        Step 7. Open file output_1.csv in Excel or any text editor to view solutions output file
        Step 8. Change your working directory to `~/python-challenge/PyParagraph`
        Step 9. Change paragraph_1.txt to paragraph_2.txt on line 16
        Step 10. Execute command `python main.py` to check the solution
        Step 11. Change your working directory to `~/python-challenge/PyPoll/output`
        Step 12. Open file output_2.csv in Excel or any text editor to view solutions output file

    PyBoss
    ------
        Python script able to convert your employee records to the required format. Script will need to do the following:

        * Import the `employee_data.csv` file, which currently holds employee records like the below:

        ```csv
        Emp ID,Name,DOB,SSN,State
        214,Sarah Simpson,1985-12-04,282-01-8166,Florida
        15,Samantha Lara,1993-09-08,848-80-7526,Colorado
        411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
        ```

        * Then convert and export the data to use the following format instead:

        ```csv
        Emp ID,First Name,Last Name,DOB,SSN,State
        214,Sarah,Simpson,12/04/1985,***-**-8166,FL
        15,Samantha,Lara,09/08/1993,***-**-7526,CO
        411,Stacy,Charles,12/20/1957,***-**-8526,PA
        ```

        * In summary, the required conversions are as follows:

        * The `Name` column should be split into separate `First Name` and `Last Name` columns.

        * The `DOB` data should be re-written into `MM/DD/YYYY` format.

        * The `SSN` data should be re-written such that the first five numbers are hidden from view.

        * The `State` data should be re-written as simple two-letter abbreviations.

        Steps to execute the script and validate the solution:

        Step 1. Download the git hub repository to local folder on your computer
        Step 2. Change your working directory to `~/python-challenge/PyBoss`
        Step 3. Ensure python is activated by running command `source activate PythonData`
        Step 4. Execute command `python main.py` to check the solution
        Step 6. Change your working directory to `~/python-challenge/PyBoss/output`
        Step 7. Open file output.csv in Excel or any text editor to view solutions output file

3. Request for you gracious feedback.

Thanks & Regards,
Anand Sharan

