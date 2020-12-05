all:
	jekyll build

upload:
	eval `ssh-agent`; ssh-add ~/.ssh/id_rsa_rr; git add .;git commit -m “update”;git push origin master

pull:
	git pull origin master