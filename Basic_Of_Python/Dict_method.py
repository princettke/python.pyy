marks ={
  "kushal":100,
  "harrypoter":56,
  "Rohan":34,
  
}
print(marks.items())
# for only keys 
print(marks.keys())
marks.update({"kushal":99 ,"prince":89}) #for add and update the dictonory
print(marks)
print(marks.get("kushal"))
#diif b/w get or normal methods to print 
print(marks.get("kushal200")) # prints none agar nhi h toh but error nhi dega 

print(marks["kushal200"]) # prints error when item does not exist
