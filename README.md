# Rain-Notifier


### How to use this script

- first go to [OpenWeather](https://openweathermap.org/) website and then signup to receive your free api key
- then paste this api key here in the script as a **STRING**: 

![image](https://user-images.githubusercontent.com/84438200/149098569-2b4c34f5-5028-4c3f-84ce-616d67cf198d.png)

- after that go to [twilio.com](https://www.twilio.com/) and signup to receive the auth_token and the account_sid
- then paste these two things here:

![image](https://user-images.githubusercontent.com/84438200/149098973-35a01828-ed86-4045-9e7b-1ec6a975b359.png)

- on [twilio.com](https://www.twilio.com/) you will see something like this:

![image](https://user-images.githubusercontent.com/84438200/149099481-7f8b87d2-59fc-4471-84ae-234fe9c64379.png)

- Instead of TRIAL NUMBER if you're a first time user you will see GENERATE A NUMBER. Click on that to generate your virtual phone number
- Then Enter That **TRIAL NUMBER WHICH YOU GENERATED** and the **PHONE NUMBER you used while signing up for TWILIO** Here:

![image](https://user-images.githubusercontent.com/84438200/149101515-3549ea7d-553c-4b71-8a0b-3f1635581817.png)

- Finally Change the specified coordinates to your own location coordinates 
- you find the coordinates of your own location [Here](https://www.latlong.net/)


### Automating the script
- To automate this task and make it send you an sms everytime it's gonna rain you can use [PythonAnywhere](https://www.pythonanywhere.com/)
- go to this website and signup for a free account and then upload this file there in the FILES option
- then to run this daily at a specfied time go to TASKS and create a new task, specify the time and in the command tab enter **python3 filename.py** in this case python3 main.py
