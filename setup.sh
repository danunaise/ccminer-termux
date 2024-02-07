apt-get update -y
apt-get upgrade -y
apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y


apt-get install python3 -y
apt-get install pip -y
apt-get install python3-requests -y
apt-get install python3-venv -y
apt-get install python3-colored -y

mv mining ../../etc
mv startminer ../../bin
mv editminer ../../bin

chmod +x startminer
chmod +x editminer

cd && cd ../etc/mining/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

chmod +x ccminer

cd && cd ../etc
nano bash.bashrc

startminer