

all: build/rubbyDucky.sh

build/rubbyDucky.sh: 
	./builder/base64.sh
	./builder/uploadGit.sh

clean:
	rm build -r

clone:
	ssh-agent bash -c 'ssh-add rubbyducky; git clone git@gist.github.com:e3c7d56524bcba9a0eff319676611d5f.git'