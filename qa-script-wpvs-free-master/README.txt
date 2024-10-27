-------------------------- WCFE-FREE AUTOMATION SCRIPT RUN STEPS --------------------------
PRE-REQUISITES:

    1) Plugin must be installed and activated. Uninstall any other active plugins woocommerce plugins.
    2) Respective browser must be installed to run script in it.
    3) Update Chrome browser to latest version.
    4) Create .env file and save the datas by referring env_sample.txt in project folder for your website.


1. If python is not installed --->
    Install Python and give its path in User variables --> Path  (while installing check add to path).
    Check if python is installed using python –version or py --version

2. If git is not installed --->
    Install git and include C:\Program Files\Git\cmd and C:\Program Files\Git\bin paths in System variables --> Path.
    Check if git is installed using git --version

3. Create and activate virtual environment -->
    (can change 'env' to any desired name)

    For macOS:
    1) python3 -m venv env
    2) source env/bin/activate

    For Windows:
    1) py -m venv env
    2) .\env\Scripts\activate

4. To clone the git repository of the automation script,  -->
    Run the command --> git clone git@github.com:Themehigh/qa-script-wpvs-free.git

5. Switch to newly created folder using command -->
    cd qa-script-wpvs-free

6. Install the required plugins to run the automation script using command -->
    pip install -r "requirements.txt"

7. To run in Chrome and generate report, run command -->
    py.test -v -s tests

8. To run in Firefox and generate report, run command -->
    py.test -v -s tests --browser_name firefox

9. To run in Edge and generate report, run command ->
    py.test -v -s tests --browser_name edge
