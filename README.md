# Terminal Prettifier
This is terminal output highliter with customizable config. If you ever wanted to have a prettier ping
command or prettier interactive shells output, it's a script for you! just add `color` to the begining of
the command you want to execute, and bam! It's so PRETTIER now.

### Example Ping
<img src="readme/images/ping.png" alt="ping" width="555"/>

### Example Python
<img src="readme/images/python.png" alt="python" width="600"/>

## Installation
Clone this library and add the `color` bash file as an alias to your environment variables.
```bash
alias color=`bash /PATH-TO-THIS-LIBRARY/TerminalPrettifier/color`
```
Then open new terminal and use color before command you want to use.
You need to have `python3` in your path. compatibility tested for `python >= 3.6`. You can also change the
python name at the bottom of the page in `color` bash file by yourself:
```bash
eval $command 2>&1 | python3 $py_exe
```
## Configuration
You can edit the configuration file and customize it. The config file is placed in the root directory
of the TerminalPrettifier folder named `.prettifier_cfg`. You can change the colors of each section and 
and set it to one of color names provided in `src/colors.py`. Colors list are as follow:
* Green
* Blue
* Red
* Cyan
* Magenta
* Yellow
* Black
* White

You can define special names painting with keyword **SN** in the config file. Also you can choose how you want to paint the word with a sequence of first letter of colors in uppercase foramt. For example if you want to change *shamir0xe* into red and blue, you can add something like this to the config:

    SN shamir0xe RB

then the output should be like this:

<img src="readme/images/shamir0xeRGB.png" alt="RB" width="222"/>

You can specify more colors to the text you want to highlight, by adding more letters to the color section.
For example this could be use for painting every letter with every color we have:

    SN shamir0xe GBRCMYW

then output should be something like this:

<img src="readme/images/shamir0xeRB.png" alt="GBRCMYW" width="222"/>

As you see, the program shuffles the list of the colors for each config when it wants to print them. This is
added for fun, and will be optional in the next releases.
