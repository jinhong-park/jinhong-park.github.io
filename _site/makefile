all:
	jekyll build

upload:
	eval `ssh-agent`; ssh-add ~/.ssh/id_rsa_mac16; git add .;git commit -m “update”;git push origin master

pull:
	git pull origin master