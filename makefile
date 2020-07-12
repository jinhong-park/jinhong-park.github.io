all:
	jekyll serve --baseurl '' --watch

upload:
	eval `ssh-agent`; ssh-add ~/.ssh/id_rsa; git add .;git commit -m “update”;git push origin master

pull:
	git pull origin master