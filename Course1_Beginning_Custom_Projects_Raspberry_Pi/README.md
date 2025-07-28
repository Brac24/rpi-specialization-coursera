Some notes for module 1.

I'm taking a while in this section because I want to do it the most correct and best practice way but that might just be a waste of time.
I could just follow along exactly as the the lectures say for the react web app portion but I'm adamant on doing it the best way.
I have decided to try to use vite instead of the lecture suggested way using create-react-app
The React documentation itself says to no longer use create-react-app because it is deprecated and no longer maintained.
I am using a tutorial from Miguel Grinberg here https://blog.miguelgrinberg.com/post/create-a-react-flask-project-in-2025.
The instructor also suggested Miguel Grinberg for flask tutorials so this works out great.
Miguel recently updated his tutorial on react and flask project to use Vite instead of create-react-app.

To use Vite we need to have nodejs and npm installed first.
Initially I used the command: sudo apt install nodejs
The above line installed version 18 of nodejs but the most current is 22.
Also Vite requires version 20 of nodejs to work.
To update it I had to use a different repo than where apt gets its packages from.
To use a different repo I ran: curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
After running the curl command I then installed with: sudo apt-get install nodejs -y and it installed version 22 of nodejs
For npm I also had to install that separately with: sudo apt intall npm
apt also installed an older version of npm.
To update npm I ran: npm update -g npm
and the above command updated to version 11.

After I setup nodejs and npm I did a bit more reading and found that nvm (Node Version Manager) was the recommended way of installing nodejs. Web development and its tools seems to be so saturated with updates and different ways of doing things because of how fast web dev tools change which can be a bit frustrating.


