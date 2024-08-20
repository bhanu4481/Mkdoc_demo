from markdown import markdown

input = "C:/Users/User/OneDrive/Desktop/Mkdoc Project/backend/resources/file1.md"
html = markdown(open(input,'r',errors = 'ignore').read())

output = "C:/Users/User/OneDrive/Desktop/Mkdoc Project/backend/resources_transformed/file1.html"
f = open(output,'x')
f.write(html)
f.close()