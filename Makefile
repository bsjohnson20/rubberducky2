

all: build/rubbyDucky.sh clone

build/rubbyDucky.sh: 
	./builder/base64.sh
	rm build -r
	
clean:
	rm build -r

clone:
	./builder/uploadGit.sh