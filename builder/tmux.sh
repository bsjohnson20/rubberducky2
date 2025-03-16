#!/bin/bash

# Create a new tmux session named "my_session"
tmux new-session -d -s my_session

# Split the window vertically (default layout is horizontal)
tmux split-window -v

# In the first panel, run the make command (replace 'Makefile' or 'target' with your own)
tmux send-keys -t my_session:0.0 "docker logs fastapi-server-app-1 -f" C-m

# In the second panel, run the netcat command (replace 'localhost' and '12345' with your own)
tmux send-keys -t my_session:0.1 "nc -lvnp 9001" C-m

# Attach to the tmux session
tmux attach -t my_session