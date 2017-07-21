# photo-text
quick tool to convert photo to 0-9 value text, now scales photo

outputs to cmd-line or text file

- pip3 install pillow
- python3 ./pic2text.py --path './pic.jpg' --scale .4

- using the scale option increases readability, .4 is ideal for medium images

## Options

- --path, str of picture path
- --scale, .1 - 1 defaults to .4
- with init of class pic2text(output_file=False)