# Blood_Donation_Management_System

![Logo (2) (2)](https://user-images.githubusercontent.com/85924566/128607590-b60d57ed-be85-4e1c-8c50-151ec2f61c53.png)



The **Blood_Donation_Management_System** website is designed to help the donors to donate blood to their nearest blood camps and the persons who need blood to receive required blood group from the neareblood bank and active donors.

## Instructions For Project Setup

- **Step 1.**
You can directly download the zip file or follow next 2 steps to clone the repo.
Install latest version of git. Open the above github repository link in browser. Click on the code button
and copy HTTPS link.

- **Step 2.**
Create new folder and open git bash inside that folder write command-
```
git clone https://github.com/anjali7786/Sleep-Tracker.git
```
- **Step 3.**
  - Install latest version of python and a code editor (Pycharm or Visual Studio Code).
  - Download & Install MYSQLCLIENT For Python : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient open this link and under MySQLclient select the wheel according to your python version and 32/64 bit windows system. 
  '''
   cmd.

- **Step 4.**
   Open the project files in the code editor. Open `main.py` file and if your MySQL username and password are not **root** then you can replace the username and password written in `main.py` file with your MySQL username and password.

- **Step 5.**
  **Installing Packages**

  For Visual Studio Code do the following:
   - Open **New Terminal**

    ![image](https://user-images.githubusercontent.com/64724039/117951623-f7f91e00-b331-11eb-8c7a-2baba835b685.png)

   - And now run the following commands in the terminal:
    ```
    python -m venv env
    Set-ExecutionPolicy Unrestricted -Scope Process
    env\scripts\activate
    pip install flask
    $env:FLASK_APP = "main"
    pip install bcrypt
    pip install flask_mysqldb
    pip install flask_mail
    flask run
    ```
   
   - Or run `requirements.txt` file :
    ```
    pip install -r requirements.txt
    
    ```
    
  For Pycharm code editor do the following:
   - Open the terminal

   - And run the following commands:
    ```
    pip install flask,
    pip install bcrypt,
    pip install flask_mysqldb,
    pip install flask_mail
    
## Snapshots

- Homepage

- User Registration Page
**User can register themselves with our website to donate blood at the available blood banks or to search for required blood groups from blood banks.**
- Blood Bank Registration Page
**Blood Banks can register themselves with us using the registration page where they need to fill the required details such as license number, etc.**
- User Login Page
**Page for user login**
- Admin Login Page
**Admin can login using admin credentials.**
- Blood Bank Login Page
**Login page for Blood Banks**
- Edit User Profile Page
**Users can edit their profile details on this page.**
- Blood Bank Profile Page
**It displays the inforation about the particular blood bank after logging in to the website and the blood bank can edit their profile details here.**
- Search Blood Banks Page
**User can search for blood banks in their area by filling out the location details. The page will show them a list of all the blood banks available in that particular region.**
- Blood Availability Page
**Users after logging in with their credentials, can search for required blood group in the area nearest to them.**
- Edit blood Stock Page
**Admin can edit the blood stock manually to the database of the website in case of any dispensaries**
- Admin Dashboard Page
**After logging in, admin is redirected to this page from where he can go to the User Message to Admin page or to Verification Requests page.**
- Verification Requests Page
**The admin can approve or reject the requests of blood banks or user from this page.**
- Contact Page
**Users can send their feedbacks/messages to admin of the website using thiis page.**
- User Message to Admin Page
**Admin can read the messages/feedbacks sent by the user to him on the user feedbacks page.**
- Non-Eligibility Page
**It shows the required conditions that are needed by a persson to be eligible to donate bloood to the blood banks.**
- Donor List
**It shows the list of active donors along with their other necessary information.**






- Sign Up page

**To activate other pages you have to fill sign up form**
![Screenshot (398)](https://user-images.githubusercontent.com/85924566/128654101-e616778c-3fa4-410f-9a97-c4cbfd874ba4.png)

- Login page

**Once you logout then to visit website again  you don't need to fill signup form again and again, just fill entries in login in form.**
**It will automatically filled by system if you have saved password in the beginning .**

![Screenshot (400)](https://user-images.githubusercontent.com/85924566/128654136-d9013bac-93ab-4e67-be46-ad8abcd8ec66.png)

   
- Record page in Track your sleep
**It is compulsory to fill all the entries in Track your nap form**

![Screenshot (404)](https://user-images.githubusercontent.com/85924566/128654833-10a14dba-0d71-4d32-8c2e-2d2770855973.png)

- Analyze your sleep in Track your sleep

![Screenshot (74)](https://user-images.githubusercontent.com/85924566/128641275-fdc56ccd-009c-4357-a690-b46cc78e039c.png)

- Unable to sleep

**To zoom the content of Yoga, Meditation, Food and Habbits hover on respective image**

![unable](https://user-images.githubusercontent.com/85924566/128641701-c36dbd37-6200-40ef-b2db-22ab8b7682cd.png)
![unable1](https://user-images.githubusercontent.com/85924566/128641715-e460cfa9-b97f-498b-9aee-54206043bafe.png)

- Boostyourself page

![boostyourself](https://user-images.githubusercontent.com/85924566/128641742-61f4cb32-5b0a-4683-85a5-210025b52f0c.png)


**To zoom the image of Boostyourself click on image**

![Screenshot (402)](https://user-images.githubusercontent.com/85924566/128654446-13772bad-df21-4987-b4f5-09b71ed7723c.png)



   
