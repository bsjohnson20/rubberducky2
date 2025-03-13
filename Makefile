all: build/rubbyDucky.sh clone clean

build/rubbyDucky.sh: 
	./builder/base64.sh
	
clean:
	rm build -r

clone:
	./builder/uploadGit.sh