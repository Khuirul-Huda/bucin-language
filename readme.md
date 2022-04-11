![](https://hits.dwyl.com/Khuirul-Huda/bucin-language.svg?show=unique)

### Bucin Programming Language

Bucin Programming Language - BPL is heart touching programming language. Love yourself before loving others <3. for now just for fun not for production. still just a language translation.  

### Compiling

you can use pyinstaller 

1. ```pip install pyinstaller```
2. ```git clone https://github.com/Khuirul-Huda/bucin-language.git```
3. ```cd bucin-language```
4. ```pyinstaller bucin.py --add-data="./words/basic.json:words"```

### Usage
```bucin <filepath>```

or

```python3 bucin.py <filepath>```


example:
```bucin example.bucin```


### Basic Syntax
```jujur dia itu "baik"``` 
```py
dia = "baik"
```

```sebenarnya aku itu "suka"```
```py
aku = "suka"
```

```ungkapkan("Hello World")```
```py
print("Hello World")
```

### Example

```bucin
jujur dia itu "baik"
sebenarnya aku itu "suka"

klo (dia bener bener "baik") lakuin ini buat dia
    ungkapkan('Hai kakak baik banget deh. boleh kenalan?')
klo gak, lakuin ini buat dia
    ungkapkan('Hai kak, jahad bgt deh')
```

Output: 
```Hai kakak baik banget deh. boleh kenalan?```
