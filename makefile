all:
	jekyll build

# ssh-add ~/.ssh/id_rsa_rr;
upload:
	eval `ssh-agent`; ssh-add ~/.ssh/id_rsa; git add .;git commit -m “update”;git push origin master; open https://jinhong-park.github.io/arxiv/recent

pull:
	git pull origin master