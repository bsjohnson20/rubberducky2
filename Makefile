all: build_server build/rubbyDucky.sh clone docker run_tmux



build/rubbyDucky.sh: 
	./builder/base64.sh
	
build_server:
	./builder/build_server.sh

run_server:
	uv run build_server/main.py

run_tmux:
	./builder/tmux.sh

.PHONY: docker
docker:
	cd docker && ./run.sh

clean:
	rm docker/docker_server -r
	rm build -r
	rm build_server -r

clone:
	./builder/uploadGit.sh


