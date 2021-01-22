# Terminal Prettifier
This is terminal output highliter with customizable config. If you ever wanted to have a prettier ping
command or prettier interactive shells output, it's a script for you! just add `color` to the begining of
the command you want to execute, and bam! It's so PRETTIER now.

### Example Ping
```html
<pre><font color="#4E9A06">color</font> ping 8.8.8.8
<font color="#D3D7CF">PING</font> <font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font> <font color="#06989A">(</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#06989A">)</font> <font color="#3465A4">56</font><font color="#06989A">(</font><font color="#3465A4">84</font><font color="#06989A">)</font> <font color="#D3D7CF">bytes</font> <font color="#D3D7CF">of</font> <font color="#D3D7CF">data</font><font color="#CC0000">.</font>
<font color="#3465A4">64</font> <font color="#D3D7CF">bytes</font> <font color="#D3D7CF">from</font> <font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">:</font> <font color="#D3D7CF">icmp_seq</font><font color="#C4A000">=</font><font color="#3465A4">1</font> <font color="#D3D7CF">ttl</font><font color="#C4A000">=</font><font color="#3465A4">108</font> <font color="#D3D7CF">time</font><font color="#C4A000">=</font><font color="#3465A4">75</font><font color="#CC0000">.</font><font color="#3465A4">6</font> <font color="#C4A000">ms</font>
<font color="#3465A4">64</font> <font color="#D3D7CF">bytes</font> <font color="#D3D7CF">from</font> <font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">:</font> <font color="#D3D7CF">icmp_seq</font><font color="#C4A000">=</font><font color="#3465A4">2</font> <font color="#D3D7CF">ttl</font><font color="#C4A000">=</font><font color="#3465A4">108</font> <font color="#D3D7CF">time</font><font color="#C4A000">=</font><font color="#3465A4">63</font><font color="#CC0000">.</font><font color="#3465A4">2</font> <font color="#C4A000">ms</font>
<font color="#3465A4">64</font> <font color="#D3D7CF">bytes</font> <font color="#D3D7CF">from</font> <font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">:</font> <font color="#D3D7CF">icmp_seq</font><font color="#C4A000">=</font><font color="#3465A4">3</font> <font color="#D3D7CF">ttl</font><font color="#C4A000">=</font><font color="#3465A4">108</font> <font color="#D3D7CF">time</font><font color="#C4A000">=</font><font color="#3465A4">63</font><font color="#CC0000">.</font><font color="#3465A4">0</font> <font color="#C4A000">ms</font>
<font color="#3465A4">64</font> <font color="#D3D7CF">bytes</font> <font color="#D3D7CF">from</font> <font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">:</font> <font color="#D3D7CF">icmp_seq</font><font color="#C4A000">=</font><font color="#3465A4">4</font> <font color="#D3D7CF">ttl</font><font color="#C4A000">=</font><font color="#3465A4">108</font> <font color="#D3D7CF">time</font><font color="#C4A000">=</font><font color="#3465A4">89</font><font color="#CC0000">.</font><font color="#3465A4">9</font> <font color="#C4A000">ms</font></pre>
```

### Example Python
<pre><font color="#4E9A06">color</font> python3
<font color="#D3D7CF">Python</font> <font color="#3465A4">3</font><font color="#CC0000">.</font><font color="#3465A4">8</font><font color="#CC0000">.</font><font color="#3465A4">5</font> <font color="#06989A">(</font><font color="#D3D7CF">default</font><font color="#CC0000">,</font> <font color="#D3D7CF">Jul</font> <font color="#3465A4">28</font> <font color="#3465A4">2020</font><font color="#CC0000">,</font> <font color="#3465A4">12</font><font color="#CC0000">:</font><font color="#3465A4">59</font><font color="#CC0000">:</font><font color="#3465A4">40</font><font color="#06989A">)</font> 
<font color="#06989A">[</font><font color="#D3D7CF">GCC</font> <font color="#3465A4">9</font><font color="#CC0000">.</font><font color="#3465A4">3</font><font color="#CC0000">.</font><font color="#3465A4">0</font><font color="#06989A">]</font> <font color="#D3D7CF">on</font> <font color="#D3D7CF">linux</font>
<font color="#D3D7CF">Type</font> <font color="#CC0000">&quot;</font><font color="#D3D7CF">help</font><font color="#CC0000">&quot;,</font> <font color="#CC0000">&quot;</font><font color="#D3D7CF">copyright</font><font color="#CC0000">&quot;,</font> <font color="#CC0000">&quot;</font><font color="#D3D7CF">credits</font><font color="#CC0000">&quot;</font> <font color="#D3D7CF">or</font> <font color="#CC0000">&quot;</font><font color="#D3D7CF">license</font><font color="#CC0000">&quot;</font> <font color="#D3D7CF">for</font> <font color="#D3D7CF">more</font> <font color="#D3D7CF">information</font><font color="#CC0000">.</font>
<font color="#C4A000">&gt;&gt;&gt;</font> a = [&quot;123&quot;, &quot;hello!&quot;]
<font color="#C4A000">&gt;&gt;&gt;</font> print(a)
<font color="#06989A">[</font><font color="#CC0000">&apos;</font><font color="#3465A4">123</font><font color="#CC0000">&apos;,</font> <font color="#CC0000">&apos;</font><font color="#D3D7CF">hello</font><font color="#C4A000">!</font><font color="#CC0000">&apos;</font><font color="#06989A">]</font>
<font color="#C4A000">&gt;&gt;&gt;</font> b = &quot;&lt;&lt;(some awesome text!)&gt;&gt;{}&quot;   
<font color="#C4A000">&gt;&gt;&gt;</font> b
<font color="#CC0000">&apos;</font><font color="#C4A000">&lt;&lt;</font><font color="#06989A">(</font><font color="#D3D7CF">some</font> <font color="#D3D7CF">awesome</font> <font color="#D3D7CF">text</font><font color="#C4A000">!</font><font color="#06989A">)</font><font color="#C4A000">&gt;&gt;</font><font color="#06989A">{}</font><font color="#CC0000">&apos;</font></pre>

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
<pre><font color="#4E9A06">color</font> echo shamir0xe  
<font color="#CC0000">s</font><font color="#3465A4">h</font><font color="#CC0000">a</font><font color="#3465A4">m</font><font color="#CC0000">i</font><font color="#3465A4">r</font><font color="#CC0000">0</font><font color="#3465A4">x</font><font color="#CC0000">e</font>
</pre>

You can specify more colors to the text you want to highlight, by adding more letters to the color section.
For example this could be use for painting every letter with every color we have:

    SN shamir0xe GBRCMYW

then output should be something like this:
<pre><font color="#4E9A06">color</font> echo shamir0xe
<font color="#06989A">s</font><font color="#75507B">h</font><font color="#4E9A06">a</font><font color="#CC0000">m</font><font color="#D3D7CF">i</font><font color="#C4A000">r</font><font color="#3465A4">0</font><font color="#06989A">x</font><font color="#75507B">e</font>
</pre>

As you see, the program shuffles the list of the colors for each config when it wants to print them. This is
added for fun, and will be optional in the next releases.
