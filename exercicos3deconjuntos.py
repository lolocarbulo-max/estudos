emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
emails_vistos = set()
emails_duplicados = set()
for a in emails:
    if a not in emails_vistos:
        emails_vistos.add(a)
    else:
        emails_duplicados.update(["a@x.com " , "b@x.com"])
        print(emails_duplicados)
         
            
        
        

    
    
