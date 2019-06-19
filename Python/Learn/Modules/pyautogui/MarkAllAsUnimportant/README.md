# Mark All As Unimportant

When searching through my e-mail I noticed a lot of messages were marked as _important_. However, they either were not important, or in fact were important but back a few months ago. Now these markers were irrelevant and misguiding, cluttering my _Importants_ inbox with more than 1,300 emails. After searching for an automated solution, like right-cliking and disabling importance of selected e-mails, I couldn't find anything, so I decided to use `pyautogui` to solve my problems.

I made sure to save the three types of "activated" important marker icons inside the `images` directory as PNG images. If there were any new icons, or if you were to reuse this script to click on other icons, you may change the images inside te `images` folder and the program will automatically adapt. The script will take a screenshot and click on every match forever for every second+ (the algorithm takes time to execute)
