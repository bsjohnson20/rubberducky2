all: build/rubbyDucky.sh clone build_server run_tmux

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
	rm build -r
	rm build_server -r

clone:
	./builder/uploadGit.sh


