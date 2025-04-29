#!/bin/bash
# filepath: /home/arjun/dev/sink_iot/run_all.sh

# Paths
VENV_PATH="/home/arjun/dev/sink_iot/venv"
NOTES_UI_PATH="/home/arjun/dev/sink_iot/notes-ui"

# 1. Flask proxy (in venv)
tmux new-session -d -s flask-proxy "export export GOOGLE_APPLICATION_CREDENTIALS="/home/arjun/.google/cpsc341-455603-42d7eb9255f6.json" && source venv/bin/activate && python server.py"

# 2. Image uploader (in venv)
tmux new-session -d -s img-uploader "source venv/bin/activate && python img_uploader.py"

# 3. Image processor (outside venv)
tmux new-session -d -s img-processor "python img_processor.py"

# 4. React npm app (outside venv)
tmux new-session -d -s notes-ui "cd notes-ui && npm run dev"

echo "All services started in tmux sessions:"
echo "  flask-proxy, img-uploader, img-processor, notes-ui"
