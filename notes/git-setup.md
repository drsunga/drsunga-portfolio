                                     GIT SETUP: A STEP BY STEP GUIDE

### Prerequisite: GitHub Account

If you do not have a GitHub account, see **[How to SetUp a GitHub Account](https://www.codecademy.com/article/how-to-set-up-a-github-account)**. You are free to choose any username you like. Once completed you can now follow the steps below.

### Generating a New SSH Key

To authenticate Git operations over SSH, you'll need to generate a new SSH key on your local machine and add the public key to your GitHub account.

#### Steps to Generate a New SSH Key:

1. **Open your terminal**  and navigate to your home directory.
2. **Generate the SSH Key using the command below. Be sure to replace the email address with the one you used for your GitHub account.** <br>

        ssh-keygen -t ed25519 -C "your_email@example[.]com"

3. **Follow the prompts** by pressing **Enter** at each step to accept the default settings. This will create your new SSH Key pair.
4. Once completed, you can verify this by checking for the presence of the key files in the ./.ssh directory.
5. Add the generated public key to your GitHub account to enable secure access.

### Installing GitHub CLI

After completing the steps above, proceed with installing and configuring GitHub CLI. This step is necessary to enable authenticated access, allowing you to push changes in the main repository on hosted on GitHub.

1. Install GitHub CLI
   
        winget install GitHub.cli

        brew install gh
    
2. Authenticate with GitHub:

        gh auth login
    
3. When prompted select the following:
      * GitHub
      * HTTPS
      * Yes
      * Login with Browser

4. A browser window will open. Log in using your GitHub account.
5. Enter the **PIN** displayed in your terminal into the browser when prompted.
6. Click **Authorize** to complete the authentication process.
7. Confirm that you are successfully authenticated by running:
    
        gh auth status
    
Note: This ensures the GitHub CLI is properly set up and authenticated with your account.
