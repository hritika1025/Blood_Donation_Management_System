INSERT INTO Blood_bank (Password, License_Number, Blood_bank_name, Owner_name, email1, phone_num1, Address, Pincode, City, State, Website)
VALUES
('riz345', '32564178', 'Rotary Blood Bank', 'Varun Tiwari', 'rotarybank321@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('e5hgvs', '25647895', 'Supppot2Care', 'Neha Sharma', 'support2care2@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('rtl654yb', '69874328', 'Right To Live', 'Ahmed Joshi', 'righttollive12@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('354abb6gr', '45587556', 'Aadhar Blood Bank', 'Rohit Kapoor', 'aadhar456@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('sbb35342', '23699875', 'Sanjeeev Blood Bank', 'Anuj Bajpayee', 'sanjeevcare5@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('jbb6674', '57148222', 'Jeevan Blood Bank', 'Rekha Kumar', 'jeevanbloodbank@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('Save2Live44', '56324417', 'SaveLives Foundation', 'Rishabh Mehta', 'savelives121321@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com'),
('Rcs33', '87546698', 'Red Cross Society', 'Kartik Jaseja', 'redcrosssocietyofficial@gmail.com', 96542135470, 'New Nehru Square, Jhanshi Street, Hyderabad', '500042', 'Hyderabad', 'Telangna', 'www.rotarybankhyedrabad.com');

INSERT INTO Blood_bank_timings (License_Number, Opening_time, Closing_time, Weekday)
VALUES
('32564178', '22:00', '16:00', 'Monday'),
('25647895', '22:00', '16:00', 'Wednesday'),
('69874328', '22:00', '16:00', 'Thursday'),
('45587556', '22:00', '16:00', 'Saturday'),
('23699875', '22:00', '16:00', 'Monday'),
('57148222', '22:00', '16:00', 'Wednesday'),
('56324417', '22:00', '16:00', 'Thursday'),
('87546698', '22:00', '16:00', 'Monday');

INSERT INTO Blood_stock (Id, License_Number, Blood_group, Adding_date, Removing_date, Units_added, Units_removed)
VALUES
('1', '32564178', 'A +ve', '2021-08-22', '2021-07-27', '2340', '540'),
('2', '25647895', 'A +ve', '2021-08-22', '2021-07-16', '3654', '200'),
('3', '69874328', 'A +ve', '2021-08-22', '2021-08-02', '1063', '2220'),
('4', '45587556', 'A +ve', '2021-08-22', '2021-08-15', '1300', '150'),
('5', '23699875', 'A +ve', '2021-08-22', '2021-09-23', '4521', '630'),
('6', '57148222', 'A +ve', '2021-08-22', '2021-10-20', '820', '360');

INSERT INTO Donor (Email_id, Password, First_name, Last_name, Age, Gender, Blood_group, Eligibility, Phone_num, Address, City, District, Pincode, State)
VALUES
('chaitanya123@gmail.com', 'cht432', 'Chaitanya', 'Dhanorkar', '19', 'Male', 'B +ve', 'TRUE', 6547812498, 'Rajiv Street, Dabha', 'Nagpur', 'Nagpur', '442233', 'Maharashtra')
('mitika243@gmail.com', 'cht432', 'Mitika', 'Bhadada', '19', 'Female', 'A +ve', 'TRUE', 9856421368, 'Hazariganj Area', 'gandhinagar', 'Gandhinagar', '600124', 'Gujrat')
('hritika674@gmail.com', 'cht432', 'Hritika', 'Gautam', '19', 'Female', 'B +ve', 'TRUE', 8788542631, 'Kushal Society', 'Bengaluru', 'Bengaluru', '547896', 'Karnataka')
('pradeepreddy1@gmail.com', 'cht432', 'Pradeep', 'Reddy', '19', 'Male', 'AB +ve', 'TRUE', 9421569875, 'Aquare XYZ', 'Nagpur', 'Nagpur', '400036', 'Delhi')
('aditya234@gmail.com', 'cht432', 'Aditya', 'Deshmukh', '19', 'Male', 'A +ve', 'TRUE', 9021365478, 'Street ABC', 'Bhopal', 'Bhopal', '755001', 'Madhya Pradesh')
('ujjwal999@gmail.com', 'cht432', 'Ujjwal', 'Hendwe', '19', 'Male', 'O +ve', 'TRUE', 8032147598, 'Trinity Society, PQR', 'Panaji', 'Panaji', '633001', 'Goa')

INSERT INTO Donations (Email_id, Date, Units, Blood_group)
VALUES
('chaitanya123@gmail.com', '2021-09-02', '1', 'B +ve'),
('mitika243@gmail.com', '2021-09-17', '2', 'A +ve'),
('hritika674@gmail.com', '2021-10-24', '4', 'B +ve'),
('pradeepreddy1@gmail.com', '2021-07-02', '3', 'AB +ve'),
('aditya234@gmail.com', '2021-08-09', '1', 'A +ve'),
('ujjwal999@gmail.com', '2021-09-12', '4', 'O +ve');

INSERT INTO Notif_Admin_to_Blood_bank ('Id', 'License_Number', 'Message', 'Date')
VALUES
(1, '32564178', "Donated this much units", '2021-07-27'),
(2, '25647895', "Donated this much units", '2021-07-16'),
(3, '69874328', "Donated this much units", '2021-08-02'),
(4, '45587556', "Donated this much units", '2021-08-15'),
(5, '23699875', "Donated this much units", '2021-09-23'),
(6, '57148222', "Donated this much units", '2021-10-20');

INSERT INTO Notif_Blood_bank_to_Donor (Id, Blood_bank_user, Donor_user, Message, Date)
VALUES
(1, 'Varun Tiwari', 'Mitika', 'This is a demo message', '2021-08-06'),
(2, 'Neha Sharma', 'Chaitanya', 'This is a demo message', '2021-08-14'),
(3, 'Ahmed Joshi', 'Ujjwal', 'This is a demo message', '2021-09-16'),
(4, 'Rohit Kapoor', 'Pradeep', 'This is a demo message', '2021-10-02'),
(5, 'Rishabh Mehta', 'Hritika', 'This is a demo message', '2021-09-09'),
(6, 'Rekha Kumar', 'Aditya', 'This is a demo message', '2021-10-10');

INSERT INTO Notif_Admin_to_Donor (Id, Donor_user, Message, Date)
VALUES
(1, 'Chaitanya', 'This is another demo message', '2021-09-19'),
(2, 'Aditya', 'This is another demo message', '2021-09-12'),
(3, 'Ujjwal', 'This is another demo message', '2021-10-19'),
(4, 'Chaitanya', 'This is another demo message', '2021-08-05'),
(5, 'Chaitanya', 'This is another demo message', '2021-08-06'),
(6, 'Chaitanya', 'This is another demo message', '2021-09-16');

INSERT INTO Message_to_admin (Id, Name, Email_id, phone_num, Message, Date)
VALUES
(1, 'Aditya', 'aditya234@gmail.com', 9021365478, 'Demo Message', '2021-10-30'),
(2, 'Chaitanya', 'chaitanya123@gmail.com', 6547812498, 'Demo Message', '2021-10-30'),
(3, 'Aditya', 'aditya234@gmail.com', 9021365478, 'Demo Message', '2021-10-30'),
(4, 'Mitika', 'mitika243@gmail.com', 9856421368, 'Demo Message', '2021-10-30'),
(5, 'Pradeep', 'pradeepreddy1@gmail.com', 9421569875, 'Demo Message', '2021-10-30'),
(6, 'Pradeep', 'pradeepreddy1@gmail.com', 9421569875, 'Demo Message', '2021-10-30');

INSERT INTO Post_by_admin (Id, Heading, Post, Date)
VALUES
(1, 'Notice to all users', 'Demo Post 1', '2021-08-23'),
(2, 'Notice to blood banks', 'Demo Post 2', '2021-08-24'),
(3, 'Notice to donors', 'Demo Post 3', '2021-08-25'),
(4, 'Notice to all active donors', 'Demo Post 4', '2021-08-26'),
(5, 'Notice from admin', 'Demo Post 5', '2021-08-27'),
(6, 'Important Notice', 'Demo Post 6', '2021-08-28');




