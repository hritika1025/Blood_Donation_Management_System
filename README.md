# iDonor

- Group 6
# Blood_Donation_Management_System
- Contributers:
Hritika Gautam      - 200001029
Mitika Bhadada      - 200001046
Pradeep Reddy       - 200001005
Chaitanya Dhanorkar - 200001021

The **iDonor** is a **Blood_Donation_Management_System**  designed to help the donors to donate blood to their nearest blood banks and the people who need blood to receive required blood group from the nearby blood banks and active donors.
This website has feature like:
 searching for blood banks in the nearby area, 
 checking blood availability,
 checking eligibility for blood donation,
 taking feedbacks/messages from the users about the website,
 editing the profiles of blood banks and users.

## Instructions For Project Setup

- **Step 1.**
You can directly download the zip file or follow next 2 steps to clone the repo.
Install latest version of git. Open the above github repository link in browser. Click on the code button
and copy HTTPS link.

- **Step 2.**
Create new folder and open git bash inside that folder write command-
```
git clone https://github.com/hritika1025/Blood_Donation_Management_System.git
```
- **Step 3.**
  - Install latest version of python and a code editor (Pycharm or Visual Studio Code).
  - Download & Install MYSQLCLIENT For Python : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient open this link and under MySQLclient select the wheel according to your python version and 32/64 bit windows system. 
  '''
   cmd.

   

   
- **Step 4.**
   Open the project files in the code editor. Open `app.py` file and if your MySQL username and password are not **root** then you can replace the username and password written in `app.py` file with your MySQL username and password.

- **Step 5.**
  **Installing Packages**

  For Visual Studio Code do the following:
   - Open **New Terminal**

   - And now run the following commands in the terminal:
    ```
    python -m venv env
    Set-ExecutionPolicy Unrestricted -Scope Process
    env\scripts\activate
    pip install flask
    $env:FLASK_APP = "app"
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

- **Homepage:
The homepage is the main page of the website. It provides links to check for blood availability, nearby blood banks, information on blood donation. Also it shows the instructions one needs to follow during blood donations.**
![home_page](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/home1.png)
![home_page](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/home2.png)
![home_page](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/home3.png)


- User Registration Page
**User can register themselves with our website to donate blood at the available blood banks or to search for required blood groups from blood banks.**
![user_registration](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/user_registration.png)


- Blood Bank Registration Page
**Blood Banks can register themselves with us using the registration page where they need to fill the required details such as license number, etc.**
![blood_bank_reg](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/blood_bank_reg.png)


- User Login Page
**Page for user login**
![user_login](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/user_login.png)


- Admin Login Page
**Admin can login using admin credentials.**
![admin_login](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/admin_login.png)


- Blood Bank Login Page
**Login page for Blood Banks**
![blood_bank_login](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/blood_bank_login.png)


- User Profile Page
**Users can edit their profile details on this page.**
![user_profile_page](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/user_profile.png)


- Blood Bank Profile Page
**It displays the inforation about the particular blood bank after logging in to the website and the blood bank can edit their profile details here.**
![blood_bank_profile](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/blood_bank_profile.png)


- Search Blood Banks Page
**User can search for blood banks in their area by filling out the location details. The page will show them a list of all the blood banks available in that particular region.**
![nearby_blood_banks](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/nearby_blood_bank.png)


- Blood Availability Page
**Users after logging in with their credentials, can search for required blood group in the area nearest to them.**
![blood_availability](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/check_blood_availability.png)


- Edit blood Stock Page
**Admin can edit the blood stock manually to the database of the website in case of any dispensaries**
![admin_dashboard](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/edit_blood_stock.png)


- Admin Dashboard Page
**After logging in, admin is redirected to this page from where he can go to the User Message to Admin page or to Verification Requests page.**
![admin_dashboard](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/admin_dashboard.png)


- Verification Requests Page
**The admin can approve or reject the requests of blood banks or user from this page.**
![verification_req](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/verification_req.png)


- Contact Page
**Users can send their feedbacks/messages to admin of the website using thiis page.**
![contact_page](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/contact_page.png)


- User Message to Admin Page
**Admin can read the messages/feedbacks sent by the user to him on the user feedbacks page.**
![admin_dashboard](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/feedback.png)


- Non-Eligibility Page
**It shows the required conditions that are needed by a persson to be eligible to donate bloood to the blood banks.**
![non_eligibility](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/Non_eligibility.png)


- Donor List
**It shows the list of active donors along with their other necessary information.**
![donor_list](https://github.com/hritika1025/Blood_Donation_Management_System/blob/main/static/images/Screenshots2/donor_list.png)



