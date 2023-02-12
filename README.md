# marp-python

## Python library for generating [Marp](https://github.com/marp-team/marpit) presentations. This lib helps to automatically generate presentations with simple builder class. 

For correct work please install marp-cli:
1. download latetst [binary file](https://github.com/marp-team/marp-cli/releases)
2. mv marp /usr/local/bin

## Getting started
[Marp](https://github.com/marp-team/marpit) is open source project, that allows to generate pptx, html, png, notes or pdf presentations from .md files. This library generates correct syntax for .md files and then convert it to presentation with [marp-client](https://github.com/marp-team/marp-cli).
Example:
```
css = open("theme.css", "r").read()
presentation = Presentation(css = css)
presentation.add_slide("Marp presentation", "Marp presentation preview",{'backgroundColor': '#f7d064'}, 
                        {'image': 'logo.jpeg', 'is_background': True, 'bg_position': 'left'})
presentation.save('example.pptx')
```
For bullet list divide each bullet with -, * or +. Alternatively you can pass numbered list. Pass text parameter as follows:
```
"1. First bullet \n2. Second bullet \n ..."
"- First bullet \n- Second bullet \n ..."
```

If you wish to set custom css, the slide "body" class is named "section". For more info read official [docs](https://marpit.marp.app/theme-css).

Example of image params struct:
| pararm        |description                             |
|---------------|------------------------------------------------|
| image         | image path or url                              |
| is_background | bool is image background                       |
| bg_position   | position of background (left, right, vertical) |
| split_pct     | percent of background that image take          |
| size          | size of bg (cover, contain, fit, auto, x%)     |

For filter:
| param  | description                                                                             |
|--------|-----------------------------------------------------------------------------------------|
| image  | image path or url                                                                       |
| filter | blur, brightness, contrast, drop-shadow, grayscale, hue-rotate, invert, opacity, saturate,sepia |
| value  | filter value                                                                            |

For image:
| param  | description       |
|--------|-------------------|
| image  | image path or url |
| width  | image width       |
| height | image height      |
