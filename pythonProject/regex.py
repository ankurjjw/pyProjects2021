import re

sampleText = 'Batwowowowoman'

batRegex = re.compile(r'Bat(wo)*')
mo = batRegex.search(sampleText)
print(mo.group())

sampletext = 'My phone numbers are 5089811702+5083092391 9830658057 . Whay say Batwowowowowoman'
batRegex = re.compile(r'(\d\d\d\d\d\d\d\d\d\d( )?(\+)?)+')
mo = batRegex.search(sampletext)
print(mo.group())
batRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = batRegex.findall(sampletext)
print(mo)

sampleText = '12 holly, 13 molly, 14 sally, 15 dolly'
shRegex = re.compile(r'\d+\s\w+')
mo = shRegex.findall(sampleText)
print(mo)

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('50898x11702')
print(mo)
