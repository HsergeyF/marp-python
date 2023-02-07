# marp-python
## Python library for generating Marp presentations. This lib helps to automatically generate presentations with simple builder class. 

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