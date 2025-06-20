#```1) შექმენით სია, სადაც შეინახავთ საკვებ პროდუქტებს. სიას მიანიჭეთ შესაბამისი სახელი და გამოიტანეთ იგი ტერმინალში.

food = ["bread","tomato","salad","caesar","shawarma"]
print(food)
# 2) შექმენით სია, რომლის მნიშვნელობებიც იქნება კომპიუტერის აქსესუარები. სიიდან გამოიტანეთ იმ აქსესუარის ინდექსი, რომელსაც ყველაზე ხშირად იყენებთ.

accessories = ["mouse","keyboard","headphones","screen"]
most_used = "keyboard"
index = accessories.index(most.used)
print("most used index: ", index)
# 3) შექმენით ისეთი სია, სადაც შეინახავთ ყველა ნასწავლ მონაცემთა ტიპს ორ-ორჯერ, რომლებსაც მოათავსებთ სხვადასხვა ინდექსებზე. ბოლოს ინდექსინგის საშუალებით გამოიტანეთ მხოლოდ Boolean მნიშვნელობები.

types = ["menu","pizza",2,3,1.4,4.2,True,False]
boolean = [x for x in data_types if type(x) == bool]
print("boolean meanings:", bool)

# 4) მეოთხე დავალების მსგავსად, შექმენით ისეთი სია,თუმცა ამჯერად შეინახეთ ყველა ნასწავლი მონაცემთა ტიპი თითოჯერ. ბოლოს უარყოფითი ინდექსსებით გამოიტანეთ მხოლოდ String ტიპის მნიშვნელობა .```

data = [12,23.1,"pets",True]
string = mixed_data[-3]
print("string type:" string)