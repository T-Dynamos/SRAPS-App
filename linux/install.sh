#!/bin/bash
trap 'Echo exiting cleanly...; exit 1;' SIGINT SIGTSTP

checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi

}

checkroot

(trap '' SIGINT SIGTSTP && command -v python3 > /dev/null 2>&1 || { printf >&2  "\e[1;92mInstalling Python3, please wait...\n\e[0m"; apt-get update > /dev/null && apt-get -y install python3  > /dev/null || printf "\e[1;91mPython 3 Not installed.\n\e[0m"; }) & wait $!

echo "Installing Sraps App"
mkdir /opt > /dev/null 2>&1
rm -rf /opt/sraps > /dev/null 2>&1
git clone https://github.com/T-Dynamos/SRAPS-App /opt/sraps
echo "Installing Modules"
pip3 install kivy https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip requests --quiet
echo "Settings Shortcuts"
chmod +x /opt/sraps/linux/run
ln -s /opt/sraps/linux/run /usr/bin/srapsapp
curl https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/linux/sraps.desktop > /usr/share/applications/sraps.desktop
printf "\e[1;92mSRAPS App is installed! . Run from applications \n\e[0m"

