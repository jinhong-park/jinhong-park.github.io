all:
	jekyll serve --baseurl '' --watch

upload:
	git add .;git commit -m “update”;git push origin master

pull:
	git pull origin master
