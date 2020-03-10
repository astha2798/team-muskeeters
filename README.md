# Musketeers
<u><b> Gate Entry Management System </u> </b>

The Hostels nation wide has an entry system where inhabitants have to make an entry when they leave
and enter the premises, mentioning their name, id number and the timings. This project was made,
keeping in mind the girls hostel of NIT Hamirpur who have to do an entry whenever they come and go
and also mark their attendance after 9:30PM.

The project recognizes faces when they enter and leave the system and make an entry in the database.
After 9:30PM (That is the in-timing) it announces the names of the students whose entry have not been
closed (using text to speech conversion). After 10:00PM if the student has still not reached the camera,
a notification goes on the attendants phone informing her of students absence.

<b> PREREQUISITES </b>
<br> <ul>
  <li> Python </li>
  <li> Verified </li> 
  <li> Twilio account </li>
  <li> Media Player </li>
  <li> Eclipse </li>
  </ul>

<b> DATABASE USED </b>
<br> <ul>
  <li>MySQL</li> </ul>

<b>LIBRARIES USED </b>
<br> <ul>
  <li> Dlib </li>
<li> Opencv </li>
<li> Tensorflow </li>
<li> Keras </li>
<li> Sklearn </li>
<li> Pillow </li>
<li> gtts </ul>

<b>ARCHITECTURE USED</b>
<br>
Convolutional Neural Network

<b>PIPELINE</b>
<br>
Image -&gt; FaceDetection -&gt; CroppedFace -&gt; FaceRecognition -&gt; Descriptor(128D) -&gt;
FaceClassifier -&gt; Name -&gt; Database entry made -&gt; Text to speech coversion of tupples
marked Absent -&gt; Notification sent 

<b>CSV File Generation</b>
<br>
Multiple pictures of students will be taken during registration. The excel sheet will then
contain their picture name, student name and the id number. The csv file will then be
extracted from the Excel.
