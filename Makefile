default:
	python3 bot.py

start:
	python3 bot.py

install:
	pip3 install -r requirements.txt
	python3 setup.py

# --- dev tools ---
# Make "examples" folder (Unix)
example:
	cp -rv `ls -A | grep -vE ".git|.env|.gitignore|.vscode|README.md|__pycache__|examples|test"` examples
# Make "examples" folder (Windows)
example-win:
	robocopy "." "examples" /xf ".gitignore" ".env" "README.md" /xd "assets" "test" ".vscode" "__pycache__" "examples" ".git" /s
	echo -e "examples" folder was builded!