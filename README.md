# marp-python
## Python library for generating Marp presentations. This lib helps to automatically generate presentations with simple builder class. 

For correct work please install marp-cli:
1. download latetst [binary file](https://github.com/marp-team/marp-cli/releases)
2. mv marp /usr/local/bin

Example:

```
presentation = Presentation()
presentation.add_slide("Optimization 2022", 'Optimization results preview',{'backgroundColor': '#f7d064'}, 
                        {'image': 'logo.jpeg', 'is_background': True, 'bg_position': 'left'})
presentation.save('example.md')
```
Example of image params struct:
```
{
    'image': 'logo.jpeg',
    'is_background': True,
    'bg_position': 'left',
    'split_pct':'33%'
}
```
For filter:
```
{
    'image': 'logo.jpeg',
    'filter': 'blur'
}
```
For image:
```
{
    'image': 'logo.jpeg',
    'width': '100px'
}
```

For bullet list divide each bullet with -, * or +. Alternatively you can pass numbered list. Pass text parameter as follows:
```
"1. First bullet \n2. Second bullet \n ..."
"- First bullet \n- Second bullet \n ..."
```